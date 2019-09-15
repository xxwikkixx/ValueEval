class Car:
    def __init__(self, id, make, model, year, trim, price, vin, miles, extColor, bodyStyle, doorCount, engineCyl, transmission, driveTrain, fuelType, mpgCity, mpgHighway, seats):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.trim = trim
        self.price = price
        self.vin = vin
        self.miles = miles
        self.extColor = extColor
        self.bodyStyle = bodyStyle
        self.doorCount = doorCount
        self.engineCyl = engineCyl
        self.tranmission = transmission
        self.driveTrain = driveTrain
        self.fuelType = fuelType
        self.mpgCity = mpgCity
        self.mgpHighway = mpgHighway
        self.seats = seats

# Generates a dynamic URL for cars.com
def generateURL(makeId, modelId, perPage, radius, sort, zipCode):
    '''
    :param makeId: MakeID = BMW = 20005
    :param modelId: ModelID = M3 = 21392
    :param perPage: PerPage = 100
    :param radius: Sort = year-newest
    :param sort: ZipCode = 19002
    :param zipCode: Radius = 99999 for max range
    :return: carUrl
    '''
    carUrl = "https://www.cars.com/for-sale/searchresults.action/?dealerType=all&mdId=" \
             + modelId + "&mkId=" + makeId + "&page=1&perPage=" + perPage + "&rd=" \
             + radius + "&searchSource=PAGINATION&sort=" + sort + "&zc=" + zipCode
    return carUrl
