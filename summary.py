def catsum(df,columnname):
    minimum_strength = df[columnname].value_counts().min()
    maximum_strength = df[columnname].value_counts().max()
    missing_values = df[columnname].isna().sum()
    missing_values_pc =(100* missing_values/len(df.index))
    zeros = len(df[df[columnname] == 0])
    return {'min_strengh':minimum_strength,'max_strength':maximum_strength,'missing values':missing_values,'missing val %': missing_values_pc,'0s':zeros}

def numsum(df,columnname):
    if (type(df[columnname][0])==str):
        mean =-1
        minimum = -1
        maximum = -1
    else:
        mean = df[columnname].mean()
        minimum = df[columnname].min()
        maximum = df[columnname].max()
    missing_values = df[columnname].isna().sum()
    missing_values_pc =(100* missing_values/len(df.index))
    zeros = len(df[df[columnname] == 0])
    return {'mean':mean,'Min':minimum,'Max':maximum,'missing values':missing_values,'missing val %': missing_values_pc,'0s':zeros}

    for i in range(len(categorical)):
        cat_sumry.append((categorical[i],smy.catsum(df,categorical[i]),vz.cat_vis(df,categorical[i],i)))
    for j in range(len(numerical)):
        num_sumry.append((numerical[j],smy.numsum(df,numerical[j]),vz.num_vis(df,numerical[j],j)))
    return cat_sumry,num_sumry