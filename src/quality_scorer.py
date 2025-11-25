# Encapsulation + methods
import numpy as np

class QualityScorer:
    def __init__(self, eda_results, df_len):
        self._eda = eda_results       # protected
        self._df_len = df_len
        self.scores = {}

    def missing_score(self):
        missing = self._eda.get('missing', {})
        pct = [v['pct'] for v in missing.values()] if missing else [0]
        self.scores['missing'] = max(0, 100 - np.mean(pct))
        return self.scores['missing']

    def duplicate_score(self):
        dups = self._eda.get('duplicates', 0)
        pct = (dups / max(1, self._df_len)) * 100
        self.scores['duplicates'] = max(0, 100 - pct*2)
        return self.scores['duplicates']

    def outlier_score(self):
        out = self._eda.get('outliers', {})
        total = sum(out.values()) if out else 0
        pct = (total / max(1, self._df_len))*100
        self.scores['outliers'] = max(0, 100 - pct*1.5)
        return self.scores['outliers']

    def balance_score(self):
        self.scores['balance'] = 90.0
        return self.scores['balance']

    def overall_score(self):
        # calculate overall using weights
        for metric in ['missing', 'duplicates', 'outliers', 'balance']:
            if metric not in self.scores:
                getattr(self, f"{metric}_score")()
        weights = {'missing':0.35, 'duplicates':0.15, 'outliers':0.25, 'balance':0.25}
        self.scores['overall'] = sum(self.scores[m]*w for m,w in weights.items())
        return self.scores['overall']
