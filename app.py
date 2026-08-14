import streamlit as st  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt 

np.random.seed(42)
sales_data={
    'Months':['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec'],
    'Cost':np.random.randint(10,100,size=12),
    'Revenue':np.random.randint(20,150,size=12)
}
data=pd.DataFrame(sales_data)

st.set_page_config(page_title="Cost & Revenue Dashboard",page_icon="📈")
st.title("Monthly Cost and Revenue Dashboard")

with st.sidebar:
    st.subheader("Select a Month")
    selected_month=st.selectbox("Choose a month",data['Months'])
    if selected_month:
        month_data=data[data['Months'] ==selected_month]
        st.write(f"Cost for {selected_month}:${month_data['Cost'].values[0]}")
        st.write(f"Revenue for {selected_month}:${month_data['Revenue'].values[0]}")

total_cost=data['Cost'].sum()
total_revenue=data['Revenue'].sum()
avg_cost=data['Cost'].mean()
avg_revenue=data['Revenue'].mean()

col1,col2,col3,col4=st.columns(4)
with col1:
    st.metric(label="Total Cost",value=f"${total_cost}")
with col2:
    st.metric(label="Total Revenue",value=f"${total_revenue}")
with col3:
    st.metric(label="Avg Cost",value=f"${round(avg_cost,2)}")
with col4:
    st.metric(label="Avg Revenue",value=f"${avg_revenue}")

col1,col2=st.columns(2)
with col1:
    st.subheader("Cost Distribution")
    fig,ax=plt.subplots(figsize=(10, 5))
    ax.pie(data['Cost'],labels=data['Months'],autopct='%1.1f%%',startangle=90)
    st.pyplot(fig)
with col2:
    st.subheader("Revenue Distribution")
    fig,ax=plt.subplots(figsize=(10, 10))
    ax.bar(data['Months'],data['Revenue'],label='Revenue',color='purple',alpha=0.7)
    ax.set_xlabel('Months')
    ax.set_ylabel('Amount')
    ax.legend()
    st.pyplot(fig)
with st.expander("Data Table"):
    st.dataframe(data)




    

