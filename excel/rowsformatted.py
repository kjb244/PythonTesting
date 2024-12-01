from pandas import Timestamp


class RowsFormatted:
    col1: str
    col2: str
    col3: str

    def __init__(self, col1: str, col2: str, col3: Timestamp):
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"RowsFormatted(col1='{self.col1}', col2={self.col2}, col3={self.col3})"

