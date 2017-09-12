from numpy import mat, asarray, mean, size, shape, hstack, ones, ceil, \
    zeros, arange
from numpy.linalg import inv, lstsq


def olsnw(y, X, constant=True, lags=None):
    # Estimation of a linear regression with Newey-West covariance
    #   Parameters
    # ----------
    # y : array_like
    #     The dependent variable (regressand).  1-dimensional with T elements.
    # X : array_like
    #     The independent variables (regressors). 2-dimensional with sizes T
    #     and K.  Should not include a constant.
    # constant: bool, optional
    #     If true (default) includes model includes a constant.
    # lags: int or None, optional
    #     If None, the number of lags is set to 1.2*T**(1/3), otherwise the
    #     number of lags used in the covariance estimation is set to the value
    #     provided.
    # Returns
    # -------
    # b : ndarray, shape (K,) or (K+1,)
    #     Parameter estimates.  If constant=True, the first value is the
    #     intercept.
    # vcv : ndarray, shape (K,K) or (K+1,K+1)
    #     Asymptotic covariance matrix of estimated parameters
    # s2 : float
    #     Asymptotic variance of residuals, computed using Newey-West variance
    #     estimator.
    # R2 : float
    #     Model R-square
    # R2bar : float
    #     Adjusted R-square
    # e : ndarray, shape (T,)
    #     Array containing the model errors
    # Notes
    # -----
    # The Newey-West covariance estimator applies a Bartlett kernel to estimate
    # the long-run covariance of the scores.  Setting lags=0 produces White’s
    # Heteroskedasticity Robust covariance matrix.
    # See also
    # --------
    # np.linalg.lstsq
    # Example
    # -------
    # >>> X = randn(1000,3)
    # >>> y = randn(1000)
    # >>> b,vcv,s2,R2,R2bar = olsnw(y, X)
    # Exclude constant:
    # 224 Custom Function and Modules
    #   >>> b,vcv,s2,R2,R2bar = olsnw(y, X, False)
    # Specify number of lags to use:
    # >>> b,vcv,s2,R2,R2bar = olsnw(y, X, lags = 4)
    T = y.size
    if size(X, 0) != T:
        X = X.T
    T, K = shape(X)
    if constant:
        X = copy(X)
        X = hstack((ones((T, 1)), X))
        K = size(X, 1)
    if lags is None:
        lags = int(ceil(1.2 * float(T)**(1.0 / 3)))
    # Parameter estimates and errors
    out = lstsq(X, y)
    b = out[0]
    e = y - X@b
    # Covariance of errors
    gamma = zeros((lags + 1))
    for lag in range(lags + 1):
        gamma[lag] = (e[:T - lag] @ e[lag:]) / T
    w = 1 - arange(0, lags + 1) / (lags + 1)
    w[0] = 0.5
    s2 = gamma @ (2 * w)
    # Covariance of parameters
    Xe = mat(zeros(shape(X)))
    for i in range(T):
        Xe[i] = X[i] * float(e[i])
    Gamma = zeros((lags + 1, K, K))
    for lag in range(lags + 1):
        Gamma[lag] = Xe[lag:].T * Xe[:T - lag]
    Gamma = Gamma / T
    S = Gamma[0].copy()

    for i in range(1, lags + 1):
        S = S + w[i] * (Gamma[i] + Gamma[i].T)
    XpX = (X.T @ X) / T
    XpXi = inv(XpX)
    vcv = mat(XpXi) * S * mat(XpXi) / T
    vcv = asarray(vcv)
    # R2, centered or uncentered
    if constant:
        R2 = (e @ e) / (y - mean(y) @ y - mean(y))
    else:
        R2 = (e @ e) / (y @ y)
    R2bar = 1 - R2 * (T - 1) / (T - K)
    R2 = 1 - R2
    return b, vcv, s2, R2, R2bar, e
