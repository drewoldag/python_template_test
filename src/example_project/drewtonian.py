"""The primary definition of the Drewtonian"""

def primary(alpha:int, beta:int = 5) -> int:
    """Implementation of the Drewtonian.
    This should only be considered accurate to first approximations.

    Subsequent implementations will be more accurate.


    Parameters
    ----------
    alpha : int
        The `alpha` parameter
    beta : int, optional
        The `beta` parameter, by default 5

    Returns
    -------
    int
        The Drewtonian for inputs `alpha` and `beta`
    """
    return alpha * beta
