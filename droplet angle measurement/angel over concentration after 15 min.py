
import math as mt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lmfit import models
from scipy.stats import chi2

#0	15	29.4	0.01



triton_cons = [ 0.5, 1, 3, 5]
triton_hoek = [ 9.8, 8.2, 8.5, 7.1]
triton_error = [ 0.97,	0.86, 0.26, 0.14]

SDS_cons = [ 0.05, 0.1, 0.5, 1, 3, 5, 7]
SDS_hoek = [ 31.1, 21.1, 18.8, 20.3, 9.3, 7.8, 7.7]
SDS_error =[ 0.04, 0.07, 0.04, 0.01, 0.63, 1.25, 1.11]

DOSS_cons = [ 0.5, 1, 3, 5]
DOSS_hoek = [ 22.8, 14.9, 9.7, 14.2]
DOSS_error = [ 0.02, 0.09, 1.51, 0.05]

CPC_cons = [ 1, 3, 5]
CPC_hoek = [ 34.8, 33.5, 33.6]
CPC_error = [ 0.12, 0.08, 0.41]





plt.errorbar(triton_cons, triton_hoek, yerr=triton_error, label = "triton", fmt='o')
plt.errorbar(SDS_cons, SDS_hoek, yerr=SDS_error, label = 'SDS', fmt='o')
plt.errorbar(DOSS_cons, DOSS_hoek, yerr=DOSS_error, label = 'DOSS', fmt='o')
plt.errorbar(CPC_cons, CPC_hoek, yerr=CPC_error, label = 'CPC', fmt='o')
plt.errorbar(0, 29.4, yerr=0.01, label='0%', fmt='o')

plt.xlim(-0.5,8)
plt.ylim(0,40)
plt.xlabel('concentration in %')
plt.ylabel('angle measurement')

plt.legend()
plt.title('measurement after 15 minutes')


plt.savefig('angel over concentration') 