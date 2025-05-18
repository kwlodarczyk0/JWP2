import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

df = pd.read_sql_query("SELECT * FROM sales", conn)
st.dataframe(df)

st.subheader('Add sale')
with st.form(key='add_sale'):
    product = st.text_input('Product Name')
    quantity = st.text_input('Quantity')
    price = st.text_input('Price')
    date = st.date_input('Date')
    submit = st.form_submit_button('Submit')
    if submit:
        cursor.execute(
            "Insert into sales (product,quantity,price,date) values (?,?,?,?)",
            (product, quantity, price, date)
        )
        conn.commit()
        st.success('Sales added to database')



st.subheader("Dzienna sprzedaż")
st.line_chart(df["price"]*df["quantity"])

df_gr = df.groupby("product")["price"].sum().reset_index()

st.subheader("Suma produktów według typu")
st.bar_chart(df_gr["price"])

