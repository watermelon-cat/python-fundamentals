import folium
from folium import plugins
import webbrowser

b = folium.Map()

bus_path = [
    [39.771860, -104.949955],
    [39.780750, -104.949520],
    [39.780170, -104.967124],
    [39.779697, -104.977129],
    [39.779992, -104.985776],
    [39.780775, -104.988612],
    [39.780517, -104.989894],
    [39.779902, -104.990484],
    [39.778866, -104.990411],
    [39.777322, -104.989773],
    [39.776070, -104.989778],
    [39.774435, -104.990233],
    [39.771432, -104.990998],
    [39.769483, -104.992839],
    [39.766305, -104.999817],
    [39.757600, -105.009910],
    [39.756357, -105.015781],
    [39.754924, -105.015827],
    [39.754873, -105.023564],
    [39.755459, -105.023597]
]
folium.plugins.AntPath(
    locations=bus_path, reverse="True", dash_array=[20,30]           
).add_to(b)

b.fit_bounds(b.get_bounds())

b.save("map.html")

# userInput = input("Do you want to see CEC (\"c\") or the Denver Zoo (\"z\").")

# c = folium.Map(location=[39.75564177867975, -105.0226102413041], zoom_start=20)
# folium.Marker([39.75564177867975, -105.0226102413041], popup="CEC").add_to(c)

# z = folium.Map(location=[39.749126876210546,-104.95075052139737], zoom_start=17)
# folium.Marker([39.749126876210546, -104.95075052139737], popup="ZOO").add_to(z)

# if userInput == "c":
#     c.save("map.html")
# elif userInput == "z":
#     z.save("map.html")
# else:
#     print("That's not an option")
webbrowser.open("map.html")   # Automatically opens map in default browser
