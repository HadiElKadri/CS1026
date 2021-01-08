#####Author: Hadi El-Kadri#####
##This class is called Country and contructs a country object
class Country:
#CONSTRUCTOR
    def __init__(self, name="", population= 0, area = 0.0, continent = ""):
        self._name = name
        self._population = population
        self._area = area
        self._continent = continent

#GETTERS
    def getName(self):
        return self._name

    def getPopulation(self):
        return self._population

    def getArea(self):
        return self._area

    def getContinent(self):
        return self._continent

    def getPopDensity(self):
        return round(self._population / self._area, 2)

#SETTERS
    def setPopulation(self, newpopulation):
        self._population = newpopulation

    def setArea(self, newarea):
        self._area = newarea

    def setContinent(self, newcontinent):
        self._continent = newcontinent

#REPRESNTING THE OBJECT AS A STRING
    def __repr__(self):
        return self._name + "(Pop: " + str(self._population) + ", Size: " + str(self._area) + ") in " + self._continent
