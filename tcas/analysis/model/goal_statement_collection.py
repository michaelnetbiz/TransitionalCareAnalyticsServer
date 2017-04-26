# -*- coding: utf-8 -*-
class GoalStatementCollection(list):
    def __init__(self, df):
        """

        Parameters
        ----------
        df
        """
        super().__init__()
        self.items = df.to_dict().items()
