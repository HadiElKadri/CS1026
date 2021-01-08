####AUTHOR: Hadi El-Kadri####
##This class is called CountryCatalogue ##
#Two text files are used to construct a catalogue of countries with their attributes as well as a dictionary#

from country import Country
class CountryCatalogue:
    def __init__(self, countryFile = "", continentFile = ""):

#Creating variables; a list and a dictionary
        self._countryCat = []
        self._cDictionary = {}
#Opening readers to read the text files
        readCountryFile = open(countryFile, 'r')
        readContinentFile = open(continentFile, 'r')

#Constructing a dictionary from the continent file
        for line in readContinentFile:
            newline = line.split(",")
            self._cDictionary[newline[0].title()] = newline[1].strip()

            if "Country" in self._cDictionary:
                self._cDictionary.pop("Country") #to disregard the first line


#Constructing a catalog of country objects from the data file
        firstline = True
        for line in readCountryFile:
            newline = line.split("|")

            if not firstline: #to disregard the first line
                newcountry = Country(newline[0], int(removePunctuation(newline[1])), float(removePunctuation(newline[2])), self._cDictionary[newline[0].title()])
                self._countryCat.append(newcountry)
            firstline = False
#Closing the file readers
        readCountryFile.close()
        readContinentFile.close()
#GETTER/ACCESSOR#
#Returns the list of country objects known as the catalogue
    def getCat(self):
        return self._countryCat

#GETTER/ACCESSOR#
#Returns an inputted country's country object from the catalogue
    def findCountry(self, countryName = ""):
        for i in range(len(self._countryCat)):
            if self._countryCat[i].getName().lower() == countryName.lower():
                country = self._countryCat[i]
                return country

#SETTER/MUTATOR#
#Allows the user to set the population of a desired country to anything they want
    def setPopulationOfCountry(self, countryName= "", newPopulation = 0):
        if self.findCountry(countryName) is None:
            return False
        self.findCountry(countryName).setPopulation(newPopulation)
        return True

#SETTER/MUTATOR#
#Allows the user to set the area of a desired country to whatever they want
    def setAreaOfCountry(self, countryName = "", newArea = 0):
        if self.findCountry(countryName) is None:
            return False
        self.findCountry(countryName).setArea(newArea)
        return True

#SETTER/MUTATOR#
#Allows the user to create a new country object with attributes and add it into the catalogue and dictionary
    def addCountry(self, newName = "", newPop = 0, newArea = 0.0, newContinent = ""):
        if self.findCountry(newName) is None:
            newName = newName.title()
            newContinent = newContinent.title()
            newCountry = Country(newName, newPop, newArea, newContinent)
            self._countryCat.append(newCountry)
            self._cDictionary[newName] = newContinent
            return True
        else:
            return False

#SETTER/MUTATOR#
#Allows a user to delete a desired country from the catalogue and dictionary
    def deleteCountry(self, countryName = ""):
        countryName = countryName.title()
        for object in self._countryCat:
            if countryName == object.getName().title():
                self._countryCat.remove(object)
                self._cDictionary.pop(countryName)

#GETTER/ACCESSOR#
#Prints out the catalogue of country objects
    def printCountryCatalogue(self):
        print(self._countryCat)

#GETTER/ACCESSOR#
#Returns a list of countries associated with an inputted continent
    def getCountriesByContinent(self, continent = ""):
        continent = continent.title()
        listofcountries = []
        for i in range(len(self._countryCat)):
            if self._countryCat[i].getContinent() == continent:
                listofcountries.append(self._countryCat[i])
        return listofcountries

#GETTER/ACCESSOR#
#Returns a list of countries associated with an inputted continent and their populations in descending order
    def getCountriesByPopulation(self, continent = ""):
        continent = continent.title()
        listofcountries = []
#If no continent is given, a list of ALL countries with their populations in descending order will be returned
        if continent == "":
            for i in range (len(self._countryCat)):
                 country = self._countryCat[i].getName()
                 population = self._countryCat[i].getPopulation()
                 tuple = country, population
                 listofcountries.append(tuple)
            listofcountries.sort(key= lambda x: x[1], reverse = True)
            return listofcountries
#If a continent is given, a list of countries associated with an inputted continent and their populations in descending order
        else:
            for i in range (len(self._countryCat)):
                if continent == self._countryCat[i].getContinent():
                    country = self._countryCat[i].getName()
                    population = self._countryCat[i].getPopulation()
                    tuple = country, population
                    listofcountries.append(tuple)
            listofcountries.sort(key= lambda x: x[1], reverse = True)
            return listofcountries

#GETTER/ACCESSOR#
#Returns a list of countries associated with an inputted continent and their areas in descending order
    def getCountriesByArea(self, continent = ""):
        continent = continent.title()
        listofcountries = []
        if continent == "":

#If no continent is given, a list of ALL countries with their areas in descending order will be returned
            for i in range (len(self._countryCat)):
                 country = self._countryCat[i].getName()
                 area = self._countryCat[i].getArea()
                 tuple = country, area
                 listofcountries.append(tuple)
            listofcountries.sort(key= lambda x: x[1], reverse = True)
            return listofcountries

#If a continent is given, a list of countries associated with an inputted continent and their areas in descending order
        else:
            for i in range (len(self._countryCat)):
                if continent == self._countryCat[i].getContinent():
                    country = self._countryCat[i].getName()
                    area = self._countryCat[i].getArea()
                    tuple = country, area
                    listofcountries.append(tuple)
            listofcountries.sort(key= lambda x: x[1], reverse = True)
            return listofcountries

#GETTER/ACCESSOR#
#This method finds the country with the biggest population and returns the country name with its population
    def findMostPopulousContinent(self):
        listofcontinents = []
        listofpopulations= []

        for i in range (len(self._countryCat)):
            if self._countryCat[i].getContinent() not in listofcontinents:
                listofcontinents.append(self._countryCat[i].getContinent())

        for i in range (len(listofcontinents)):
            population = 0
            countries = self.getCountriesByContinent(listofcontinents[i])
            for j in range(len(countries)):
                population = population + countries[j].getPopulation()
                tuple = listofcontinents[i], population
                listofpopulations.append(tuple)

        listofpopulations.sort(key= lambda x: x[1], reverse = True)

        return listofpopulations[0]

#GETTER/ACCESSOR#
#This method returns population densities of countries whose densities fall inbetween the given parameters
    def filterCountriesByPopDensity(self, lowerbound = 0.0, upperbound = 0.0):
        popdensities = []
        max = 0
        min = 0

        if lowerbound == upperbound:
            for i in range (len(self._countryCat)):
                if self._countryCat[i].getPopDensity() == lowerbound:
                    tuple = self._countryCat[i].getName(), self._countryCat[i].getPopDensity()
                    popdensities.append(tuple)

        elif lowerbound < upperbound:
            min = lowerbound
            max = upperbound

        elif upperbound < lowerbound:
            min = upperbound
            max = lowerbound

        for i in range (len(self._countryCat)):
            if min <= self._countryCat[i].getPopDensity() <= max:
                tuple = self._countryCat[i].getName(), self._countryCat[i].getPopDensity()
                popdensities.append(tuple)

        popdensities.sort(key= lambda x: x[1], reverse = True)

        return popdensities

#SETTER/MUTATOR#
#This method allows the user to write and save the country catalogue created into a file
    def saveCountryCatalogue(self, file = ""):
        sortcat = sorted(self._countryCat, key= lambda country: country.getName())
        count = 0
        writefile = open(str(file), "w")
        done = False

        while not done:
            for i in range (len(sortcat)):
                writefile.write(sortcat[i].getName() + "|" + sortcat[i].getContinent() + "|" + str(sortcat[i].getPopulation()) + "|" + "%.2f" % (sortcat[i].getArea()) + "|" + "%.2f" % ((sortcat[i].getPopDensity())) + "\n")

                count = count + 1
                if i == len(sortcat)- 1:
                    done = True

        writefile.close()
        if done:
            return count
        else:
            return -1

#This function is not in the class but is needed to remove unnecessary punctuation
def removePunctuation(string):
    punctuations = ','
    no_punct = ""
    for i in range(0,len(string)):
       if string[i] not in punctuations:
        no_punct = no_punct + string[i]
    return no_punct
