import pymongo
import pandas as pd

myclient = pymongo.MongoClient("mongodb+srv://padmajothithangavel:Padma123@cluster0.yoja8kw.mongodb.net/")
mydb = myclient["sample_airbnb"]
mycol = mydb.listingsAndReviews.find()

data = []
for i in mycol:
    data.append(i)

## Collecting the Listing details
def listing_details(data):
    listing = [] 
    for i in data:
        listing_dict = {
            "Listing_Id" : i['_id'],
            "Listing_URL" : i['listing_url'],
            "Name" : i['name'],
            "Summary" : i['summary'],
            "Space" : i['space'],
            "Description" : i['description'],
            "Neighborhood_Overview" : i['neighborhood_overview'],
            "Transit" : i['transit'],
            "Access" : i['access'],
            "Interaction" : i['interaction'],
            "House_Rules" : i['house_rules'],
            "Property_Type" : i['property_type'],
            "Room_Type" : i['room_type'],
            "Bed_Type" : i['bed_type'],
            "Minimum_Nights" : i['minimum_nights'],
            "Maximum_Nights" : i['maximum_nights'],
            "Cancellation_Policy" : i['cancellation_policy'],
            "Accommodates" : i['accommodates'],
            "Bedrooms" : i.get('bedrooms'),
            "Beds" : i.get('beds'),
            "Number_of_Reviews" : i['number_of_reviews'],
            "Bathrooms" : i.get('bathrooms'),
            "Price" : i['price'], 
            "Extra_People":i['extra_people'], 
            "Guests_Included":i['guests_included'], 
            "Images":i['images']['picture_url'], 
            "Review_Scores":i['review_scores'].get('review_scores_rating'),
            "Cleaning_Fee":i.get('cleaning_fee')
        }
        listing.append(listing_dict)
    return listing

listing_data = listing_details(data)
listing_df =pd.DataFrame(listing_data)

## Finding the null values in the numerical columns
listing_df.describe().T

listing_df.isnull().sum()

## Handling the Null Values
listing_df.fillna({'Bedrooms':0},inplace=True)
listing_df.fillna({'Beds':0},inplace=True)
listing_df.fillna({'Bathrooms':0},inplace=True)
listing_df.fillna({'Review_Scores':0},inplace=True)
listing_df.fillna({'Cleaning_Fee':0},inplace=True)

listing_df.isnull().sum()

## Convert datas into int data types
listing_df.dtypes

listing_df["Minimum_Nights"]= listing_df["Minimum_Nights"].astype(int)
listing_df["Maximum_Nights"]= listing_df["Maximum_Nights"].astype(int)
listing_df["Bedrooms"]= listing_df["Bedrooms"].astype(int)
listing_df["Beds"]= listing_df["Beds"].astype(int)
listing_df["Bathrooms"]= listing_df["Bathrooms"].astype(str).astype(float).astype(int)
listing_df["Price"]= listing_df["Price"].astype(str).astype(float).astype(int)
listing_df["Extra_People"]= listing_df["Extra_People"].astype(str).astype(float).astype(int)
listing_df["Guests_Included"]= listing_df["Guests_Included"].astype(str).astype(float).astype(int)
listing_df["Review_Scores"]= listing_df["Cleaning_Fee"].astype(str).astype(float).astype(int)
listing_df["Cleaning_Fee"]= listing_df["Cleaning_Fee"].astype(str).astype(float).astype(int)

## Collecting Amenities Details
def amenties_details(data):
    amenities = []
    for i in data:
        amenities_dict = {
            "Listing_Id":i['_id'],
            "Amenities":i['amenities']
        }
        amenities.append(amenities_dict)
    return amenities

amenities_data = amenties_details(data)
amenties_df = pd.DataFrame(amenities_data)

## Sorting the extracted Amenties rows
def sort_amenities(x):
    a = x
    a.sort()
    return a

amenties_df['Amenities'] = amenties_df['Amenities'].apply(lambda x:sort_amenities(x))
amenties_df = amenties_df[amenties_df['Amenities'].str.len() > 0]

## Handling the Null values
amenties_df.isnull().sum()

Id_e = []
Amenities_e = []
for index,row in amenties_df.iterrows():
    if row['Listing_Id'] =='':
        Id_e.append(index)
    if row['Amenities'] == '':
        Amenities_e.append(index)

empty_columns = [Id_e,Amenities_e]
for i in empty_columns:
    print(len(i))

amenties_df.dtypes

## Collecting the Host details
def host_details(data):
    host = []
    for i in data:
        host_dict ={
            "Listing_Id":i['_id'],
            "Host_Id":i['host']['host_id'],
            "Host_URL":i['host']['host_url'],
            "Host_Name":i['host']['host_name'],
            "Host_Location":i['host']['host_location'],
            "Host_About":i['host']['host_about'],
            "Host_Thumbnail_URL":i['host']['host_thumbnail_url'],
            "Host_Picture_URL":i['host']['host_picture_url'],
            "Host_Neighbourhood":i['host']['host_neighbourhood'],
            "Host_Is_Superhost":i['host']['host_is_superhost'],
            "Host_Has_Profile_Pic":i['host']['host_has_profile_pic'],
            "Host_Identity_Verified":i['host']['host_identity_verified'],
            "Host_Listings_Count":i['host']['host_listings_count'],
            "Host_Total_Listings_Count":i['host']['host_total_listings_count'],
            "Host_Verifications":i['host']['host_verifications']   
        }
        host.append(host_dict)
    return host

host_data = host_details(data)
host_df = pd.DataFrame(host_data)

host_df.isnull().sum()

## Handling the Null Values
Listing_Id_e = []
Host_Id_e = []
Host_URL_e = []
Host_Name_e = []
Host_Location_e = []
Host_About_e = []
Host_Thumbnail_URL_e = []
Host_Picture_URL_e = []
Host_Neighbourhood_e = []
Host_Is_Superhost_e = []
Host_Has_Profile_Pic_e = []
Host_Identity_Verified_e = []
Host_Listings_Count_e = []
Host_Total_Listings_Count_e = []
Host_Verifications_e = []

for index,row in host_df.iterrows():
    if row['Listing_Id'] == '':
        Listing_Id_e.append(index)
    if row['Host_Id'] == '':
        Host_Id_e.append(index)
    if row['Host_URL'] == '':
        Host_URL_e.append(index)
    if row['Host_Name'] == '':
        Host_Name_e.append(index)
    if row['Host_Location'] == '':
        Host_Location_e.append(index)
    if row['Host_About'] == '':
        Host_About_e.append(index)
    if row['Host_Thumbnail_URL'] == '':
        Host_Thumbnail_URL_e.append(index)
    if row['Host_Picture_URL'] == '':
        Host_Picture_URL_e.append(index)
    if row['Host_Neighbourhood'] == '':
        Host_Neighbourhood_e.append(index)
    if row['Host_Is_Superhost'] == '':
        Host_Is_Superhost_e.append(index)
    if row['Host_Has_Profile_Pic'] == '':
        Host_Has_Profile_Pic_e.append(index)
    if row['Host_Identity_Verified'] == '':
        Host_Identity_Verified_e.append(index)
    if row['Host_Listings_Count'] == '':
        Host_Listings_Count_e.append(index)
    if row['Host_Total_Listings_Count'] == '':
        Host_Total_Listings_Count_e.append(index)
    if row['Host_Verifications'] == '':
        Host_Verifications_e.append(index)

empty_columns=[Listing_Id_e,Host_Id_e,Host_URL_e,Host_Name_e,Host_Location_e,Host_About_e,Host_Thumbnail_URL_e,Host_Picture_URL_e,Host_Neighbourhood_e,Host_Is_Superhost_e,Host_Has_Profile_Pic_e,Host_Identity_Verified_e,Host_Listings_Count_e,Host_Total_Listings_Count_e,Host_Verifications_e]
for i in empty_columns:
    print(len(i))

host_df['Host_Location']=host_df['Host_Location'].replace({'':"Not Specified"})
host_df['Host_About']=host_df['Host_About'].replace({'':"Not Specified"})
host_df['Host_Neighbourhood']=host_df['Host_Neighbourhood'].replace({'':"Not Specified"})

host_df['Host_Is_Superhost'] = host_df['Host_Is_Superhost'].map({True:'Yes',False:'No'})
host_df['Host_Has_Profile_Pic'] = host_df['Host_Has_Profile_Pic'].map({True:'Yes',False:'No'})
host_df['Host_Identity_Verified'] = host_df['Host_Identity_Verified'].map({True:'Yes',False:'No'})

## Collecting the Address Details
def address_details(data):
    address =[]
    for i in data:
        address_dict = {
            "Listing_Id":i['_id'],
            "Address_street":i['address']['street'],
            "Address_suburb":i['address']['suburb'],
            "Government_Area":i['address']['government_area'],
            "Market":i['address']['market'],
            "Country":i['address']['country'],
            "Country_Code":i['address']['country_code'],
            "Location_type":i['address']['location']['type'],
            "Longitude":i['address']['location']['coordinates'][0],
            "Latitude":i['address']['location']['coordinates'][1],
            "Exact_Location":i['address']['location']['is_location_exact']
        }
        address.append(address_dict)
    return address

address_data = address_details(data)
address_df = pd.DataFrame(address_data)

address_df.isnull().sum()

## Handling the Null Values
Listing_Id_e = []
Address_street_e = []
Address_suburb_e = []
Government_Area_e = []
Market_e = []
Country_e = []
Country_Code_e = []
Location_type_e = []
Longitude_e = []
Latitude_e = []
Exact_Location_e =[]

for index,row in address_df.iterrows():
    if row['Listing_Id']=='':
        Listing_Id_e.append(index)    
    if row['Address_street']=='':
        Address_street_e.append(index)
    if row['Address_suburb']=='':
        Address_suburb_e.append(index)
    if row['Government_Area']=='':
        Government_Area_e.append(index)
    if row['Market']=='':
        Market_e.append(index)
    if row['Country']=='':
        Country_e.append(index)
    if row['Country_Code']=='':
        Country_Code_e.append(index)
    if row['Location_type']=='':
        Location_type_e.append(index)
    if row['Longitude']=='':
        Longitude_e.append(index)
    if row['Latitude']=='':
        Latitude_e.append(index)
    if row['Exact_Location']=='':
        Exact_Location_e.append(index)

empty_columns = [Listing_Id_e,Address_street_e,Address_suburb_e,Government_Area_e,Market_e,Country_e,Country_Code_e,Location_type_e,Longitude_e,Latitude_e,Exact_Location_e] 
for i in empty_columns:
    print(len(i))

address_df['Address_suburb']=address_df['Address_suburb'].replace({'':"Not Specified"})

## Collecting the Availability Details

def availability_details(data):
    availability = []
    for i in data:
        availability_dict={
            "Listing_Id" : i['_id'],
            "Availability_30" : i['availability']['availability_30'],
            "Availability_60" : i['availability']['availability_60'],
            "Availability_90":i['availability']['availability_90'],
            "Availability_365" :i['availability']['availability_365']
        }
        availability.append(availability_dict)
    return availability

availability_data = availability_details(data)
availability_df = pd.DataFrame(availability_data)

availability_df.dtypes

availability_df.isnull().sum()

## Converting the DataFrame to csv
listing_df.to_csv('listing.csv')
amenties_df.to_csv('amenities.csv')
host_df.to_csv('host.csv')
address_df.to_csv('address.csv')
availability_df.to_csv('availability.csv')
