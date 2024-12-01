import pandas as pd

header_df = pd.DataFrame({
    'uid': [1, 2],
    'vendor': ['macys', 'jcpenny'],
    'amt': [23, 34],
})

line_df = pd.DataFrame({
    'date': ['10/23/24', '01/01/17', '01/01/17', '04/25/1980'],
    'proj': ['34d', '23r', '23y', '56y'],
    'series_id': [2, 3, 4, 23],
    'id': [1, 1, 1, 2]
})

merged_df = pd.merge(header_df, line_df[['proj', 'series_id', 'id', 'date']], how='left', left_on='uid',
                     right_on='id').drop(columns=['id'])
print(merged_df)
print('')

pivot_df = pd.pivot_table(merged_df, index=['vendor', 'amt'], values=['proj', 'series_id', 'date'], aggfunc=list)
print(pivot_df)
print('')


# output we want is vendor, amt, meta (json string of array of date, proj, series_id)
def calculate_meta(row):
    arr = []
    columns = ['date', 'proj', 'series_id']
    for i in range(len(row['date'])):
        meta = {}
        for c in columns:
            meta.update({c: row[c][i]})
        arr.append(meta)
    return arr


pivot_df['meta'] = pivot_df.apply(calculate_meta, axis=1)
print(pivot_df)

vendors = merged_df['vendor'].unique()
for vend in vendors:
    vendor_df = merged_df.loc[merged_df['vendor'] == vend]
    grouped_df = vendor_df.groupby('date')
    print(vend)
    for x in list(grouped_df.groups):
        print(grouped_df.get_group(x))
