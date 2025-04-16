# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 10:17:44 2022

@author: rmish
"""
# using Anaconda, install the ffmpeg package:
# conda install -c conda-forge ffmpeg
#%%Initialization
import numpy as np
import Fig6_modeling_convolution as mc
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import cmcrameri.cm as cm
from skimage.transform import rescale, resize, downscale_local_mean
import matplotlib.animation as animation
import pandas as pd
import time
# plt.ioff()
plt.style.use('dark_background')
# ns = np.arange(10,61,2)
#%%Function (discretization)
def callbackF(x,f,accept):
    attempts.append([x,f,accept])

#%% Kernel and initial size and sender num
ns = [20]  #number of generators*2
ss = [22] #grid size
# s = 22
#a and b were taken from model_Bfit_8hr_v9b. asd = 3.75, bsd = 0.81
a = 7.68
b = 8.79

# ss = [22,30,40,50,60,70,80,90,100] [15,25,35,45,55,65]
for s in ss:
    for n in ns:
        for i in [45]:
            t1 = time.time()            
            label='ai_s'+str(s)+'_g'+str(n)+'_t'+str(i)+'_v7'
    
            print('generators:', n)
            print('size:' , s)
            print('i:',i)
            kernel = a*mc.dkernel(s,b)        
            tp = np.load('Fig6_target_pattern.npy')
            tpnorm = (tp-np.min(tp))/(np.max(tp)-np.min(tp))
            turing_target = tpnorm[i:i+s,i:i+s]
            t1 = resize(turing_target,(s-4,s-4),preserve_range=True)
            turing_target = np.pad(t1,[2,2])            
            tspline = mc.spline_interp(t1)

            plt.imshow(np.pad(tspline,[2,2]),cmap=cm.oslo)
            plt.axis('off')
            plt.axis('equal')
            plt.savefig('text'+str(i)+'.svg')
            plt.figure()
            #%%
            senderlocs = np.array(np.random.randint(0,s,size=20),dtype=np.float64)
            plt.scatter(senderlocs[1::2]*100/s,senderlocs[::2]*100/s,c='r')
            plt.axis('off')
            plt.axis('equal')
            plt.savefig('initial_scatter_v3.svg')

            m,p = mc.conv_plotter2(senderlocs, s, kernel)
            tspline = mc.spline_interp(m)
            plt.imshow(tspline,cmap=cm.oslo)

            plt.savefig('conv_model_v3.svg')

            
            #%%
            initial_guess = senderlocs
            attempts = []
            
            #%%optimization
            mkwargs = {'method': 'CG'}
            minimizer_kwargs = {"args": (kernel,turing_target,s)}
            result = optimize.basinhopping(mc.f6, initial_guess,disp = True,stepsize = n*0.13,
                                           niter_success=100,T=0.02,interval=30,callback=callbackF,minimizer_kwargs = minimizer_kwargs)#,bounds = blist)#,options = {1000sc,disp=True})    
            
            #%%save results
            fitted_params = result.x
            # np.save('fitted_params_size'+str(s)+'_senders'+str(int(n/2))+'texture'+str(i)+'_v7b.npy',fitted_params)
            allinfo = pd.DataFrame(attempts,columns = ['x','f','accept'])
            allinfo.to_pickle(label+'.pkl')
            print('initial guess: ', np.array(initial_guess,np.uint8))
            print('fitted locs: ',fitted_params)            
            
            #%%plotting
            ai = allinfo.copy()          
            numframes = len(ai)
            tspline = mc.spline_interp(t1)
            
            fig, ax = plt.subplot_mosaic("ABC;DDD",dpi=200)        
            ax['A'].imshow(tspline , cmap = cm.oslo)
            ax['A'].title.set_text('target texture')
            ax['D'].set_xlabel('Generation Number')
            ax['D'].set_ylabel('Loss F')
            ax['A'].set_axis_off()
            ax['B'].set_axis_off()
            ax['C'].set_axis_off()
            plt.tight_layout()
            ani = animation.FuncAnimation(fig, mc.update_plot_v1, frames=range(numframes),
                                          fargs=(ax,ai,s,kernel))
            ani.save(label+'.mp4')
            tdiff = time.time()-t1
            print('total time for this round: '+str(tdiff))
        