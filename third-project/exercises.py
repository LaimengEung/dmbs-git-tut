# List down 3 more built-in methods
l = []

l.count('') # count total elements of list
l.sort() # sort the list
l.reverse() # reverse the list

# List down 3 more built-in methods for dictionaries
d = {}
d2 = {}

d.get('') # returns the value of the specified 'key'
d.setdefault('') # setting a default value for a dictionary key if it doesn't exist; if no default value is provided, it defaults to None
d.update(d2) # updates the dictionary with elements from d2 dict

    # Example:      # dict1 = {'a': 1, 'b': 2}
                    # dict2 = {'b': 3, 'c': 4}
                    # dict1.update(dict2)
                    # dict1 is {'a': 1, 'b': 3, 'c': 4}
                    
TEMPERATURES = [28, 32, 25, 30, 35, 29, 31]

def temp_filter(temperature):
    return [temp for temp in temperature if temp > 30]

def temp_filter_recursive(temperature, index=0):
    if index == len(temperature):
        return []
    
    if temperature[index] > 30:
        return [temperature[index]] + temp_filter_recursive(temperature, index + 1)
    else:
        return temp_filter_recursive(temperature, index + 1)

COLORS =  ["red", "blue", "red", "green", "blue", "red", "yellow"]

color_dict = {}

def count_color(color_list, color_dict):
    for color in color_list:
        if color not in color_dict:
            color_dict[color] = 1
        else:
            color_dict[color] += 1

    return color_dict

def count_color_2(color_list): # use collections more efficient!
    color_dict = {}
    color_set = (color_list)
    for color in color_set:
        color_dict[color] = 1
        color_dict[color] = color_list.count(color)
    
    return color_dict

USERS = [
    { 'name': "Alex", 'age': 28, 'status': "active" },
    { 'name': "Ben", 'age': 19, 'status': "inactive" },
    { 'name': "Chloe", 'age': 35, 'status': "active" },
    { 'name': "Dana", 'age': 22, 'status': "inactive" },
    { 'name': "Ethan", 'age': 40, 'status': "active" },
]

def calc_user_age(users):
    total_users_age = 0
    for user in users:
        if user['status'] == 'active':
            total_users_age += user.get('age')

    return total_users_age

def calc_user_age_2(users):
    total_users_age = sum([user.get('age') for user in users if user['status'] == 'active'])
    return total_users_age
    
INVENTORY = [
    { 'id': 101, 'name': "Laptop Stand", 'price': 45.00 },
    { 'id': 202, 'name': "Wireless Mouse", 'price': 25.50 },
    { 'id': 303, 'name': "Mechanical Keyboard", 'price': 120.00 },
]
SHOPPING_CART = [202, 101, 202]

def new_cart(inventory, shop_cart):
    new_cart = []
    for cart in shop_cart:
        for i in inventory:
            if i['id'] == cart:
                new_cart.append(i.get('price'))
    
    return new_cart

def new_cart_2(inventory, shop_cart):
    def get_price(cart):
        for i in inventory:
            if i['id'] == cart:
                return i['price']
    # return map(get_price, shop_cart)
    return list(map(get_price, shop_cart)) # map(function, iterable) returns an iterator that yields the results (according to the order of the iterable); (iterable can be list, tuple, or set)
                                           # There's no loop involved!

    # Example:      # list1 = [1, 2, 3]
                    # list2 = [4, 5, 6]

                    # def add_together(a, b):
                    #     return a + b

                    # sum_list = list(map(add_together, list1, list2))
                    #                                          
print(temp_filter_recursive(TEMPERATURES))

print(count_color_2(COLORS))

print(calc_user_age_2(USERS))

print(new_cart_2(INVENTORY, SHOPPING_CART))


# Check out collections library! Prof recommend this.