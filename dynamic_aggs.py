import pandas as pd 

#params containing list of groupby columns and dict of agg columns and agg type 
agg_params = {
    'groupby': ['label','batch']
    ,'agg': {'profit':'sum','hours':'mean'}
}

#data being passed in for aggregation
df_in = pd.DataFrame(
    {
        'id': [1,2,3,4],
        'label': ['a','a','b','b'],
        'batch': ['foo','foo','bar','bar'],
        'profit': [3,7,160,40],
        'hours': [6,10,100,60],
    }
)

#aggregate function
def agg_data_frame(df,group,agg):
    df = df.groupby(group,as_index=False).agg(agg)

    return df

#aggregate function call
df_agg = agg_data_frame(df_in,agg_params.get('groupby'),agg_params.get('agg'))

#return aggregation
print(df_agg)