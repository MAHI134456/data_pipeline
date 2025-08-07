import pymc as pm
import numpy as np
import arviz as az

def build_change_point_model(returns):
    """
    Build a simple change point model for the log returns.
    
    Parameters:
        returns (np.array): Array of log return values.
        
    Returns:
        model: PyMC model object.
    """
    n = len(returns)
    
    with pm.Model() as model:
        # Prior for the change point location
        tau = pm.DiscreteUniform('tau', lower=0, upper=n - 1)

        # Priors for the means before and after change
        mu_1 = pm.Normal('mu_1', mu=0, sigma=1)
        mu_2 = pm.Normal('mu_2', mu=0, sigma=1)

        # Shared standard deviation
        sigma = pm.Exponential('sigma', lam=1.0)

        # Use switch based on tau
        mu = pm.math.switch(np.arange(n) < tau, mu_1, mu_2)

        # Likelihood
        obs = pm.Normal('obs', mu=mu, sigma=sigma, observed=returns)

    return model
