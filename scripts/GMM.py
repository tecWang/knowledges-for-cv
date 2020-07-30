import itertools

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn import mixture

color_iter = itertools.cycle(['navy', 'c', 'cornflowerblue', 'gold','darkorange'])

def plot_results(X, Y_, means, covariances, index, title):
    splot = plt.subplot(2, 2, 1 + index)
    for i, (mean, covar, color) in enumerate(zip(means, covariances, color_iter)):
        v, w = linalg.eigh(covar)
        v = 2. * np.sqrt(2.) * np.sqrt(v)
        u = w[0] / linalg.norm(w[0])
        # as the DP will not use every component it has access to
        # unless it needs it, we shouldn't plot the redundant
        # components.
        if not np.any(Y_ == i):
            continue
        plt.scatter(X[Y_ == i, 0], X[Y_ == i, 1], .8, color=color)

        # Plot an ellipse to show the Gaussian component
        angle = np.arctan(u[1] / u[0])
        angle = 180. * angle / np.pi  # convert to degrees
        ell = mpl.patches.Ellipse(mean, v[0], v[1], 180. + angle, color=color)
        ell.set_clip_box(splot.bbox)
        ell.set_alpha(0.5)
        splot.add_artist(ell)

    plt.xlim(-9., 5.)
    plt.ylim(-3., 6.)
    plt.xticks(())
    plt.yticks(())
    plt.title(title)

# Number of samples per component
n_samples = 1000

# Generate random sample, two components
np.random.seed(0)

x1 = np.random.normal(0, 1, (n_samples, 2))  # 创建符合正态分布(0, 1)的数据
x2 = np.random.normal(-1, 1, (n_samples, 2))  # 创建符合正态分布(0, 1)的数据
X = np.vstack((x1, x2))
np.random.shuffle(X)
print(X.shape)

'''
String describing the type of covariance parameters to use. Must be one of:
‘full’: each component has its own general covariance matrix
‘tied’: all components share the same general covariance matrix
‘diag’: each component has its own diagonal covariance matrix
‘spherical’: each component has its own single variance

The covariance of each mixture component. The shape depends on covariance_type:
(n_components, n_features, n_features) if 'full'
(n_features, n_features)               if 'tied',
(n_components, n_features)             if 'diag',
(n_components,)                        if 'spherical',

# variance and covariance

'''

# 预览iris数据结构
# from sklearn import datasets
# from sklearn.model_selection import StratifiedKFold
# skf = StratifiedKFold(n_splits=4)
# iris = datasets.load_iris()
# train_index, test_index = next(iter(skf.split(iris.data, iris.target)))
# X_train = iris.data[train_index]
# print(X_train.shape)

# 指定成分为5的话，GM会直接划归为5类，BGM会自适应的删掉一些成分
gmm = mixture.GaussianMixture(n_components=5, covariance_type='full').fit(X)
print(gmm.means_)
print(gmm.covariances_)
plot_results(X, gmm.predict(X), gmm.means_, gmm.covariances_, 0,'Gaussian Mixture')

dpgmm = mixture.BayesianGaussianMixture(n_components=5, covariance_type='full').fit(X)
plot_results(X, dpgmm.predict(X), dpgmm.means_, dpgmm.covariances_, 1, 'Bayesian Gaussian Mixture')

gmm = mixture.GaussianMixture(n_components=2, covariance_type='full').fit(X)
plot_results(X, gmm.predict(X), gmm.means_, gmm.covariances_, 2,'Gaussian Mixture')

dpgmm = mixture.BayesianGaussianMixture(n_components=2, covariance_type='full').fit(X)
plot_results(X, dpgmm.predict(X), dpgmm.means_, dpgmm.covariances_, 3, 'Bayesian Gaussian Mixture')

plt.show()