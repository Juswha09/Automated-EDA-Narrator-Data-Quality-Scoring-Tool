# Base class + inheritance + polymorphism
import pandas as pd
import numpy as np

class EDAAnalyzer:
    """
    Base class for exploratory data analysis.

    Attributes:
        _df (pd.DataFrame): DataFrame to analyze.
        results (dict): Stores analysis results.
    """

    def __init__(self, df):
        """
        Initialize EDAAnalyzer with a DataFrame.

        Args:
            df (pd.DataFrame): Input DataFrame.
        """
        self._df = df
        self.results = {}

    def run_all(self):
        """
        Run basic analysis.

        Returns:
            dict: Summary statistics.
        """
        return {"summary": self._df.describe().to_dict()}


class NumericAnalyzer(EDAAnalyzer):
    """
    Performs EDA specifically on numeric columns.
    """

    def run_all(self):
        """
        Generate summary statistics for numeric columns.

        Returns:
            dict: Numeric summary statistics.
        """
        import numpy as np
        num = self._df.select_dtypes(include=[np.number])
        self.results['summary'] = num.describe().to_dict()
        return self.results


class CategoricalAnalyzer(EDAAnalyzer):
    """
    Performs EDA specifically on categorical columns.
    """

    def run_all(self):
        """
        Generate summary statistics for categorical columns.

        Returns:
            dict: Categorical summary statistics.
        """
        cat = self._df.select_dtypes(include=['object'])
        self.results['summary'] = cat.describe(include='all').to_dict()
        return self.results

