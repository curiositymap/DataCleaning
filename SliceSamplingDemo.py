###########################
### Slice Sampling Demo ###
###########################

# Slice sampling applied to Standard Normal, the special case of Gaussian distribution

import numpy as np
import scipy.stats as st
import seaborn as sns
import matplotlib.pyplot as plt


sns.set()
mu = 65 # mu in Gaussian is used to shift the center of the distribution
sigma = 32


# Define the target distribution P(x).
# In this demo, P(x) is set to be unimodal.
# The key to implement Slice Sampling is to get the inverse function of the PDF.


def p(x):
    return st.norm.pdf(x, loc=mu, scale=sigma)


def p_inv(y):
    x = np.sqrt(-2*sigma**2 * np.log(y * sigma * np.sqrt(2*np.pi)))
    return mu-x, mu+x


def slice_sampling(iter=1000):
    samples = np.zeros(iter)
    x = 0

    for i in range(iter):
        u = np.random.uniform(0, p(x))
        x_lo, x_hi = p_inv(u)
        x = np.random.uniform(x_lo, x_hi)
        samples[i] = x

    return samples


if __name__ == '__main__':
    samples = slice_sampling(iter=10000)
    sns.distplot(samples, kde=False, norm_hist=True)
    x = np.arange(-100, 250)
    plt.plot(x, p(x))
    plt.show()



# Source: https://wiseodd.github.io/techblog/2015/10/24/slice-sampling/)
