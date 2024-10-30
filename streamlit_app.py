import streamlit as st
from io import StringIO
st.title("Ben's Bowling Greens")

#from shapely.geometry import Point, Polygon
#import geopandas as gpd
import pandas as pd
#import geopy

#from geopy.geocoders import Nominatim
#from geopy.extra.rate_limiter import RateLimiter

import folium
from streamlit_folium import st_folium

import csv


str_data =StringIO("""Country,Region,Town,Name,Street Address,Postcode,lat,long,Website,Email Address,Telephone
UK,Shropshire,Shrewsbury,Shrewsbury Indoor Bowls Club,"Shrewsbury Sports Village, Sundorne Rd, Shrewsbury SY1 4RQ",SY1 4RQ,52.727485,-2.7197761,,,01743 361128
UK,Shropshire,Shrewsbury,Old Shrewsbury Bowling Club Ltd,"Victoria Ave, Coleham, Shrewsbury SY1 1XR",SY1 1XR,52.705273,-2.7527551,,,01743 344192
UK,Shropshire,Shrewsbury,Meole Brace Bowling Club,"Meole Rise, off, Upper Rd, Shrewsbury SY3 9JF",SY3 9JF,52.694802,-2.756644,,,01743 343219
UK,Shropshire,Shrewsbury,"Bagley Bowling Club, Shrewsbury","24-41 Wood St, Shrewsbury SY1 2PN",SY1 2PN,52.718115,-2.7506519,,,
UK,Shropshire,Shrewsbury,Greenfields Bowling Club,"19C Falstaff St, Shrewsbury SY1 2QN",SY1 2QN,52.719838,-2.7483127,,,07903 397957
UK,Shropshire,Shrewsbury,Castlefields Bowling Club,"26-34 Queen St, Shrewsbury SY1 2JX",SY1 2JX,52.714804,-2.7411505,,,
UK,Shropshire,Shrewsbury,Battlefield Bowling Club,"29 Battlefield Rd, Shrewsbury SY1 4AB",SY1 4AB,52.742267,-2.7207603,,,
UK,Shropshire,Shrewsbury,Shelton Bowling Club,"Bicton Heath, Shrewsbury SY3 5FT",SY3 5FT,52.712287,-2.8018278,,,
UK,Shropshire,Shrewsbury,Hanwood Bowling Club,"Great Hanwood, Shrewsbury SY5 8LJ",SY5 8LJ,52.681033,-2.8288275,,,
UK,Shropshire,Shrewsbury,Unison Bowling Club,Shrewsbury SY2 5LR,SY2 5LR,52.706345,-2.7309132,,,
UK,Shropshire,Shrewsbury,Bicton Bowling Club,"9 Church Cl, Bicton, Shrewsbury SY3 8EN",SY3 8EN,52.727215,-2.8182273,,,
UK,Shropshire,Shrewsbury,Atcham Malthouse Bowling Club,"Malthouse Ln, Atcham, Shrewsbury SY5 6QE",SY5 6QE,52.6791,-2.6789698,,,01743 762374
UK,Shropshire,Shrewsbury,Wem Sports Bowling Club,"59 Bowens Fld, Wem, Shrewsbury SY4 5AR",SY4 5AR,52.858902,-2.7247119,,,
UK,Shropshire,Shrewsbury,Hadnall Bowling Club,"10A Station Rd, Hadnall, Shrewsbury SY4 4AF",SY4 4AF,52.773921,-2.7102546,,,
UK,Shropshire,Shrewsbury,Pontesbury BC Nags Head Green,"2 Main Rd, Pontesbury, Shrewsbury SY5 0RR",SY5 0RR,52.64949,-2.8903865,,,
UK,Shropshire,Oswestry,Oswestry Church Bowling Club,"40-42 Church St, Oswestry SY11 2SY",SY11 2SY,52.857219,-3.0577978,,,
UK,Shropshire,Oswestry,Oswestry Bowling Club,"33 Welsh Walls, Oswestry SY11 1AP",SY11 1AP,52.860495,-3.058427,,,
UK,Shropshire,Oswestry,Ye Olde Croft Bowling Club,Oswestry SY11 1BZ,SY11 1BZ,52.86123,-3.0597223,,,
""")
#str_data2 = str_data
#df = pd.read_csv(str_data, sep=",")


reader = csv.reader(str_data)
data2 = list(reader)

df = pd.DataFrame(data2)
headers = df.iloc[0].values
df.columns = headers
df.drop(index=0, axis=0, inplace=True)

#df.drop(index=0, axis='columns', inplace=True)
df.drop("Country", axis='columns', inplace=True)
df.drop("Region", axis='columns', inplace=True)
df.drop("Town", axis='columns', inplace=True)
df.drop("Postcode", axis='columns', inplace=True)
df.drop("lat", axis='columns', inplace=True)
df.drop("long", axis='columns', inplace=True)


#st.write(data2)
#map_data=[]


# center on Liberty Bell, add marker
m = folium.Map(location=[52.714804, -2.7411505], zoom_start=6)

for postcode in data2:
    #st.write(postcode[6])
    #print(postcode[6], postcode[7])
    
    if postcode[6] !="lat":
        folium.Marker([str(postcode[6]), str(postcode[7])], popup=postcode[3]
                      ).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m) #, width=725)

#postcode = st.sidebar.text_input("Postcode", postcode[5])
#postcode="sy1 2pn"
#geolocator = Nominatim(user_agent="GTA Lookup")
#geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
#location = geolocator.geocode(postcode+", "+"UK")

#lat = location.latitude
#lon = location.longitude

#map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})

#st.map(map_data) 


st.dataframe(df,use_container_width = False)

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

