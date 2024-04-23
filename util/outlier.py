import pandas as pd
import numpy as np
from scipy.stats import iqr

def get_outlier_fence(data_column):
    """Returns outlier threshold values

    Args:
        data_column: dataframe column to be observed

    Returns:
        low_threshold, up_threshold: lower and upper threshold values
    """
    iqr = iqr(data_column)
    low_threshold = np.quantile(data_column, 0.25) - 1.5 * iqr
    up_threshold = np.quantile(data_column, 0.75) + 1.5 * iqr
    return low_threshold, up_threshold

