from catalogue import *

def testFindCountry(countryCatalog):
    print()
    print("Looking up country")
    cntry = input("-- Enter name of country: ")
    cntry = cntry.strip()
    cntryObj = countryCatalog.findCountry(cntry)
    if cntryObj is None:
        print("-- Country not found in list")
    else:
        print(cntryObj)

def testSetPopulationOfCountry(countryCatalog):
    print()
    print("Setting population of country")
    itemFound = False
    cntry = input("-- Enter name of country: ")
    cntry = cntry.strip()
    cPop = input("  --  Enter new population: ")
    cPop = cPop.strip()
    cPop = float(cPop.replace(",",""))
    itemFound = countryCatalog.setPopulationOfCountry(cntry,cPop)
    if not itemFound:
        print("  Country " + cntry + " is not in the current list")

def testSetAreaOfCountry(countryCatalog):
    print()
    print("Setting area(size) of country")
    itemFound = False
    cntry = input("-- Enter name of country: ")
    cntry = cntry.strip()
    cSz = input("  --  Enter new area: ")
    cSz = cSz.strip()
    cSz = float(cSz.replace(",",""))
    itemFound = countryCatalog.setAreaOfCountry(cntry,cSz)
    if not itemFound:
        print("  Country " + cntry + " is not in the current list")

def testAddCountry(countryCatalog):
    print()
    cntry = input("-- Enter name of country to add: ")
    cntry = cntry.strip()
    thePop = input("      Enter the population: ")
    thePop = thePop.strip()
    cPop = float(thePop.replace(",",""))
    theSz = input("      Enter the size(area): ")
    theSz = theSz.strip()
    cSz = float(theSz.replace(",",""))
    theCont = input("      Enter the continent: ")
    theCont = theCont.strip()
    itemFound = countryCatalog.addCountry(cntry,cPop,cSz,theCont)
    if not itemFound:
        print("  Country " + cntry + " is already in the current list")

def testDeleteCountry(countryCatalog):
    print()
    cntry = input("-- Enter name of country to delete: ")
    cntry = cntry.strip()
    countryCatalog.deleteCountry(cntry)

def testGetCountriesByContinent(countryCatalog,theCont):
    lst = countryCatalog.getCountriesByContinent(theCont)
    if len(lst) > 0:
        print()
        print("Countries in "+theCont+" are:")
        for cobj in lst:
            print(cobj)

def testGetCountriesByArea(countryCatalog,theCont):
    lst = countryCatalog.getCountriesByArea(theCont)
    if len(lst) > 0:
        print()
        if theCont == "":
            print("Countries by size are:")
        else:
            print("Countries in "+theCont+" by size are:")
        for ac in lst:
            print(ac[0],ac[1])

def testGetCountriesByPopulation(countryCatalog,theCont):
     alst = countryCatalog.getCountriesByPopulation(theCont)
     if len(alst) > 0:
        print()
        if theCont == "":
            print("Countries by population are:")
        else:
            print("Countries in "+theCont+" by population are:")
        for ac in alst:
            print(ac[0],ac[1])

def testFindMostPopulousContinent(countryCatalog):
    rslt = countryCatalog.findMostPopulousContinent()
    print()
    print("The most populous continent is "+ rslt[0] + " with a population of " + str(rslt[1]))

def testFilterCountriesByPopDensity(countryCatalog):
    print()
    lb = input("-- Enter the lower bound for population density: ")
    lb = float(lb.strip())
    ub = input("-- Enter the upper bound for population density: ")
    ub = float(ub.strip())
    rlst = countryCatalog.filterCountriesByPopDensity(lb,ub)
    if len(rlst) == 0:
        print("  No countries with density in that range found.")
    else:
        print("  Countries with density in this range are:")
        for ac in rlst:
            print(ac[0] + ", " + "density = "+ str(ac[1]))

def testSaveCountryCatalogue(cc,fname):
    print()
    print("Saving Country Catalogue")
    nitems = cc.saveCountryCatalogue(fname)
    print(" "+str(nitems)+" items written to file "+fname)


def main():
    cc = CountryCatalogue('data.txt','continent.txt')
    # print initial catalogue
    cc.printCountryCatalogue()
    # find a country
    testFindCountry(cc)
    # add a country, delete a country, print the new catalogue and find a country in the new catalogue
    testAddCountry(cc)
    testDeleteCountry(cc)
    cc.printCountryCatalogue()
    testFindCountry(cc)
    # set the area and population
    testSetAreaOfCountry(cc)
    testSetPopulationOfCountry(cc)
    # print various parts of the catalogue
    testGetCountriesByContinent(cc,"Europe")
    testGetCountriesByArea(cc,"Europe")
    testGetCountriesByArea(cc,"")
    testGetCountriesByPopulation(cc,"Europe")   # prints countries in Europe
    testGetCountriesByPopulation(cc,"")        # prints all countries
    # test filters
    testFindMostPopulousContinent(cc)
    testFilterCountriesByPopDensity(cc)
    # print final catalogue and then output it to a file
    cc.printCountryCatalogue()
    testSaveCountryCatalogue(cc,'output.txt')

main()
