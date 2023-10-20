
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

df = pd.read_csv('data/data_process.csv')
samples, features = df.shape
print('Number Of Samples: ', samples) # how many rows/columns
print('Number Of Features: ', features) # how many rows/columns
print(df.head())
print(df.info())
print(df.describe().T)
print(df.tail())
d = []
u = []
t = []
for col in df:
    d.append(col)
    u.append(df[col].nunique())
    t.append(df[col].dtype)
print(pd.DataFrame({'column':d,'type': t ,'unique value' : u}))
print("_________________________________________________________")

#Preprocessing and Cleaning Data
print(df.isnull().sum())
print(df.duplicated().sum())

# labels = ['ChuaXem', 'DaXem'] # define gender
# values = df["TrangThaiXem"].value_counts().values # count TrangThaiXem
# df["TrangThaiXem"].replace({True: 'DaXem', False: 'ChuaXem'}, inplace=True)
# plt.style.use('fivethirtyeight')
# plt.figure(figsize=(12, 8))
# plt.subplot(1, 2, 1)
# plt.title('Total Status Open SMS/ Not Open SMS')
# sns.countplot(x=df["TrangThaiXem"], data=df)
# plt.subplot(1, 2, 2)
# plt.pie(values, labels=labels, autopct='%1.1f%%')

st.title('Total Status Open SMS/ Not Open SMS')
count = df['TrangThaiXem'].value_counts()
pie_col = ["Chua xem", "Da xem"]
fig = px.pie(values=count.values, names= pie_col)
st.plotly_chart(fig)


st.title('Top 10 Revenue Employee')
top10 = df.groupby("VanPhong").agg(total_Revenue=("TongTienBL", "sum")).nlargest(10, "total_Revenue").reset_index()
fig = px.bar(top10, x="total_Revenue", y = "VanPhong", color='total_Revenue')
st.plotly_chart(fig)


st.title('Top 10 Revenue Employee by Units')
top10_cb = df.groupby(['VanPhong', 'UserLayMau']).agg(total_Revenue=("TongTienBL", "sum")).nlargest(10, "total_Revenue").reset_index()
top10_cb = top10_cb.sort_values('total_Revenue', ascending=False)
fig = px.bar(top10_cb, x='UserLayMau', y = "total_Revenue", text="VanPhong", color='total_Revenue')
st.plotly_chart(fig)
fig.write_image("top10_revenue_byunits.png")

# top10_cb.to_excel("top10_cb_web.xlsx", index= False)
# wb = openpyxl.load_workbook("top10_cb_web.xlsx")
# wb.worksheets[0].title = "data"
# chart = wb[wb.sheetnames[0]]
# img = openpyxl.drawing.image.Image("top10_revenue_byunits.png")
# img.anchor = "D2"
# chart.add_image(img)
# chart.cell(row = 1, column = 4).value = "Top 10 Revenue Employee by Units" #This will change the cell(2,4) to 4
# wb.save("top10_cb_web.xlsx")


st.title('Total Status Open SMS/ Not Open SMS by Units')
daxem = df.groupby('VanPhong')['TrangThaiXem'].sum().reset_index()
chuaxem = df[df["TrangThaiXem"]==0].groupby('VanPhong')['TrangThaiXem'].count().reset_index()
fig = px.bar(daxem, x='VanPhong', y = 'TrangThaiXem')
fig1 = px.bar(chuaxem, x='VanPhong', y = 'TrangThaiXem')
st.plotly_chart(fig)
st.plotly_chart(fig1)


st.title('Total Revenue by Units')
df2 = df.groupby(['VanPhong'])['TongTienBL'].sum().reset_index().sort_index()
fig = px.bar(df2, x='VanPhong', y = "TongTienBL", color='TongTienBL')
st.plotly_chart(fig)


st.title('Total Open SMS by Units')
df4 = df.groupby('VanPhong')['TrangThaiXem'].sum().reset_index().sort_index()
fig = px.bar(df4, x='VanPhong', y = "TrangThaiXem", color='TrangThaiXem')
st.plotly_chart(fig)


st.title('Total Schedule by Units')
df3 = df.groupby(['VanPhong'])['SID'].count().reset_index().sort_index()
fig = px.bar(df3, x='VanPhong', y = "SID", color='SID')
st.plotly_chart(fig)

#define categories cilumns
categorical_columns = ['TrangThaiXem', 'TuVan', 'TrangThaiGui', 'TrangThaiSMSKQ']
fig, axes = plt.subplots(4,2, figsize=(20,30))
idx = 0
for col in categorical_columns:
    fig = px.bar(df, x=col, y = col)
    st.plotly_chart(fig)
   
    
