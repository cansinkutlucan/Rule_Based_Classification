import pandas as pd
persona = pd.read_csv('persona.csv')

#Question 1: How many unique SOURCE are there? What are their frequencies?
print("Unique SOURCE", persona["SOURCE"].nunique())
print("Frequencies of SOURCE:", persona['SOURCE'].value_counts())
#Question 2:How many unique PRICEs are there?
print("Unique PRICE", persona["PRICE"].nunique())
#Question 3: How many sales were made from which PRICE?
print("Frequencies of PRICE", persona['PRICE'].value_counts())
#Question 4: How many sales were made from which country
print("Frequencies of COUNTRY", persona['COUNTRY'].value_counts())
#Question 5: How much was earned from sales by country?
print("Winnings by COUNTRY:", persona.groupby("COUNTRY")[['PRICE']].aggregate("sum"))
#Question 6: What are the sales numbers by SOURCE types
print("Amount of sales by SOURCE", persona['SOURCE'].value_counts())
#Question 7: What are the PRICE averages by country?
print(("Mean PRICE by COUNTRY", persona.groupby('COUNTRY')[["PRICE"]].aggregate("mean")))
#Question 8: What are the PRICE averages according to SOURCEs
print(("Mean PRICE by SOURCE", persona.groupby('SOURCE')[["PRICE"]].aggregate("mean")))
#Question 9: What are the PRICE averages in the COUNTRY-SOURCE breakdown?
print(("Mean PRICE by COUNTRY and SOURCE", persona.groupby(['COUNTRY', 'SOURCE'])[["PRICE"]].aggregate("mean").unstack()))

print(("Mean PRICE by COUNTRY", persona.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE'])[["PRICE"]].aggregate("mean").head()))

agg_df = persona.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE'])[["PRICE"]].aggregate("mean")
agg_df= agg_df.sort_values('PRICE', ascending=False)
agg_df = agg_df.reset_index()

bins = [0, 18, 23, 30, 40, 70]
lab = ["0_18", "19_23", "24_30", "31_40", "41_70"]
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins, labels=lab)
agg_df.head()

agg_df["customer_level_based"] = [val[0] +"_" + val[1] +"_"+ val[2] + "_" +val[5] for val in agg_df.values]
agg_df = agg_df[["customer_level_based", "PRICE"]]

agg_df = agg_df.groupby("customer_level_based").agg({"PRICE": "mean"})
agg_df = agg_df.reset_index()

agg_df["SEGMENT"] = pd.qcut(agg_df['PRICE'],4,labels=['D','C','B','A'])
agg_df

new_user = 'tur_android_female_19_23'
agg_df[agg_df['customer_level_based'] == new_user]
