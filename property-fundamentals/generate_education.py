from govuk_api.ofns.api import API as OFNS_API
from google_api.api import API as GOOGLE_API
from govuk_ws.ofsted.schoolratings import SchoolRatings
from doogal_api.api import API as DOOGAL_API
#from govuk_ws.geoportal.postcode_to_ward import PostcodeMapping
from postcodes_api.postcode_api import API as POSTCODE_API
from development_district import district
from development_district import wards
from development_district import centre_lat
from development_district import centre_lng
from development_district import distance
from development_district import max_lat
from development_district import min_lat
from development_district import max_lng
from development_district import min_lng
import matplotlib.pyplot as plt
import numpy as np
import json

school_ratings = SchoolRatings()
doogal_api = DOOGAL_API()
ofns_api = OFNS_API()
google_api = GOOGLE_API(key_path="../property-fundamentals/google_api/key.txt")
#postcode_mapping = PostcodeMapping()
postcodes_api = POSTCODE_API()
import simplekml
import zipfile
kml = simplekml.Kml()

y_pos = np.arange(len(wards[0]))
point = []
school_ward = []
icon_style = ['images/icon-1.png', 'images/icon-2.png', 'images/icon-3.png', 'images/icon-4.png','images/icon-10.png']
ofsted_rating = ['Outstanding', 'Good', 'Requires improvement', 'Poor']
further_education_count = np.array([0]*len(wards[0]))
school_count_outstanding = np.array([0]*len(wards[0]))
school_count_good = np.array([0]*len(wards[0]))
school_count_requires_improvement = np.array([0]*len(wards[0]))
school_count_poor = np.array([0]*len(wards[0]))

school_data = school_ratings.get_schools_with_coordinates_from_district(doogal_api, district)

further_education_result = google_api.nearby_search(
    centre_lat,
    centre_lng,
    distance,
    location_type='university'
)

for j in range (0,len(further_education_result)):
    if (further_education_result[j][2]['lat'] <= max_lat) and (further_education_result[j][2]['lat'] >= min_lat) and (further_education_result[j][2]['lng'] <= max_lng) and (further_education_result[j][2]['lng'] >= min_lng):
        #Create the plot
        further_education_ward = postcodes_api.get_postcode(str(further_education_result[j][2]['lng']),str(further_education_result[j][2]['lat']))
        if further_education_ward is not None:
            for i in range (0,len(wards[0])):
                if further_education_ward == wards[0][i]:
                    further_education_count[i] +=1
            #create the KML
            point = kml.newpoint()
            point.name = further_education_result[j][0]
            point.description = further_education_result[j][0]
            point.coords = [(further_education_result[j][2]['lng'],further_education_result[j][2]['lat'])]
            point.style.iconstyle.icon.href = icon_style[4]

    
for name, postcode, rating, ward, school_coordinates in school_data:
    lng , lat = map(float, str(school_coordinates).strip('[]').split(','))
    if (lat <= max_lat) and (lat >= min_lat) and (lng <= max_lng) and (lng >= min_lng):
        #create the KML
        point = kml.newpoint()
        point.name = name
        point.description = ofsted_rating[int(rating)-1]
        point.coords = [school_coordinates]
        point.style.iconstyle.icon.href = icon_style[int(rating)-1] 
        #Create the plot
        school_ward.insert(0,doogal_api.get_postcode_info(postcode))
        if int(rating) == 1:
            for j in range (0,len(wards[0])):
                if school_ward[0][6] == wards[0][j]:
                    school_count_outstanding[j] +=1
        elif int(rating) == 2:
             for j in range (0,len(wards[0])):
                if school_ward[0][6] == wards[0][j]:
                    school_count_good[j] +=1                
        elif int(rating) == 3:
            for j in range (0,len(wards[0])):
                if school_ward[0][6] == wards[0][j]:
                    school_count_requires_improvement[j] +=1                    
        elif int(rating) == 4:
            for j in range (0,len(wards[0])):
                if school_ward[0][6] == wards[0][j]:
                    school_count_poor[j] +=1

#Save and zip the KML/KMZ  
kml.save(district + "_education" + ".kml")
zf = zipfile.ZipFile(district + "_education" + ".kmz", "w")
zf.write("images/icon-1.png")
zf.write("images/icon-2.png")
zf.write("images/icon-3.png")
zf.write("images/icon-4.png")
zf.write("images/icon-10.png")
zf.write(district + "_education" + ".kml")
zf.close()

#plot the further education data
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
plt.barh(y_pos, further_education_count, color = (0.1015625,0.13671875,0.4921875), edgecolor='black') #color = (R,G,B)
plt.yticks(y_pos,wards[0])
plt.gca().invert_yaxis()
plt.xlabel("Number of Further Education Institutions")
plt.title(district + " Further Education Institutions", weight='bold')
plt.savefig(district + "_further_education" + ".png", bbox_inches='tight', transparent=True)
plt.clf()


#plot the school data
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
p1 = plt.barh(y_pos, school_count_poor, color = (0.7578125,0.09375,0.35546875), edgecolor='black', left=school_count_requires_improvement+school_count_good+school_count_outstanding) #color = (R,G,B)
p2 = plt.barh(y_pos, school_count_requires_improvement, color = (0.98046875,0.75,0.17578125), edgecolor='black', left=school_count_good+school_count_outstanding) #color = (R,G,B)
p3 = plt.barh(y_pos, school_count_good, color = (0.484375,0.69921875,0.2578125), edgecolor='black', left=school_count_outstanding) #color = (R,G,B)
p4 = plt.barh(y_pos, school_count_outstanding, color = (0.03515625,0.44140625,0.21875), edgecolor='black') #color = (R,G,B)
plt.yticks(y_pos,wards[0])
plt.gca().invert_yaxis()
plt.xlabel("Number of Schools")
plt.title(district + " Primary and Secondary School Ofsted Rating", weight='bold')
plt.legend([p4,p3,p2,p1],["Outstanding", "Good", "Requires Improvement", "Poor"], loc="lower center", bbox_to_anchor=(0.5,-0.4), framealpha=0)
plt.savefig(district + "_ofsted_rating" + ".png", bbox_inches='tight', transparent=True)
plt.clf()
