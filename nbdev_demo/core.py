# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['mass_error_ppm']

# %% ../00_core.ipynb 3
def mass_error_ppm(theor: float, obsvd: float):
    """Calculate relative mass error."""
    return round(1e6*(obsvd/theor - 1), 2)
