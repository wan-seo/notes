class UndergroundSystem:

    def __init__(self):
        self.travels = {}
        self.checkIns = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (t, stationName)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        check_in_at, check_in_station_name = self.checkIns.pop(id)
        time_taken = t - check_in_at
        route = (check_in_station_name, stationName)
        time, count = self.travels.get(route, (0, 0))
        self.travels[route] = (time_taken + time, count + 1)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation,)
        time, count = self.travels[route]
        return time / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)