import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Input phone number
number = input("Enter a phone number: ")

# Parse the phone number
pepnumber = phonenumbers.parse(number)

# Get the location (country/region) of the phone number
location = geocoder.description_for_number(pepnumber, "en")
print("Location:", location)

# Get the service provider (carrier) of the phone number
service_pro = carrier.name_for_number(pepnumber, "en")
print("Service Provider:", service_pro)

# Use OpenCageGeocode to get latitude and longitude
key = "d447d6d81b824b2fac83a416ed17a1d4"  # Replace with your OpenCage API key
geocoder = OpenCageGeocode(key)
query = str(location)

# Perform geocoding
results = geocoder.geocode(query)

if results and len(results):
    # Extract latitude and longitude
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print("Latitude:", lat, "Longitude:", lng)

    # Create a map using folium
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)

    # Save the map to an HTML file
    myMap.save("mylocation.html")
    print("Map saved to mylocation.html")
else:
    print("No results found for the given location.")
