import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.stoggle import stoggle
from PIL import Image


#Using csv file to convert into Dataframe
#Listing CSV
df_1 = pd.read_csv('availability.csv')
availability_df = pd.DataFrame(df_1,columns=["Listing_Id","Availability_30","Availability_60","Availability_90","Availability_365"])

def availability_analysis(availability_df):
    fig_availability = px.scatter_3d(availability_df,x="Listing_Id",y="Availability_30",z="Availability_365",hover_data=["Listing_Id", "Availability_30", "Availability_365"],color="Availability_365",width=700,height=800)
    st.plotly_chart(fig_availability)

    fig_availability = px.scatter_3d(availability_df,x="Listing_Id",y="Availability_60",z="Availability_365",hover_data=["Listing_Id", "Availability_60", "Availability_365"],color="Availability_365",width=700,height=800)
    st.plotly_chart(fig_availability)

    fig_availability = px.scatter_3d(availability_df,x="Listing_Id",y="Availability_90",z="Availability_365",hover_data=["Listing_Id", "Availability_90", "Availability_365"],color="Availability_365",width=700,height=800)
    st.plotly_chart(fig_availability)


#Streamlit Page
icon = Image.open("airbnb-logo.png")
with open("Introducing Icons.mp4","rb") as video_file:
    video_bytes=video_file.read()
st.set_page_config(page_title="Airbnb Data Analysis",
                   page_icon= icon,
                   layout="wide",
                   initial_sidebar_state="collapsed")

with st.sidebar:
    select = option_menu("Main Menu",("Home","Data Analysis","Insights"))

if select == "Home":
    st.title("****AIRBNB DATA ANALYSIS****",)
    st.divider()
    col1,col2 = st.columns(2)
    with col1:
        st.markdown(" ")
        st.markdown(" ")
        st.write("***Airbnb, Inc. is an American company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. Airbnb is the most well-known company for short-term housing rentals***")
    with col2:
        st.image(image="Airbnb-img.jpeg",caption="Airbnb",use_column_width=False,width=400)
    stoggle("About Airbnb","After moving to San Francisco in October 2007, roommates and former schoolmates Brian Chesky and Joe Gebbia came up with an idea of putting an air mattress in their living room and turning it into a bed and breakfast.The site Airbed and breakfast.com officially launched on August 11, 2008.The founders had their first customers in the summer of 2008, during the Industrial Design Conference held by Industrial Designers Society of America, where travelers had a hard time finding lodging in the city.In March 2009, the name of the company was shortened to Airbnb.com to eliminate confusion over air mattresses; by then listings included entire rooms and properties.By November 2010, out of 700,000 nights booked, 80% had occurred in the previous six months.At the March 2011 South by Southwest conference, Airbnb won the APP award.In November 2012, Airbnb launched NEIGHBORHOODS, a travel guide of 23 cities that helps travelers choose a neighborhood in which to stay based on certain criteria and personal preferences.By October 2013, Airbnb had served 9,000,000 guests since its founding in August 2008.[22] Nearly 250,000 listings were added in 2013.In July 2014, Airbnb revealed design revisions to the site and mobile app and introduced a new logo.")
    st.markdown(" ")
    st.write("****In March 2024, Airbnb announced a ban on indoor cameras for properties listed on the site, scheduled to take effect on April 30. The changes also involve a requirement for hosts to disclose the use of noise-decibel monitoring equipment****")
    st.video(video_bytes)

if select == "Data Analysis":
    st.title("DATA ANALYSIS")
    st.header("Amenities Analysis")
    availability_analysis(availability_df)

if select == "Insights":
    st.title("****Insights****")
    st.subheader("Countries located for Airbnb")
    st.write("**Australia**")
    st.write("**Brazil**")
    st.write("**Canada**")
    st.write("**China**")
    st.write("**Hong Kong**")
    st.write("**Portugal**")
    st.write("**Spain**")
    st.write("**Turkey**")
    st.write("**United States**")

    st.subheader("Detailed View Points")
    stoggle("Price Level","Maximum every place has a equal level of price as per their country wise.But in listing_id-14644562 a city in Hong Kong has a maximum price comapred with other places.")

    stoggle("Availability","As per Availability 1193 Listing Id is not available for 365 days.")

    stoggle("Amenities","In most of the rooms common amenities has AIR CONDITIONING,IRON,KITCHEN and WIFI faciliteies are avilable.")

    stoggle("Host Details","Overall Host neighborhood count is maximum in Listing_Id-97178439")
