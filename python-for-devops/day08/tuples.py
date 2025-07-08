# Basic
ebs_volume_tuple = ("uiux", "cache", "logs", "staticweb")
print(ebs_volume_tuple)

# tuple indexing
print(ebs_volume_tuple[2])

# tuple length
tuple_length = len(ebs_volume_tuple)
print(tuple_length)

# tuple pack and unpack
coordinates = (3, 4)
x, y = coordinates
print(coordinates)

# tuple concate
concate_tuple = ("apple", "cherry", "orange", "mango")
new_cat_tuple = concate_tuple + ("------",) + ("pineapple",)
print(new_cat_tuple)

#tuple checking for element
dry_fruits_tuple = ("dates", "almond", "pistachio", "wallnut")
fav_dry_fuits = "dates" in dry_fruits_tuple
print(fav_dry_fuits)

# tuples for multiple returns
def get_coordinates():
    return(3, 4)

x, y = get_coordinates()

# The append, remove and ordering is practiced in lists.