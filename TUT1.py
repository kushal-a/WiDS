with open("Moons_and_planets.csv",'r') as f:
    entries=f.read().split("\n")
moonsData=[]
for entry in entries:
    moonsData.append(entry.split(","))
moonsData.remove(moonsData[0])

planetData={"Mercury":0,"Venus":0,"Earth":0,"Mars":0,"Jupiter":0,"Saturn":0,"Uranus":0,"Neptune":0,"Pluto":0}
for moon in moonsData:
    moon[2]=float(moon[2])
    if moon[1]=="Mercury":
        planetData["Mercury"]+=1
    elif moon[1]=="Venus":
        planetData["Venus"]+=1
    elif moon[1]=="Earth":
        planetData["Earth"]+=1
    elif moon[1]=="Mars":
        planetData["Mars"]+=1
    elif moon[1]=="Jupiter":
        planetData["Jupiter"]+=1
    elif moon[1]=="Saturn":
        planetData["Saturn"]+=1
    elif moon[1]=="Uranus":
        planetData["Uranus"]+=1
    elif moon[1]=="Neptune":
        planetData["Neptune"]+=1
    elif moon[1]=="Pluto":
        planetData["Pluto"]+=1
sorted_list=sorted(moonsData,key=lambda x: x[2])
out="Number of moons of planets\n--------------------------\nPlanet     No. of moons\n\n"
for i,j in planetData.items():
    out+=f"{i:<16}{j:>4}\n"
out+="\n"
out+="Moons of all planets in order\n-------------------------------\nSatellite      Planet      Diameter\n\n"
for i in sorted_list:
    out+=f"{i[0]:<15}{i[1]:<12}{i[2]:>8}" + "\n"
out.rstrip()
print(out)