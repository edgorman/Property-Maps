import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors

fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

plt.rcParams["figure.figsize"] = (9,9)


y = np.array([10, 10, 25, 25, 30])
mylabels = ["Burglary", "Flooding", "Universal Credit", "Housing benefit", "Schools"]
mylabels_factor = ["Risk", "Risk", "Push", "Push", "Pull"]
myexplode = [0.2, 0.2, 0, 0.1, 0]
mycolors = ["#FF0014", "#1478F0", "#F07800", "#B478FF", "#006400"]
textprops = {"fontsize":16}

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, colors = mycolors, textprops =textprops, autopct = "%0.2f%%",startangle = 0)
plt.legend( labels = mylabels_factor,
            title='Desirability Factor',
            title_fontsize=16,
            loc="lower center",
            bbox_to_anchor=(0.4,-0.1),
            framealpha=0,
            ncol = 5,
            fontsize=16)

#plot the data
#plt.rcParams["figure.dpi"] = 200
#plt.rcParams["figure.figsize"] = (10,10)
plt.title("Desirability Weighting with Burglary data", loc="center", fontsize=18)
plt.savefig("desirability_weighting_with_burglary" + ".png", bbox_inches='tight', transparent=True)
plt.close()
    

y2 = np.array([12.5, 27.5, 27.5, 32.5])
mylabels2 = ["Flooding", "Universal Credit", "Housing benefit", "Schools"]
mylabels_factor2 = ["Risk", "Push", "Push", "Pull"]
myexplode2 = [0.2, 0, 0.1, 0]
mycolors2 = ["#1478F0", "#F07800", "#B478FF", "#006400"]
textprops2 = {"fontsize":16}

plt.pie(y2, labels = mylabels2, explode = myexplode2, shadow = True, colors = mycolors2, textprops =textprops2, autopct = "%0.2f%%", startangle = 0)
plt.legend( labels = mylabels_factor2,
            title='Desirability Factor',
            title_fontsize=16,
            loc="lower center",
            bbox_to_anchor=(0.4,-0.1),
            framealpha=0,
            ncol = 5,
            fontsize=16)

#plot the data
#plt.rcParams["figure.dpi"] = 200
#plt.rcParams["figure.figsize"] = (10,10)
plt.title("Desirability Weighting without Burglary data", loc="center", fontsize=18)
plt.savefig("desirability_weighting_without_burglary" + ".png", bbox_inches='tight', transparent=True)
plt.close()






y = np.array([10, 10, 25, 25, 30])
mylabels = ["Burglary", "Flooding", "Universal Credit", "Housing benefit", "Schools"]
mylabels_factor = ["Risk", "Risk", "Push", "Push", "Pull"]
myexplode = [0.2, 0.2, 0, 0.1, 0]
mycolors = ["#FF0014", "#1478F0", "#F07800", "#B478FF", "#006400"]
textprops = {"fontsize":16}

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, colors = mycolors, textprops =textprops, autopct = "%0.2f%%",startangle = 0)
plt.legend( labels = mylabels_factor,
            title='Desirability Factor',
            title_fontsize=16,
            loc="lower center",
            bbox_to_anchor=(0.4,-0.1),
            framealpha=0,
            ncol = 5,
            fontsize=16)

#plot the data
#plt.rcParams["figure.dpi"] = 200
#plt.rcParams["figure.figsize"] = (10,10)
plt.title("Desirability Weighting with Burglary data", loc="center", fontsize=18)
plt.savefig("desirability_weighting_with_burglary" + ".png", bbox_inches='tight', transparent=True)
plt.close()




#plot the scatter
plt.rcParams["figure.figsize"] = (3.5,3)
x = np.array([0.2,0.7,1])
y = np.array([350000,240000,180000])
colors = np.array(["red","green","blue"])
#text_labels = np.array(["Ward A","Ward B","Ward C"])

for xp, yp, c in zip(x, y, colors):
   plt.scatter(xp, yp, s=800, c=c)

#plt.rcParams["figure.figsize"] = (3.5,3)
plt.title("Property Price vs. Location Desirability", fontsize=16)
plt.ylabel("Property Price (£)", fontsize=16)
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.locator_params(axis='y', nbins=3)
plt.xlabel( "Location Desirability" , fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

plt.legend( labels = ["Ward A","Ward B","Ward C"],
            title='Wards',
            title_fontsize=16,
            loc="upper right",
            bbox_to_anchor=(1.8,1),
            framealpha=0,
            ncol = 1,
            labelspacing = 1.2,
            fontsize=16)


plt.savefig("_scatter_generic" + ".png", bbox_inches='tight', transparent=True)
plt.close()



