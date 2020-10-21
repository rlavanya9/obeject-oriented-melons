############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

        # print(self.name)
        # Fill in the rest
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
    
        self.pairings.append(pairing)
        # print(self.pairings)
        return self.pairings



    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code
        # print(self.code) #for checking
        return self.code
        

def make_melon_types():
    """Returns a list of current melon types."""
    
    all_melon_types = []
    test_list = []
    
    
    Muskmelon = MelonType('musk', '1998', 'green', True, True, 'Muskmelon')
    Muskmelon.add_pairing("mint")    
    Muskmelon.update_code("musk")
    all_melon_types.append(Muskmelon)

    Casaba = MelonType('cas', '2003', 'orange', False, False, 'Casaba')
    Casaba.add_pairing("strawberries")
    Casaba.add_pairing("mint")
    Casaba.update_code("cas")
    all_melon_types.append(Casaba)
    
    Crenshaw = MelonType('cren', '1996', 'green', False, False, 'Crenshaw')
    Crenshaw.add_pairing("proscuitto")
    Crenshaw.update_code("cren")
    all_melon_types.append(Crenshaw)

    Yellow_Watermelon = MelonType('yw', '2013', 'yellow', False, True, 'Yellow Watermelon')
    Yellow_Watermelon.add_pairing("ice cream")
    Yellow_Watermelon.update_code('yw')
    all_melon_types.append(Yellow_Watermelon)

    # for melon in all_melon_types:
    #     test_list.append(melon.code)
    #     test_list.append(melon.first_harvest)
    #     test_list.append(melon.color)
    #     test_list.append(melon.pairings)
    #     test_list.append(melon.is_seedless)
    #     test_list.append(melon.is_bestseller)
    #     test_list.append(melon.name)
    # print(test_list)
       
       


    return all_melon_types
    # return test_list

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    print(melon_types)

    for melon in melon_types:
        print(f"{melon.name} is paired with {melon.pairings}")



    

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # Fill in the rest
    melon_type_dict = {}
    melon_types = make_melon_types()

    for melon in melon_types:
        melon_type_dict[melon.code] = melon
        
    
    return melon_type_dict




if __name__ == "__main__":
    # make_melon_types()   
    melon_types = make_melon_types()
    print_pairing_info(melon_types)
    make_melon_type_lookup(melon_types)


    

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, name, melon_type, shape_rating, color_rating, field, harvested_by):
        self.name = name
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by
    
    # def is_sellable(self, shape_rating, color_rating, field):
    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            print("is_Sellable section")
            return True
            
        return False



def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons = []

    melon_id = make_melon_type_lookup(melon_types)
    melon1 = Melon('Melon 1', melon_id['yw'], 8, 7, 2, "Shiela")
  

    melon9 = Melon('Melon 9', 'yw', 7, 10, 3, "Michael")

    melons.extend([melon1, melon9])

 
    
    return melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    for melon in melons:
        if melon.is_Sellable():
            status = 'CAN BE SOLD'
        else:
            status = "NOT SELLABLE"
        print(f"Harvested by {melon.hervested_by} from {melon.field} {status}")



if __name__ == "__main__":

     melon_types = make_melon_types()
     make_melons(melon_types)
    



