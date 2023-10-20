import pyodbc 
import pandas as pd
import numpy as np
from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import time
import sys
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.0.0.50;PORT=8080;DATABASE=BV41;UID=hmas41;PWD=123456')
#cnxn1 = pyodbc.connect('DRIVER={SQL Server};SERVER=10.0.0.36;PORT=8080;DATABASE=LABCONN;UID=Hienbuf;PWD=Hien@123')
pd.options.display.max_columns = 100
pd.options.display.max_rows = 50
plt.style.use('seaborn-whitegrid')
sns.set_color_codes('bright')

cursor = cnxn.cursor()
#cursor1 = cnxn1.cursor()
# sql = 'SELECT \
#   a.ProcessLocationID, \
#   a.LocationID, \
#   b.ProcessLocationName \
#   FROM Process_Locations a \
#   INNER JOIN ProcessLocation b \
#   ON a.ProcessLocationID = b.ProcessLocationID \
#   GROUP BY a.ProcessLocationID, a.LocationID, b.ProcessLocationName \
#   ORDER BY a.ProcessLocationID DESC'

# cursor.execute(sql)
#cursor.execute("exec Process_HomePage_LichHen('KVPST')")
#cursor.execute("{call Process_HomePage_LichHen('KVPST')}")
sql = """\
SET NOCOUNT ON;
DECLARE @RC varchar(200);
EXEC @RC = [BV41].[dbo].[Process_LichHen_ThongKe_All_New] ?, ?, ?, ?, ?;
SELECT @RC AS rc;
"""
values = ('2023-09-24 00:00:00','2023-09-24 23:59:59','TPT;VN_TH_TLI;VN_HBT_VTU;VN_LB_TBA;VN_DA_VHA;VN_TT_TTR;VN_HM_DKI;VN_GL_TQU;VN_DD_TQU;VN_TH_XLA;VN_SS_PLI;VN_BTL_MKH;VN_TX_TDI;KTNHCM;VN_HDU_AKH;VN_TTI_THI;VN_HM_DCO;VN_CG_NDO;VN_NTL_MDI;BNTN;VN_BTL_CNH2;VN_HK_CDU;VN_PX_PTI;VN_QO_PHU;VN_HM_TPH;VN_GL_DTO;VN_HDU_AKH;VN_TX_TDI;VN_CM_CSO;VN_TT_THI;VN_UH_VDI;KVPST;KVPPT;VN_BTL_CNH;VN_BD_NKA;VN_DP_TLA;VN_GL_PTH;VN_CM_CSO;VN_TO_KBA;VN_DA_KCH;VN_CG_THO;VN_HDU_AKH;VN_NTL_DMO;VN_HD_PLA;VN_GL_DXU;VN_CM_XMA;VN_MD_DNG;VN_ML_DTH;VN_HBT_DTA;VN_TTI_PGA;VN_LB_DGI;VN_DP_PHU;VN_DA_UNO', '', '')
cursor.execute(sql, values)
myresult = cursor.fetchall()
df = pd.DataFrame.from_records(myresult)
cnxn.close();
 
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


labels = ['Chưa xem', 'Đã xem'] # define gender
values = df[38].value_counts().values # count gender
df[38].replace({True: 'Đã xem', False: 'Chưa xem'}, inplace=True)
print(df.columns.to_list())
#
plt.style.use('fivethirtyeight')
plt.figure(figsize=(10, 8))
plt.subplot(1, 2, 1)
sns.countplot(x=df[38], data=df)
plt.subplot(1, 2, 2)
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.savefig('FirstImage')
plt.show()

# df = pd.read_csv('data/data_process.csv')
# st.title('Demo Connect SQL Server')
# top10 = df.groupby("VanPhong").agg(total_Revenue=("TongTienBL", "sum")).nlargest(10, "total_Revenue").reset_index()
# fig = px.bar(top10, x="total_Revenue", y = "VanPhong")
# st.plotly_chart(fig)

#ndim
x = np.array([(1,2),(4,5)])
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([(1, 2, 3), (4, 5, 6)])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(x.ndim)
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)


#itemsize
S = range(1000)
print(sys.getsizeof(5) * len(S))

D = np.arange(1000)
print(D.size)
print(D.itemsize)
print(D.size * D.itemsize)
#4000

#Size, shape
x = np.array([(1,2,3,4,5,6)])
print(x.size)
print(x.shape)

#reshape
a = np.array([(8,9,10),(11,12,13)])
print(a)
a=a.reshape(3,2)
print(a)


#slicing
a=np.array([(8,9),(10,11),(12,13)])
print(a[0:3,0])

#linspace
a=np.linspace(1,3,5)
print(a)

#max/ min
a= np.array([1,2,3,4])
print(a.min())
print(a.max())
print(a.sum())

#axis
a= np.array([(1,2,3),(3,4,5)])
print(a.sum(axis=1))

#Square Root & Standard Deviation:
a=np.array([(10,2,3),(30,4,5,)])
print(np.sqrt(a))
print(np.std(a))

#Addition Operation:
x= np.array([(1,6,3),(3,4,5)])
y= np.array([(1,2,3),(3,4,5)])
print(x+y)
print(x-y)
print(x*y)
print(x/y)

#Vertical & Horizontal Stacking:
x= np.array([(1,2,3),(3,4,5)])
y= np.array([(1,2,3),(3,4,5)])
print(np.vstack((x,y)))
print(np.hstack((x,y)))

#ravel
x= np.array([(1,2,3),(3,4,5)])
print(x.ravel())

#NumPy Array Indexing 
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[1])
print(arr[2]+arr[3])

#Access 2-D Arrays
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
print('2nd element on 2st row: ', arr[1, 1])

#Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# And this is why:
# The first number represents the first dimension, which contains two arrays:
# [[1, 2, 3], [4, 5, 6]]
# and:
# [[7, 8, 9], [10, 11, 12]]
# Since we selected 0, we are left with the first array:
# [[1, 2, 3], [4, 5, 6]]

# The second number represents the second dimension, which also contains two arrays:
# [1, 2, 3]
# and:
# [4, 5, 6]
# Since we selected 1, we are left with the second array:
# [4, 5, 6]

# The third number represents the third dimension, which contains three values:
# 4
# 5
# 6
# Since we selected 2, we end up with the third value:
# 6
print('3nd element on 1st row:', arr[0, 1, 2])

# import pyodbc

# # Establish a connection
# conn = pyodbc.connect(
#     'Driver={SQL Server};'
#     'Server=10.0.0.9;'
#     'Database=BV41;'
#     'UID=hmas41;'
#     'PWD=123456;'
# )

# # Create a cursor object
# cursor = conn.cursor()

# # Execute SQL queries
# cursor.execute("SELECT ProcessID, SID FROM Process where Phone = '0972406036' AND SID IS NOT NULL")
# rows = cursor.fetchall()

# # Process the returned data
# for row in rows:
#     print(row.SID)
#     print(row.ProcessID)

# Close the connection
# conn.close()