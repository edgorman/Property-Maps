import simplekml
import matplotlib.pyplot as plt
import numpy as np
from development_district import wards
from development_district import coordinates
from development_district import district
from development_district import ward_codes
from development_district import population
from statxplore_api.api import API as STATXPLORE_API
import json

#Define variables / lists
kml = simplekml.Kml()
colour = ['19FF78B4', '1EFF78B4', '23FF78B4', '28FF78B4', '2DFF78B4', '32FF78B4', '37FF78B4', '3CFF78B4', '41FF78B4', '46FF78B4', '4BFF78B4', '50FF78B4', '55FF78B4' ,'5AFF78B4', '5FFF78B4', '64FF78B4', '69FF78B4', '6EFF78B4', '73FF78B4', '78FF78B4', '7DFF78B4', '82FF78B4', '87FF78B4', '8CFF78B4', '91FF78B4', '96FF78B4', '9BFF78B4', 'A0FF78B4', 'A5FF78B4', 'AAFF78B4']
colour_plot = ['#B478FF19', '#B478FF1E', '#B478FF23', '#B478FF28', '#B478FF2D', '#B478FF32', '#B478FF37', '#B478FF3C', '#B478FF41', '#B478FF46', '#B478FF4B', '#B478FF50', '#B478FF55', '#B478FF5A', '#B478FF5F', '#B478FF64', '#B478FF69', '#B478FF6E', '#B478FF73', '#B478FF78', '#B478FF7D', '#B478FF82', '#B478FF87', '#B478FF8C', '#B478FF91', '#B478FF96', '#B478FF9B', '#B478FFA0', '#B478FFA5', '#B478FFAA']

print(ward_codes)

#-------------------------------------Update (Currently Cheltenham)
housing_benefit = ["151", "78", "76", "110", "43", "110", "382", "229", "64", "403", "131", "190", "74", "323", "359", "399", "247", "153", "98", "117"]
month = "May"
year = "2021"
#--------------------------------------


housing_benefit_percentage = []
pol = []
colour_scale = []
price_plot = []
y_pos = np.arange(len(wards[0]))
housing_benefit_percentage_scale = []
statxplore_api = STATXPLORE_API(key_path="../property-fundamentals/statxplore_api/key.txt")
yaxis = []
xaxis = []
colouraxis = []

#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]
    
    #housing_benefit.append(statxplore_api.get_housing_benefit('table', ward_codes[h]))
    housing_benefit_percentage.append((float(housing_benefit[h])*100) / (float(population[h])))
    
print(housing_benefit_percentage)

#Generate price scaling information
max_housing_benefit_percentage = max(housing_benefit_percentage)
min_housing_benefit_percentage = min(housing_benefit_percentage)
delta = max_housing_benefit_percentage - min_housing_benefit_percentage
step = delta / (len(colour)-1)

#Normalise the colours in the price range
for i in range(0,len(colour)):
    colour_scale.insert(i,(min_housing_benefit_percentage + (i*step)))

#Assign a colour to the normalised house prices
for j in range(0,len(coordinates)):
    housing_benefit_percentage_scale.append([])
    for k in range(0,len(colour_scale)):
        if (colour_scale[k] >= (housing_benefit_percentage[j])):
            housing_benefit_percentage_scale.insert(j,colour[k])
            price_plot.insert(j,colour_plot[k])
            break
    #Add price and colour to the polygons
    #pol[j].description = statxplore_api.get_housing_benefit_date('table', ward_codes[h]) + ": " + str(housing_benefit_percentage[j])[0:4] + "% of people claim Housing Benefits"
    pol[j].style.polystyle.color = housing_benefit_percentage_scale[j]
    
#Save the polygons to a KML file
kml.save(district + "_housing_benefit_percentage" + ".kml")

#Arrange the data for the plot
yaxis_order = sorted(range(len(housing_benefit_percentage)), key=lambda k: housing_benefit_percentage[k])
print(yaxis_order)
yaxis.clear()
xaxis.clear()
colouraxis.clear()
for j in range(0,len(wards[0])):
    a = yaxis_order[j]
    yaxis.insert(j,wards[0][a])
    xaxis.insert(j,housing_benefit_percentage[a])
    colouraxis.insert(j,price_plot[a])

#plot the data
plt.rcParams["figure.figsize"] = (4.5,5)
plt.rcParams["figure.dpi"] = 200
plt.barh(y_pos, xaxis, color= colouraxis, edgecolor='black')
plt.yticks(y_pos,yaxis)
plt.xlabel("Percentage (%)")
plt.title(district + " (" + month + "-" + year + ") \n % of people on Housing Benefits")
plt.savefig(district + "_housing_benefit_claimants_percentage" + ".png", bbox_inches='tight', transparent=True)
plt.clf()

