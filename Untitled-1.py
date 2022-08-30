# %%
accident_df = pd.read_csv("US_Accidents_Dec20_updated.csv")

# %%
accident_df.describe()
 

# %%
accident_df.shape

# %%
accident_df.info()

# %%
accidents= accident_df[['ID','Severity','Start_Time','City','State']]


# %%
accidents.isnull().sum()

# %%
sortedByTime= accidents.sort_values(by=["Start_Time"])
print(sortedByTime)

# %%
sortedByTime.describe(include='all')

# %%
frequancy= sortedByTime['Start_Time'].value_counts()
print(frequancy)

# %%
accident_df_2= pd.DataFrame(frequancy)

# %%
plot= frequancy.reset_index()
print(plot)


# %%
accident_df_3= accident_df_2.reset_index()

# %%

accident_df_3 = accident_df_3.rename(columns={"index":"date_time", "Start_Time": "counts"})
print(accident_df_3)


# %%
accident_df_3[accident_df_3['date_time']=='False'].count()

# %%
accident_df_3 = accident_df_3[accident_df_3['date_time']!='False']

# %%

accident_df_3['Months'] =pd.to_datetime(accident_df_3['date_time']).dt.month
accident_df_3['Minute'] =pd.to_datetime (accident_df_3['date_time']).dt.minute
accident_df_3['Hours'] = pd.to_datetime(accident_df_3['date_time']).dt.hour
accident_df_3['Year'] = pd.to_datetime(accident_df_3['date_time']).dt.year
accident_df_3['Day'] =pd.to_datetime(accident_df_3['date_time']).dt.day

# %%
accident_df_4= accident_df_3[['Year','Months','Day','Hours','Minute']]
print(accident_df_4)

# %%
accident_df_4.describe(include='all')

# %%


plt.hist(accident_df_4.loc[accident_df_3['counts']]['Hours'])


# %% [markdown]
# Aylara Göre

# %%

accidents[accidents['Severity']=='2']

# %%
accident_df_4["Hours"].value_counts().plot.barh()

# %%
accident_df_5= accidents["City"].isin(["Los Angeles"])
accidents[accident_df_5]

# %%
accident_df_6= pd.DataFrame(accidents[accident_df_5])

accident_df_6

# %%
accident_df_7= accident_df_6.reset_index()

accident_df_7

# %%
accident_df_8= accident_df_7.rename(columns={"index":"date_time", "Start_Time": "counts"})
print(accident_df_8)

# %%
accident_df_8['Months'] =pd.to_datetime(accident_df_8['counts']).dt.month
accident_df_8['Minute'] =pd.to_datetime (accident_df_8['counts']).dt.minute
accident_df_8['Hours'] = pd.to_datetime(accident_df_8['counts']).dt.hour
accident_df_8['Year'] = pd.to_datetime(accident_df_8['counts']).dt.year
accident_df_8['Day'] =pd.to_datetime(accident_df_8['counts']).dt.day

# %%
accident_df_9= accident_df_8[['Year','Months','Day','Hours','Minute']]
print(accident_df_9)

# %%
sure= [str(i).split('Huors')[-1].strip() for i in accident_df_9.Hours]
accident_df_9['Hours']= sure
plt.show()

# %%
fig, ax = plt.subplots(figsize = (12,6), dpi = 80)

sns.distplot(accident_df_9.Hours, bins=24, kde=False, norm_hist=True)


# %%
accident_df_9['Hours'].value_counts().plot.barh().set_title("saatler")

# %%
p= sns.countplot(accident_df_9.Hours)
p.set_xticklabels([x for x in range(0,25)])




# %%
accident_df_9[accident_df_9['Hours'].str.contains('<')]

# %%
b = [0,4,8,12,16,20,24]
l = ['Late_Night', 'Early_Morning','Morning','Noon','Eve','Night']
accident_df_9['Araliklar'] = pd.cut(accident_df_9['Hours'].astype(int), bins=b, labels=l, include_lowest=True)



# accidents_df_9['aralık_bır']= accident_df_9['Hours'].map(lambda x: x<3,accident_df_9['Hours'])
# accidents_df_9['aralık_ıkı']= (accident_df_9['Hours'].map(lambda x:2<x<6,Hours))
# accidents_df_9['aralık_uc']= (accident_df_9['Hours'].map(lambda x:5<x<9,Hours))
# accidents_df_9['aralık_dort']= (accident_df_9['Hours'].map(lambda x:8<x<12, Hours))
# accidents_df_9['aralık_bes']= (accident_df_9['Hours'].map(lambda x:11<X<15,Hours))
# accidents_df_9['aralık_altı']= (accident_df_9['Hours'].map(lambda x:14<X<18,Hours))
# accidents_df_9['aralık_yedı']= (accident_df_9['Hours'].map(lambda x:17<X<21,Hours))
# accidents_df_9['aralık_sekız']= (accident_df_9['Hours'].map(lambda x:20<X<24,Hours))

print(accident_df_9)

# %%
p1= sns.countplot(accident_df_9.Araliklar)
p1.set_xticklabels([x for x in l])

# %%
def getDayNumber(year, month, day):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dayNumber = calendar.weekday(year, month, day)
    return (weekdays[dayNumber])



accident_df_9['weekday']= accident_df_9.apply(lambda x: getDayNumber(x['Year'], x['Months'], x['Day']), axis=1)

accident_df_9


# %%
accident_df_9["weekday"].value_counts()

# %%
day = accident_df_9.groupby("weekday")["weekday"].count()
day

# %%
p2= sns.countplot(accident_df_9.weekday)
p2.set_xticklabels([x for x in weekdays])

# %%
df8= accident_df_9.groupby(['weekday','Hours'])
table = pd.pivot_table(accident_df_9,index=['weekday','Hours'])
table
#table.plot(kind='bar')

# %%
late_date=  pd.DataFrame(accident_df_9['weekday'].loc[accident_df_9['Araliklar']=='Late_Night'].groupby(accident_df_9['weekday']).count())
early_date= pd.DataFrame(accident_df_9['weekday'].loc[accident_df_9['Araliklar']=='Early_Morning'].groupby(accident_df_9['weekday']).count())
morning= pd.DataFrame(accident_df_9['weekday'].loc[accident_df_9['Araliklar']=='Morning'].groupby(accident_df_9['weekday']).count())
noon_date= pd.DataFrame(accident_df_9['weekday'].loc[accident_df_9['Araliklar']=='Noon'].groupby(accident_df_9['weekday']).count())
eve_date= pd.DataFrame(accident_df_9['weekday'].loc[accident_df_9['Araliklar']=='Eve'].groupby(accident_df_9['weekday']).count())
night_date= pd.DataFrame(accident_df_9['weekday'].loc[accident_df_9['Araliklar']=='Night'].groupby(accident_df_9['weekday']).count())
late_date

# %%
late_date_1= pd.DataFrame({'gunler': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
               'Toplam_kaza':              [late_date['weekday'].loc[late_date.index=='Monday'].sum(), 
                                            late_date['weekday'].loc[late_date.index=='Tuesday'].sum(),      
                                            late_date['weekday'].loc[late_date.index=='Wednesday'].sum(), 
                                            late_date['weekday'].loc[late_date.index=='Thursday'].sum(), 
                                            late_date['weekday'].loc[late_date.index=='Friday'].sum(),
                                            late_date['weekday'].loc[late_date.index=='Saturday'].sum(), 
                                            late_date['weekday'].loc[late_date.index=='Sunday'].sum()]})

late_date_1

# %%
cevirilmis_r=list(late_date_1.gunler)
cevirilmis_p= list(late_date_1.Toplam_kaza)
fig = plt.figure(figsize = (10, 5))
plt.bar(cevirilmis_r, cevirilmis_p, color ='maroon',
        width = 0.4)
 
plt.show()

# %%
early_date_1= pd.DataFrame({'gunler': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 
               'Toplam_kaza':              [early_date['weekday'].loc[early_date.index=='Monday'].sum(), 
                                            early_date['weekday'].loc[early_date.index=='Tuesday'].sum(),      
                                            early_date['weekday'].loc[early_date.index=='Wednesday'].sum(), 
                                            early_date['weekday'].loc[early_date.index=='Thursday'].sum(), 
                                            early_date['weekday'].loc[early_date.index=='Friday'].sum(),
                                            early_date['weekday'].loc[early_date.index=='Saturday'].sum(), 
                                            early_date['weekday'].loc[early_date.index=='Sunday'].sum()]})
early_date_1


# %%
cevirilmis_x=list(early_date_1.gunler)
cevirilmis_y= list(early_date_1.Toplam_kaza)
fig = plt.figure(figsize = (10, 5))
plt.bar(cevirilmis_x, cevirilmis_y, color ='maroon',
        width = 0.4)
 
plt.show()

# %%
morning_1= pd.DataFrame({'gunler': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 
               'Toplma_kaza':              [morning['weekday'].loc[morning.index=='Monday'].sum(), 
                                            morning['weekday'].loc[morning.index=='Tuesday'].sum(),      
                                            morning['weekday'].loc[morning.index=='Wednesday'].sum(), 
                                            morning['weekday'].loc[morning.index=='Thursday'].sum(), 
                                            morning['weekday'].loc[morning.index=='Friday'].sum(),
                                            morning['weekday'].loc[morning.index=='Saturday'].sum(), 
                                            morning['weekday'].loc[morning.index=='Sunday'].sum()]})
morning_1


# %%
cevirilmis_e=list(morning_1.gunler)
cevirilmis_f= list(morning_1.Toplma_kaza)
fig = plt.figure(figsize = (10, 5))
plt.bar(cevirilmis_e, cevirilmis_f, color ='black',
        width = 0.4)
 
plt.show()

# %%
noon_date_1= pd.DataFrame({'gunler': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 
               'Toplam_kaza':          [noon_date['weekday'].loc[noon_date.index=='Monday'].sum(), 
                                            noon_date['weekday'].loc[noon_date.index=='Tuesday'].sum(),      
                                            noon_date['weekday'].loc[noon_date.index=='Wednesday'].sum(), 
                                            noon_date['weekday'].loc[noon_date.index=='Thursday'].sum(), 
                                            noon_date['weekday'].loc[noon_date.index=='Friday'].sum(),
                                            noon_date['weekday'].loc[noon_date.index=='Saturday'].sum(), 
                                            noon_date['weekday'].loc[noon_date.index=='Sunday'].sum()]})
noon_date_1



# %%
cevirilmis_c=list(noon_date_1.gunler)
cevirilmis_d= list(noon_date_1.Toplam_kaza)
fig = plt.figure(figsize = (10, 5))
plt.bar(cevirilmis_c, cevirilmis_d, color ='yellow',
        width = 0.4)
 
plt.show()

# %%
eve_date_1= pd.DataFrame({'gunler': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 
               'Toplam_kaza':              [eve_date['weekday'].loc[eve_date.index=='Monday'].sum(), 
                                            eve_date['weekday'].loc[eve_date.index=='Tuesday'].sum(),      
                                            eve_date['weekday'].loc[eve_date.index=='Wednesday'].sum(), 
                                            eve_date['weekday'].loc[eve_date.index=='Thursday'].sum(), 
                                            eve_date['weekday'].loc[eve_date.index=='Friday'].sum(),
                                            eve_date['weekday'].loc[eve_date.index=='Saturday'].sum(), 
                                            eve_date['weekday'].loc[eve_date.index=='Sunday'].sum()]})
eve_date_1


# %%
cevirilmis_a=list(eve_date_1.gunler)
cevirilmis_b= list(eve_date_1.Toplam_kaza)
fig = plt.figure(figsize = (10, 5))
plt.bar(cevirilmis_a, cevirilmis_b, color ='blue',
        width = 0.4)
 
plt.show()

# %%
night_date_1= pd.DataFrame({'gunler': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 
                'Toplam_kaza':             [night_date['weekday'].loc[late_date.index=='Monday'].sum(), 
                                            night_date['weekday'].loc[late_date.index=='Tuesday'].sum(),      
                                           night_date['weekday'].loc[late_date.index=='Wednesday'].sum(), 
                                            night_date['weekday'].loc[late_date.index=='Thursday'].sum(), 
                                            night_date['weekday'].loc[late_date.index=='Friday'].sum(),
                                            night_date['weekday'].loc[late_date.index=='Saturday'].sum(), 
                                            night_date['weekday'].loc[late_date.index=='Sunday'].sum()]})
night_date_1

# %%
cevirilmis_1=list(night_date_1.gunler)
cevirilmis_2= list(night_date_1.Toplam_kaza)
fig = plt.figure(figsize = (10, 5))
plt.bar(cevirilmis_1, cevirilmis_2, color ='red',
        width = 0.4)
 
plt.show()

# %%
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import calendar 



