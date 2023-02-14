import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 
import matplotlib



upload_file = st.file_uploader(label="please upload your CSV file")

if upload_file is not None :
   df = pd.read_csv(upload_file)
   st.success("upload file success!")
else:
   st.stop()

st.write(pd.DataFrame(df))

x_var = st.selectbox(label= "please choose the x lable",
                     options=['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin'])

y_var = st.selectbox(label= "please choose the y lable",
                     options=['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin'])

fig1, ax = plt.subplots()
ax = sns.scatterplot(data=df,x=x_var,y=y_var)
plt.xlabel(x_var)
plt.ylabel(y_var)
plt.title('auto-mpg')
st.pyplot(fig1)

fig2, bx = plt.subplots()
bx = sns.lineplot(data=df,x=x_var,y=y_var)
plt.xlabel(x_var)
plt.ylabel(y_var)
plt.title('auto-mpg')
st.pyplot(fig2)

