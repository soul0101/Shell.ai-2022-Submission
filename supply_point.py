class SupplyPoint():
    def __init__(self, index, x, y, total_parking_slots, existing_num_SCS, existing_num_FCS):
        self.index = index
        self.x = x
        self.y = y
        self.total_parking_slots = total_parking_slots
        self.existing_num_SCS = existing_num_SCS
        self.existing_num_FCS = existing_num_FCS
        # self.max_supply = self.calculate_max_supply(self.existing_num_SCS, self.existing_num_FCS)
        
    # def calculate_max_supply(self, num_SCS, num_FCS):
    #     return num_SCS * 200 +  num_FCS * 400 
