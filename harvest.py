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
    
    
    Muskmelon = MelonType('musk', '1998', 'green', True, True, 'Muskmelon')
    Muskmelon.add_pairing("mint")    
    Muskmelon.update_code("musk001")
    all_melon_types.append(Muskmelon)

    Casaba = MelonType('cas', '2003', 'orange', False, False, 'Casaba')
    Casaba.add_pairing("strawberries")
    Casaba.add_pairing("mint")
    Casaba.update_code("cas001")
    all_melon_types.append(Casaba)
    
    Crenshaw = MelonType('cren', '1996', 'green', False, False, 'Crenshaw')
    Crenshaw.add_pairing("proscuitto")
    Crenshaw.update_code("cren001")
    all_melon_types.append(Crenshaw)

    Yellow_Watermelon = MelonType('yw', '2013', 'yellow', False, True, 'Yellow Watermelon')
    Yellow_Watermelon.add_pairing("ice cream")
    Yellow_Watermelon.update_code('yw001')
    all_melon_types.append(Yellow_Watermelon)

    # for melon in all_melon_types:
    #     print(melon.code)
    #     print(melon.name)
    #     print(melon.pairings)
    #     print(melon.first_harvest)


    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    melon_types = make_melon_types()

    for melon in melon_types:
        print(f"{melon.name} is paired with {melon.pairings}")


    

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # Fill in the rest



if __name__ == "__main__":
    make_melon_types()   


    

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



