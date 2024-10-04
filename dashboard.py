import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('white')

st.title('Analisis Data E-Commerce')
tab1, tab2, tab3, tab4 = st.tabs(["Negara Bagian", "Metode Pembayaran", "Produk", "Tingkat Kepuasan"])

with tab1:
    st.header("Negara Bagian dengan Customer Terbanyak dan Paling Sedikit")
    
    url='https://drive.google.com/file/d/1Z80xMdeEOEub_nSUQBKiwxb2Vwgj3qkV/view?usp=drive_link'
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    customer_df = pd.read_csv(url)

    state_df = customer_df.groupby("customer_state").customer_id.nunique().sort_values(ascending=False).reset_index()
    
    fig, ax = plt.subplots()

    sns.barplot(x="customer_id", y="customer_state", data=state_df.head(27))
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.set_title("5 Produk Penjualan Tertinggi", loc="center", fontsize=15)
    ax.tick_params(axis ='y', labelsize=12)

    st.pyplot(fig)

    st.subheader('Dataset Customer')
    st.dataframe(data=customer_df, width=1200, height=350)
    st.write("Dataset diatas merupakan dataset customer yang terdiri dari beberapa parameter seperti customer_id, customer_state, dan customer_city ")
    st.write("Dataset tersebut kemudian akan di assess untuk mengetahui potensi masalah yang akan muncul saat proses analisis data ")
    st.write("Melalui proses assessing data, tidak ditemukan masalah yang mungkin bisa menghambat proses analisis data sehingga dapat dilanjutkan ke tahapan Exploratory Data")

    st.subheader('Dataset Customer Sorted State')
    st.caption('Hasil exploratory data')
    
    st.dataframe(data=state_df, width=1200, height=980)
    st.write("Exploratory Data menunjukkan urutan negara bagian dengan jumlah customer terbanyak dan terendah")
    
    
with tab2:
    st.header("Metode Pembayaran yang Paling Banyak Dipilih")
    
    url='https://drive.google.com/file/d/11Bx5CiO1o5W8-tqrnXC_c8iq2zyu1xZP/view?usp=sharing'
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    order_payments_df = pd.read_csv(url)
    methods_df = order_payments_df.groupby("payment_type").order_id.nunique().sort_values(ascending=False).reset_index()
    
    fig, ax = plt.subplots()
 
    sns.barplot(x="order_id", y="payment_type", data=methods_df.head(27))
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.set_title("Metode Pembayaran Terpopuler", loc="center", fontsize=15)
    ax.tick_params(axis ='y', labelsize=12)

    st.pyplot(fig)

    st.subheader('Dataset Order Payments')
    st.dataframe(data=order_payments_df, width=1200, height=350)

    st.subheader('Sorting Metode Paling Banyak Digunakan')
    st.dataframe(data=methods_df, width=1200, height=200)

    
with tab3:
    st.header("Produk Dengan Penjualan Tertinggi dan Terendah")
    
    url='https://drive.google.com/file/d/1G_9F_Js_kL1itiYbyl4WTtVkOZvbXXkP/view?usp=sharing'
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    order_items_df = pd.read_csv(url)
    url='https://drive.google.com/file/d/1dWZGvb2J2aC2pvyiXac2DxG5uQvuE6Xg/view?usp=sharing'
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    product_category_df = pd.read_csv(url)
    url='https://drive.google.com/file/d/1s0XclYEbPq-NJNp3QmpW3favw9Oy6i0Y/view?usp=sharing'
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    product_df = pd.read_csv(url)

    item_product_df = pd.merge(
        left=order_items_df,
        right=product_df,
        how="left",
        left_on="product_id",
        right_on="product_id"
    )
    item_product_df.head()

    english_item_df = pd.merge(
        left=item_product_df,
        right=product_category_df,
        how="left",
        left_on="product_category_name",
        right_on="product_category_name"
    )
    english_item_df.head()
    Product_eng_df = english_item_df.groupby(by="product_category_name_english").product_id.nunique().sort_values(ascending=False)
    highest_product_df = english_item_df.groupby("product_category_name_english").product_id.nunique().sort_values(ascending=False).reset_index()
    
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
 
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
    sns.barplot(x="product_id", y="product_category_name_english", data=highest_product_df.head(5), palette=colors, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("5 Produk Penjualan Tertinggi", loc="center", fontsize=15)
    ax[0].tick_params(axis ='y', labelsize=12)
 
    sns.barplot(x="product_id", y="product_category_name_english", data=highest_product_df.sort_values(by="product_id", ascending=True).head(5), palette=colors, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("5 Produk Penjualan Terendah", loc="center", fontsize=15)
    ax[1].tick_params(axis='y', labelsize=12)
 
    plt.suptitle("Data Penjualan Produk Tertinggi dan Terendah", fontsize=20)
    st.pyplot(fig)

    st.subheader('Dataset Order Item, Product, Product Category')
    st.caption("Dataset Order Items")
    st.dataframe(data=order_items_df, width=1200, height=140)

    st.caption("Dataset Product Category")
    st.dataframe(data=product_category_df, width=1200, height=140)

    st.caption("Dataset Product")
    st.dataframe(data=product_df, width=1200, height=140)

    st.subheader('Exploratory Order Item, Product, Product Category')
    
    st.caption("Dataset Gabungan Order Item, Product, Product Category")
    st.dataframe(data=english_item_df, width=1200, height=140)

    
    st.caption("Sort Produk Dengan Penjualan Tertinggi")
    st.dataframe(data=Product_eng_df, width=1200, height=140)
    
    
with tab4:
    st.header("Tingkat Kepuasan Customer")
    
    url='https://drive.google.com/file/d/1wBvAknA86m8pZm1COBdGflmiLYRpKn4n/view?usp=sharing'
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    order_reviews_df = pd.read_csv(url)
    score_df = order_reviews_df.groupby(by="review_score").order_id.nunique().reset_index()
    
    fig, ax = plt.subplots()
 
    sns.barplot(y="order_id", x="review_score", data=score_df.head(27))
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.set_title("Metode Pembayaran Terpopuler", loc="center", fontsize=15)
    ax.tick_params(axis ='y', labelsize=12)

    st.pyplot(fig)

    st.subheader('Dataset Order Reviews')
    st.dataframe(data=order_reviews_df, width=1200, height=350)

    st.subheader('Ringkasan Score Review')
    st.dataframe(data=score_df, width=1200, height=210)

    