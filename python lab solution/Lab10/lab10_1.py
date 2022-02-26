class Vehicle:
    def __init__(self, model_year: int, total_mileage: int, VIN: str, EPAclass, EPAmileage, engine, transmission, options, fuel, kms_per_liter):
        self.model_year = model_year
        self.total_mileage = total_mileage
        self.VIN = VIN
        self.EPAclass = EPAclass
        self.EPAmileage = EPAmileage
        self.engine = engine
        self.transmission = transmission
        self.options = options
        self.fuel = fuel
        self.kms_per_liter = kms_per_liter

    def __str__(self):
        result = "Model year {} \n".format(self.model_year)
        result += "Total Mileage {} \n".format(self.total_mileage)
        # add all the other atrributes to the string
        return result

    def drive_kms(self, kms):
        try:
            kms = float(kms)
        except ValueError:
            print ("Kms not well formatted")
            return

        self.fuel -= kms / self.kms_per_liter
        print ("Vehicle has now {} litres of gasoline".format(self.fuel))

class Truck(Vehicle):

    def __init__(self, model_year, total_mileage, VIN, EPAclass, EPAmileage, engine, transmission, options, fuel, maximum_seating, cabin_size):
        Vehicle.__init__(model_year, total_mileage, VIN, EPAclass, EPAmileage, engine, transmission, options, fuel)
        self.maximum_seating = maximum_seating
        self.cabin_size = cabin_size # kgs
        self.current_load = 0

    def __str__(self):
        result_str = Vehicle.__str__(self)
        result_str += " {} maximum seating and {} cabin size".format(self.maximum_seating, self.cabin_size)

    def add_package(self, kgs):

        try:
            kms = float(kgs)
        except ValueError:
            print ("Kgs not well formatted")
            return

        if self.current_load + kgs <= self.cabin_size:
            self.current_load += kgs
        else:
            print("Cabin size can not handle this package")
            return
