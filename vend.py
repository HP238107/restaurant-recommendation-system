import streamlit as st
import pickle
import pandas as pd
import base64
from PIL import Image
import matplotlib.pyplot as plt
import altair as alt
from plotly import graph_objs as go
st.set_option('deprecation.showPyplotGlobalUse', False)
hide_st_style="""
              <style>
              MainMenu {visibility: hidden;}
              footer {visibility: hidden;}
              </style>
              """
st.markdown(hide_st_style,unsafe_allow_html=True)





user_menu = st.sidebar.radio(
    'Select an Option',
    ('Vendor Recommendation','Overall Analysis')
)

if user_menu == 'Vendor Recommendation':


   st.title('Restaurant Recommendation')

   image= Image.open("vegetables-set-left-black-slate.png")
   st.image(image)
   customer= pickle.load(open('customer.pkl','rb'))
   d = pd.DataFrame(customer)
   user_final_ratings = pickle.load(open('customer_final_ratings.pkl','rb'))


   def recommend(x):
     a = user_final_ratings.iloc[x].sort_values(ascending=False)[0:5]
     vendor_id = []
     vendor_rate = []

     for i in a.index:
        vendor_id.append(d[d['vendor_id'] == i]['vendor_id'].iloc[0])
        vendor_rate.append(d[d['vendor_id'] == i]['vendor_rating_y'].iloc[0])

        B = pd.DataFrame(list(zip(vendor_id, vendor_rate)),
                         columns=['vendor_ID', 'Rating'])
        Z = B.sort_values(by=['Rating'], ascending=False)

     return Z


   g = d['customer_id'].drop_duplicates()
   x = st.selectbox(
       'Please select customer ID',
        g.values)
   if st.button('Recommend'):
    recommendation = recommend(x)
    st.dataframe(recommendation)


   def ry(y):
        tag = []
        latitude=[]
        longitude=[]
        tag.append(d['vendor_tag_name'][y])
        latitude.append(d["ven_latitude"][y])
        longitude.append(d["ven_longitude"][y])
        f = pd.DataFrame(list(zip(tag,latitude,longitude)),
                        columns=['cuisine','Latitude','Longitude'])
        return f


   recommendation = recommend(x)
   y = st.selectbox('Please select Vendor_id',
                     recommendation['vendor_ID'].values)
   if st.button('Vendor'):
     vendor1 = ry(y)
     st.table(vendor1)


if user_menu == 'Overall Analysis':
    @st.cache
    def load_data():
        data = pd.read_csv("NEW_Project.csv", nrows=100)
        data = data.drop_duplicates()
        return data


    data = load_data()
    if st.checkbox("Show Data"):
        st.write(data)



    st.subheader('Data Analysis about vendor rating, customer data and vendor id.')
    c= alt.Chart(data).mark_circle().encode(
        x="vendor_id", y= "customer_id", size ="vendor_rating_y",color="vendor_rating_y",  tooltip=['vendor_id', 'customer_id', 'vendor_rating_y'])
    st.altair_chart(c, use_container_width=True)


    st.subheader("Data analysis about preepration time for each order")
    bar_chart= alt.Chart(data).mark_bar().encode(
         x='akeed_order_id',y='vendor_id',color='prepration_time:N',tooltip=['akeed_order_id','vendor_id','prepration_time']
     )
    st.altair_chart(bar_chart, use_container_width=True)


    st.subheader("Data Analysis about Payment Mode")
    fig, ax = plt.subplots()
    ax.pie(data.payment_mode.value_counts(), labels=data.payment_mode.unique(), autopct='%1.0f%%',
           explode=(0.1,0.2,0,0.1,0), shadow=True, startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

    st.subheader("Vendor Location")
    data_of_map = data[["latitude", "longitude"]]
    st.map(data_of_map)



    st.subheader("Data Analysis about Vendor_rating")
    val = st.slider("Filter data using rating", 0.0, 4.9)
    data = data.loc[data["vendor_rating_y"] >= val]
    plt.figure(figsize=(10, 5))
    plt.scatter(data["vendor_rating_y"], data["customer_id"])
    plt.ylim(0)
    plt.xlabel("Vendor Rating")
    plt.ylabel("Customer ID")
    plt.tight_layout()
    st.pyplot()
