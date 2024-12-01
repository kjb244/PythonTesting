from typing import TypeVar, Union, List

import pandas as pd

from excel.rowsformatted import RowsFormatted

df = pd.read_excel('test.xlsx', header=0)


def format_rows(df_inner) -> List[RowsFormatted]:
    arr = []
    for index, row in df_inner.iterrows():
        row = RowsFormatted(*row.values)
        arr.append(row)

    return arr


arr = format_rows(df)

print(arr[1])

