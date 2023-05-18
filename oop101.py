class Company():
    #Init functiion for object initialisation
    def __init__(self, c_name, c_address):
        self.name = c_name
        self.address = c_address

    def payment(self):
        print("payment Done by", self.name)

    def shipment(self):
        print("product reached at", self.address)

#make one object
c1 = Company('simform', 'binori B')
c1.payment()
c1.shipment()
