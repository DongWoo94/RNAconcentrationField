# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:56:03 2022

@author: rmish
"""

import numpy
import pandas as pd
import cmcrameri as cmc
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
from scipy.interpolate import griddata
from scipy import interpolate
plt.style.use('default')

def HWHM(xumtot,ctot):
    z1 = ctot
    yToFind = np.max(z1)/2    
    yreduced = np.array(z1) - yToFind
    freduced = interpolate.UnivariateSpline(xumtot, yreduced, s=0)
    # print(freduced.roots())
    return freduced.roots()[-1]

fs=15

toplot = pd.read_table('Fig1_data.txt',delimiter='      ',names=['x','y','c'],engine='python')
x1 = toplot.x.to_numpy()
c1 = toplot.y.to_numpy()

xumtot = x1[:int(len(x1)/2)]
ctot = c1[int(len(x1)/2):]
plt.figure(dpi=150)
plt.tight_layout()
# for i in [1]:
#     xumtot, ctot = patchRNA(kp,Tc,L,n2,kDss*i,Dss)
plt.plot(xumtot,ctot,linewidth=5,c='k')
plt.ylabel('Concentration (nM)',fontsize=fs,weight='bold')
plt.xlabel(r'Distance from center ($\mu$m)',fontsize=fs,weight='bold')
plt.xticks(fontsize=fs,weight='bold')
plt.yticks(fontsize=fs,weight='bold')
plt.locator_params(nbins=6)
ax = plt.gca()

plt.xlim([0,500])
plt.ylim([-1,150])
z = HWHM(xumtot,ctot)
# ax.set_aspect('equal')#, 1'box')

t2 = toplot.sort_values(by = ['x','y'])
X, Y = np.meshgrid(toplot.x,toplot.y)
z = np.trapz(ctot,xumtot)


plt.savefig('RNA_numpatch_v1.svg', format='svg',bbox_inches = 'tight')
plt.savefig('RNA_numpatch_v1.png', format='png',bbox_inches = 'tight')

#%%


pRD_free = pd.read_table('rep_model_v1.txt',delim_whitespace=True,header=0)
dist_free = pRD_free.x-1500
print(HWHM(dist_free,pRD_free.Height))


plt.figure(dpi=150)
plt.plot(dist_free,pRD_free.Height,linewidth=3)
print(HWHM(dist_free,pRD_free.Height))
plt.ylabel('Concentration (nM)',fontsize=fs,weight='bold')
plt.xlabel(r'Distance from Center ($\mu$m)',fontsize=fs,weight='bold')
plt.xticks(fontsize=fs,weight='bold')
plt.yticks(fontsize=fs,weight='bold')
plt.locator_params(nbins=6)
plt.xlim(-1000,1000)
# plt.legend([r'[S]','[R:S],$k_{off}$ = 0.0002','[R:S],$k_{off}$ = 0.002','[R:S],$k_{off}$ = 0.02','[R:S],$k_{off}$ = 0.2'],loc='upper right', fontsize=fs-2)
save_label = 'freeRD_scaled'
plt.savefig(save_label+'.svg', format='svg')
plt.savefig(save_label+'.png', format='png')


z = np.trapz(pRD_free.Height[163:],dist_free[163:])

#%%
toplot = pd.read_table('rC2_conc_v1.txt',delimiter='      ',names=['x','y','c'],engine='python')
N = 1000
X = toplot.x
Y = toplot.y
Z = toplot.c
# nx = 10*int(np.sqrt(N))
nx = 500
xg = np.linspace(X.min(), X.max(), nx)
yg = np.linspace(Y.min(), Y.max(), nx)
xgrid, ygrid = np.meshgrid(xg, yg)
ctr_f = griddata((X, Y), Z, (xgrid, ygrid), method='cubic')
#%%
fig = plt.figure(dpi=400)
ax = fig.add_subplot(1, 1, 1) 
zc = ax.pcolormesh(xgrid-1000,ygrid-1000,ctr_f,cmap=cmc.cm.oslo)
ax.set_aspect('equal', 'box')
# zc=ax.contourf(xgrid, ygrid, ctr_f, cmap=cmc.cm.oslo,levels = 100)

cbar = fig.colorbar(zc)#,fontsize=fs)#zc,ticks=[0,10,20,30,40,50,60,70])#proj, shrink=0.5, aspect=5)
cbar.ax.tick_params(labelsize=fs)

plt.locator_params(nbins=6)
plt.xticks(fontsize=fs,weight='bold')
plt.yticks(fontsize=fs,weight='bold')
plt.xlim(-500,500)
plt.ylim(-500,500)
# plt.savefig('RNA_2d_data.svg')
plt.savefig('RNA_2d_data.png',format='png')
plt.savefig('RNA_2d_data.svg',format='svg')

