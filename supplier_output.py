import datetime
from felfel_ix.ix.cronscripts import Regression
import pprint

forecast_date = datetime.datetime(2017, 9, 1)
re = Regression(forecast_date)
df = re.observations.reset_index()

df['productname'] = df.productid.map(re.products.productname)
df['suppliername'] = df.productid.map(re.products.suppliername)
df['productname'] = df.productname.str.replace('"', '')
df['productname'] = df.productname.str.replace("'", '')
# Encode strings differently
df['foodcategoryname'] = df.foodcategoryname.str.encode('latin-1')
df['suppliername'] = df.suppliername.str.encode('latin-1')
df['productname'] = df.productname.str.encode('latin-1')
df['productname'] = df.productname.astype(str)

supp = (df.groupby(['locationid',
                    df.date.dt.week,
                    'suppliername',
                    'foodcategoryname',
                    'productname'])
          .sold
          .sum()
          .groupby(level=[2,
                          3,
                          4])
          .mean())
supp
# Remove quotes in product names

output = {"name": "Suppliers", "children": []}
for supplier in list(supp.index.get_level_values(0).unique()):
    output['children'].append({"name": supplier, "children": []})

for supplier in list(supp.index.get_level_values(0).unique()):
    index = next(index for (index, d) in enumerate(output['children']) if d["name"] == supplier)
    for foodcategory in list(supp.index.get_level_values(1).unique()):
        output['children'][index]['children'].append({"name": foodcategory, "children": []})

for supplier in list(supp.index.get_level_values(0).unique()):
    index1 = next(index for (index, d) in enumerate(output['children']) if d["name"] == supplier)
    for foodcategory in list(supp.index.get_level_values(1).unique()):
        index2 = next(index for (index, d) in enumerate(output['children'][index]['children']) if d["name"] == foodcategory)
        try:
            for i in supp.loc[supplier, foodcategory].iteritems():
                output['children'][index1]['children'][index2]['children'].append({"name": i[0], "size": i[1]})
        except:
            pass


pprint.pprint(output)