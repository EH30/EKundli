from datetime import datetime
from SiderealKundliCraft import chart, SiderealAstroData


class DataHouse:
    def __init__(self):
        self.sign_num         = None
        self.is_ascendant     = False
        self.asc_signlon      = None
        self.asc_minute       = None
        self.asc_second       = None
        self.asc_degree       = None
        self.planets          = {}

class AstroCharts:
    def __init__(self, planetData:SiderealAstroData.AstroData, latitude:float, longitude:float, utc:list):
        self.latitude  = latitude
        self.longitude = longitude
        self.utc  = utc
        self.data = planetData
        self.navamasa_mfd = {
            "move": [1,4,7,10],
            "fixed": [2,5,8,11],
            "dual": [3,6,9,12]
        }
        self.navamasa_degree = [
            [ 0,   3.20, 6.4, 10  , 13.20, 16.40, 20  ,  23.20, 26.40 ],
            [ 3.20, 6.40, 10,  13.20, 16.40, 20  , 23.20,  26.40, 30   ]
        ]

    
    def lagnaChart(self) -> list[DataHouse]:
        data = chart.Chart(self.data.planets_rashi())
        return data.lagnaChart()
    
    def moonChart(self) -> list[DataHouse]:
        data = chart.Chart(self.data.planets_rashi())
        return data.moonChart()
    
    def transitKundli(self) -> list[DataHouse]:
        tdata = SiderealAstroData.AstroData(
            int(datetime.now().strftime("%Y")), int(datetime.now().strftime("%m")),int(datetime.now().strftime("%d")), int(datetime.now().strftime("%H")), 
            int(datetime.now().strftime("%M")), 0, int(self.utc[0]), int(self.utc[1]), self.latitude, self.longitude)
        houses = []
        lagna_chart   = self.lagnaChart() 
        current_chart = chart.Chart(tdata.planets_rashi()).lagnaChart()
        
        for i in range(len(lagna_chart)):
            temp = DataHouse()
            temp.sign_num = lagna_chart[i].sign_num
            houses.append(temp)
        
        for i in range(len(current_chart)):
            if current_chart[i].is_ascendant:
                for x in range(len(houses)):
                    if houses[x].sign_num == current_chart[i].sign_num:
                        houses[x].is_ascendant = True
                        houses[x].asc_signlon  = current_chart[i].asc_signlon
                        houses[x].asc_minute   = current_chart[i].asc_minute
                        houses[x].asc_second   = current_chart[i].asc_second
                        houses[x].asc_degree   = chart.Chart.degree_minute_second_st(None, current_chart[i].asc_signlon, current_chart[i].asc_minute, current_chart[i].asc_second)
                        
            
            if len(current_chart[i].planets) != 0:
                for x in range(len(houses)):
                    if houses[x].sign_num == current_chart[i].sign_num:
                        houses[x].planets = current_chart[i].planets 
        return houses
    
    def get_start_count(self, sign_num, pos, current_house):
        if sign_num in self.navamasa_mfd["move"]:
            start_house = current_house
            for i in range(len(self.navamasa_degree[0])):
                if pos >= self.navamasa_degree[0][i] and pos <= self.navamasa_degree[1][i]:
                    house_to_count = i+1
                    return [start_house+1, house_to_count]
        elif sign_num in self.navamasa_mfd["fixed"]:
            start_house = 9+current_house if 9+current_house <= 12 else 9+current_house-12 
            for i in range(len(self.navamasa_degree[0])):
                if pos >= self.navamasa_degree[0][i] and pos <= self.navamasa_degree[1][i]:
                    house_to_count = i+1
                    return [start_house, house_to_count]
        elif sign_num in self.navamasa_mfd["dual"]:
            start_house = 5+current_house if 5+current_house <= 12 else 5+current_house-12
            for i in range(len(self.navamasa_degree[0])):
                if pos >= self.navamasa_degree[0][i] and pos <= self.navamasa_degree[1][i]:
                    house_to_count= i+1
                    return [start_house, house_to_count]
    

    def navamsaChart(self, lagnaKundli):
        asc = [lagnaKundli[0].sign_num, float(str(lagnaKundli[0].asc_degree.split(":")[0])+"."+str(lagnaKundli[0].asc_degree.split(":")[0]))]
        houses = []

        count_house = self.get_start_count(asc[0], asc[1], 0)
        temp = count_house[0]-1
        for _ in range(count_house[1]):
            temp += 1
            if temp > 12:
                temp = 1
        
        for i in range(0, 12):
            temp_a = DataHouse()
            temp_a.sign_num = lagnaKundli[temp-1].sign_num
            temp_a.planets  = []
            houses.append(temp_a)
            temp += 1
            if temp > 12:
                temp = temp-12
        
        for house in range(len(lagnaKundli)):
            if len(lagnaKundli[house].planets) != 0:
                for item in lagnaKundli[house].planets:
                    pos =  float(str(lagnaKundli[house].planets[item]["degree"].split(":")[0])+"."+str(lagnaKundli[house].planets[item]["degree"].split(":")[1] ))
                    count_house = self.get_start_count(lagnaKundli[house].sign_num, pos, int(house))
                    temp = count_house[0]-1
                    for _ in range(count_house[1]):
                        temp += 1
                        if temp > 12:
                            temp = 1
                    
                    rashi = lagnaKundli[temp-1].sign_num
                    for i in range(len(houses)):
                        if houses[i].sign_num == rashi:
                            houses[i].planets.append(item)
        return houses
