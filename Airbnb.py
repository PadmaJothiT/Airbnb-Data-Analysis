import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


#Using csv file to convert into Dataframe
#Listing CSV
df_1 = pd.read_csv('listing.csv')

#Host CSV
df_2 = pd.read_csv('host.csv')

def price_analysis(listing_df):
    fig_price_ana = sns.barplot(x=Price,y=Review_Scores,hue=Host_Location,data=listing_df)
    plt.legend(loc='upper right')
    st.pyplot(fig_price_ana.figure)



#Streamlit Page
icon = Image.open("airbnb-logo.png")
with open("Introducing Icons.mp4","rb") as video_file:
    video_bytes=video_file.read()
st.set_page_config(page_title="Airbnb Data Analysis",
                   page_icon= icon,
                   layout="wide",
                   initial_sidebar_state="collapsed")

with st.sidebar:
    select = option_menu("Main Menu",("Home","Data Analysis"))

if select == "Home":
    st.title("AIRBNB DATA ANALYSIS:sunglasses",)
    st.divider()
    st.write("***Airbnb, Inc. is an American company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. Airbnb is the most well-known company for short-term housing rentals***")
    col1,col2=st.columns(2)
    with col1:
        st.image(image="Airbnb-img.jpeg",caption="Airbnb",use_column_width=False,width=400)
    with col2:
        st.write("***After moving to San Francisco in October 2007, roommates and former schoolmates Brian Chesky and Joe Gebbia came up with an idea of putting an air mattress in their living room and turning it into a bed and breakfast.***")
        st.write("****The site Airbed and breakfast.com officially launched on August 11, 2008.****")
        st.write("***The founders had their first customers in the summer of 2008, during the Industrial Design Conference held by Industrial Designers Society of America, where travelers had a hard time finding lodging in the city.***")
    st.write("***In March 2009, the name of the company was shortened to Airbnb.com to eliminate confusion over air mattresses; by then listings included entire rooms and properties.***")
    st.write("***By November 2010, out of 700,000 nights booked, 80% had occurred in the previous six months.***")
    st.write("***At the March 2011 South by Southwest conference, Airbnb won the APP award.***")
    st.write("***In November 2012, Airbnb launched NEIGHBORHOODS, a travel guide of 23 cities that helps travelers choose a neighborhood in which to stay based on certain criteria and personal preferences.***")
    st.write("***By October 2013, Airbnb had served 9,000,000 guests since its founding in August 2008.[22] Nearly 250,000 listings were added in 2013.In July 2014, Airbnb revealed design revisions to the site and mobile app and introduced a new logo.***")
    st.markdown(" ")
    st.write("****In March 2024, Airbnb announced a ban on indoor cameras for properties listed on the site, scheduled to take effect on April 30. The changes also involve a requirement for hosts to disclose the use of noise-decibel monitoring equipment****")
    st.video(video_bytes)

if select == "Data Analysis":
    st.title("DATA ANALYSIS")
    tab1,tab2 = st.tabs(["***PRICE ANALYSIS***","***AVAILABILITY ANALYSIS***"])
    with tab1:
        st.title("PRICE ANALYSIS IN LOCATION WISE")

        price_analysis(df_1)