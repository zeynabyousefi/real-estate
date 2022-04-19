import re
import pandas as pd


class Address:

    def __init__(self, city_name, street_name, number_plaque, number_postal_code):
        self.city = city_name
        self.street = street_name
        self.number_plaque = number_plaque
        self.number_postal_code = number_postal_code

    def change_to_dict(self):
        dict_info_Adress = vars(self)
        return dict_info_Adress

    def Edit(self):
        dict_info_Adress = Address.change_to_dict(self)
        list_of_key_edit = []
        list_of_value_edit = []
        number_of_edit = int(input('How many do you want to change?'))
        for i in range(number_of_edit):
            print("city\t\tstreet\t\tnumber_plaque\t\tnumber_postal_code")
            key = input("Enter the attribute you want to change:")
            if key in dict_info_Adress.keys():
                list_of_key_edit.append(key)
            else:
                print("The key not found!")
        for j in range(len(list_of_key_edit)):
            value = input(f"Enter the value of {list_of_key_edit[j]} you want to change:")
            list_of_value_edit.append(value)
            dict_info_Adress.update({list_of_key_edit[j]: list_of_value_edit[j]})

    def show_info(self):

        for k, v in Address.change_to_dict(self).items():
            print(k, '=', v, end=" , ")
        else:
            print('\n')


class Person:

    def __init__(self, firstname, lastname, phone_number):
        self.firstname = firstname
        self.lastname = lastname
        self.email = ''
        self.national_code = None
        self.phone_number = phone_number

    def email_address_validation(self):

        while True:
            try:
                email = input('enter your email: ')
                if email.endswith(".com"):
                    if email.startswith('@') == False:
                        if re.findall("@", email):
                            self.email = email
                            break

                        else:
                            raise ValueError()
                    else:

                        raise ValueError()

                else:

                    raise ValueError()



            except  ValueError:
                print("email is wrong!please try again")

    def national_code_validation(self):
        while True:
            try:
                national_code = input("Enter national code:")
                if len(national_code) == 10:
                    self.national_code = national_code
                    break
                else:
                    raise ValueError()

            except ValueError:
                print("it is wrong try again!please try again")

    def change_to_dict(self):
        dict_info_Person = vars(self)

        return dict_info_Person

    def Edit(self):
        dict_info_Person = Person.change_to_dict(self)

        list_of_key_edit = []
        list_of_value_edit = []
        number_of_edit = int(input('How many do you want to change?'))
        for j in range(number_of_edit):
            print("firstname\t\tlastname\t\temail\t\tnational_code\t\tphone_number")
            key = input("Enter the attribute you want to change:")
            if key not in dict_info_Person.keys():
                print("This key not found!")
            else:
                list_of_key_edit.append(key)

        for k in range(len(list_of_key_edit)):
            if list_of_key_edit[k] == "email":
                while True:
                    try:
                        value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                        if value.endswith(".com"):
                            if value.startswith('@') == False:
                                if re.findall("@", value):

                                    list_of_value_edit.append(value)
                                    dict_info_Person.update({list_of_key_edit[k]: list_of_value_edit[k]})
                                    break

                                else:
                                    raise ValueError()
                            else:

                                raise ValueError()

                        else:

                            raise ValueError()

                    except  ValueError:
                        print("email is wrong!please try again")
            elif list_of_key_edit[k] == "national_code":
                while True:
                    try:
                        value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                        if len(value) == 10:
                            list_of_value_edit.append(value)
                            dict_info_Person.update({list_of_key_edit[k]: list_of_value_edit[k]})
                            break
                        else:
                            raise ValueError()

                    except ValueError:
                        print("it is wrong try again!please try again")

            else:
                value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                list_of_value_edit.append(value)
                dict_info_Person.update({list_of_key_edit[k]: list_of_value_edit[k]})

    def show_info(self):

        for k, v in Person.change_to_dict(self).items():
            print(k, '=', v, end=" , ")
        else:
            print('\n')


class Store:

    def __init__(self, tenant, owner, address, active_inactive, telephone, area,
                 mortgage_amount, rental_amount, sales_amount, sales_rental):
        self.tenant = tenant
        self.owner = owner
        self.address = address
        self.active_inactive = active_inactive
        self.telephone = telephone
        self.area = area
        self.mortgage_amount = mortgage_amount
        self.rental_amount = rental_amount
        self.sales_rental = sales_rental
        self.sales_amount = sales_amount

    def change_to_dict(self):
        dict_info_Store = vars(self)

        return dict_info_Store

    def Edit(self):
        dict_info_Store = Store.change_to_dict(self)

        list_of_key_edit = []
        list_of_value_edit = []
        number_of_edit = int(input('How many do you want to change?:'))
        for i in range(number_of_edit):
            key = input("Enter the attribute you want to change:")
            list_of_key_edit.append(key)

        for j in list_of_key_edit:
            if j in dict_info_Store.keys():
                for k in range(number_of_edit):
                    value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                    list_of_value_edit.append(value)
                    dict_info_Store.update({list_of_key_edit[k]: list_of_value_edit[k]})
                break

            else:
                print("Not found!")

    def show_info(self):

        for k, v in Store.change_to_dict(self).items():
            print(k, '=', v, end=" , ")
        else:
            print('\n')


class Apartment:
    def __init__(self, tenant, owner, address, active_inactive, telephone, area,
                 mortgage_amount, rental_amount, sales_amount, sales_rental, number_rooms, number_floor, floor,
                 parking):
        self.tenant = tenant
        self.owner = owner
        self.address = address
        self.active_inactive = active_inactive
        self.telephone = telephone
        self.area = area
        self.mortgage_amount = mortgage_amount
        self.rental_amount = rental_amount
        self.sales_rental = sales_rental
        self.sales_amount = sales_amount
        self.number_rooms = number_rooms
        self.number_floor = number_floor
        self.floor = floor
        self.parking = parking

    def change_to_dict(self):
        dict_info_Apartment = vars(self)

        return dict_info_Apartment

    def Edit(self):
        dict_info_Apartment = Apartment.change_to_dict(self)

        list_of_key_edit = []
        list_of_value_edit = []
        number_of_edit = int(input('How many do you want to change?:'))
        for i in range(number_of_edit):
            key = input("Enter the attribute you want to change:")
            list_of_key_edit.append(key)

        for j in list_of_key_edit:
            if j in dict_info_Apartment.keys():
                for k in range(number_of_edit):
                    value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                    list_of_value_edit.append(value)
                    dict_info_Apartment.update({list_of_key_edit[k]: list_of_value_edit[k]})
                break

            else:
                print("Not found!")

    def show_info(self):

        for k, v in Apartment.change_to_dict(self).items():
            print(k, '=', v, end=" , ")
        else:
            print('\n')


class Home:
    def __init__(self, tenant, owner, address, active_inactive, telephone, area,
                 mortgage_amount, rental_amount, sales_amount, sales_rental, number_rooms, number_floor,
                 area_yard):
        self.tenant = tenant
        self.owner = owner
        self.address = address
        self.active_inactive = active_inactive
        self.telephone = telephone
        self.area = area
        self.mortgage_amount = mortgage_amount
        self.rental_amount = rental_amount
        self.sales_rental = sales_rental
        self.sales_amount = sales_amount
        self.number_rooms = number_rooms
        self.number_floor = number_floor
        self.area_yard = area_yard

    def change_to_dict(self):
        dict_info_Home = vars(self)

        return dict_info_Home

    def Edit(self):
        dict_info_Home = Home.change_to_dict(self)

        list_of_key_edit = []
        list_of_value_edit = []
        number_of_edit = int(input('How many do you want to change?:'))
        for i in range(number_of_edit):
            key = input("Enter the attribute you want to change:")
            list_of_key_edit.append(key)

        for j in list_of_key_edit:
            if j in dict_info_Home.keys():
                for k in range(number_of_edit):
                    value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                    list_of_value_edit.append(value)
                    dict_info_Home.update({list_of_key_edit[k]: list_of_value_edit[k]})
                break

            else:
                print("Not found!")

    def show_info(self):

        for k, v in Home.change_to_dict(self).items():
            print(k, '=', v, end=" , ")
        else:
            print('\n')


class Real_Estate_Advisor:

    def __init__(self, sales_rental, area, mortgage_amount, rental_amount, sales_amount, type_building):
        self.sales_rental = sales_rental
        self.area = area
        self.mortgage_amount = mortgage_amount
        self.rental_amount = rental_amount
        self.sales_amount = sales_amount
        self.type_building = type_building

    def change_to_dict(self):
        dict_info_search = vars(self)

        return dict_info_search

    def search(self):
        dict_info_search = Real_Estate_Advisor.change_to_dict(self)
        df = pd.read_csv("csv_file1.csv", sep=",")
        a = df.loc[(df["active_inactive"] == "active") & (df["type_building"] == dict_info_search["type_building"]) & (
                df["sales_rental"] == dict_info_search["sales_rental"]) & (df["area"] == dict_info_search["area"]) & (
                           df["mortgage_amount"] == dict_info_search["mortgage_amount"]) & (
                           df["rental_amount"] == dict_info_search["rental_amount"]) & (
                           df["sales_amount"] == dict_info_search["sales_amount"])]
        # print(a)
        if len(a) >= 1:
            print("found your building")
            print(a)
            b = a.index
            for x in b:
                df.loc[x, ["Suggestion"]] = "yes"
                df.to_csv("csv_file1.csv")
            return True
        else:
            print("Not found")
        return False


class Transaction:
    def __init__(self, owner, tenant, buyer, experition_transaction, date_of_contract):
        self.buyer = buyer
        self.owner = owner
        self.tenant = tenant
        self.experition_transaction = experition_transaction
        self.date_of_contract = date_of_contract

    def change_to_dict(self):
        dict_info_tr = vars(self)

        return dict_info_tr
    def done(self):
      df = pd.read_csv("csv_file1.csv", sep=",")
      b = df.loc[(df["Suggestion"] == "yes") & (df["active_inactive"] == "active")]
      if len(b) >= 1:
          print("The deal was done")
      else:
          raise ValueError
    def inactive(self):
        dict_info_tr = Transaction.change_to_dict(self)
        df = pd.read_csv("csv_file1.csv", sep=",")
        c = df.loc[(df["Suggestion"] == "yes") & (df["active_inactive"] == 'active')]
        d = c.index
        for x in d:
            df.loc[x, ['active_inactive', 'owner', "tenant", "buyer"]] = ["inactive", dict_info_tr["owner"],
                                                                          dict_info_tr["tenant"], dict_info_tr["buyer"]]
            df.to_csv("csv_file1.csv")

    def __str__(self):
            return f"buyer is{self.buyer} tenant is {self.tenant} owner is {self.owner} and date of experition is  {self.experition_transaction} and the date of contract is {self.date_of_contract}"






"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"

"""
give address
"""


def give_address():
    global dict_address
    global address
    city_name = input('Enter the city:')
    street_name = input('Enter the street:')
    number_plaque = input("Enter the plaque:")
    number_postal_code = input("Enter postal code:")
    address = Address(city_name=city_name, street_name=street_name, number_plaque=number_plaque,
                      number_postal_code=number_postal_code)
    dict_address = {"city_name": city_name, "street_name": street_name, "number_plaque": number_plaque,
                    "number_postal_code": number_postal_code}

    address.change_to_dict()
    address.show_info()
    return address


"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"

"""
give info_person
"""


def get_info_person():
    global info_person
    firstname = input('Enter your first name:')
    lasttname = input('Enter your last name:')
    phone_number = input("Enter the phone number:")
    info_person = Person(firstname, lasttname, phone_number=phone_number)

    # list_firstname.append(firstname)
    # list_lastname.append(lastname)
    # dict_person = {"firstname": firstname, "lastname": lastname}
    # list_person.append(dict_person)

    return info_person


"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
"""
give info_store
"""


def get_info_store():
    global store
    # global dict_store
    tenant = input("Enter tenant:")
    owner = input("Enter owner:")
    sales_rental = input("Enter sales or rental:")
    mortgage_amount = float(input("Enter mortgage_amount: "))
    rental_amount = float(input("Enter Rental_amount:"))
    sales_amount = float(input("Enter sales_amount:"))
    address = input("Enter address:")
    active_inactive = input("Enter active or inactive")
    telephone = input("Enter telephone number:")
    area = float(input("Enter area"))
    store = Store(tenant=tenant, owner=owner, mortgage_amount=mortgage_amount, rental_amount=rental_amount,
                  sales_rental=sales_rental, address=address, active_inactive=active_inactive, telephone=telephone,
                  sales_amount=sales_amount, area=area)

    store.show_info()
    return store


"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"

"""
get info_home
"""


def get_info_home():
    global home
    # global dict_home
    tenant = input("Enter tenant:")
    owner = input("Enter owner:")
    sales_rental = input("Enter sales or rental:")
    mortgage_amount = float(input("Enter mortgage_amount: "))
    rental_amount = float(input("Enter Rental_amount:"))
    sales_amount = float(input("Enter sales_amount:"))
    address = input("Enter address:")
    active_inactive = input("Enter active or inactive!")
    telephone = input("Enter telephone number:")
    area = float(input("Enter area"))
    number_rooms = input("Enter number_rooms:")
    number_floor = input("Enter number_floor:")
    area_yard = input("Enter area yard:")
    home = Home(tenant=tenant, owner=owner, mortgage_amount=mortgage_amount, rental_amount=rental_amount,
                sales_rental=sales_rental, address=address, active_inactive=active_inactive, telephone=telephone,
                sales_amount=sales_amount, area=area, number_rooms=number_rooms, number_floor=number_floor,
                area_yard=area_yard)

    home.change_to_dict()
    home.show_info()
    return home


"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
"""
get info_apart
"""


def get_info_apart():
    global apart
    global apartment_dict
    tenant = input("Enter tenant:")
    owner = input("Enter owner:")
    sales_rental = input("Enter sales or rental:")
    mortgage_amount = float(input("Enter mortgage_amount: "))
    rental_amount = float(input("Enter Rental_amount:"))
    sales_amount = float(input("Enter sales_amount:"))
    address = input("Enter address:")
    active_inactive = input("Enter active or inactive!")
    telephone = input("Enter telephone number:")
    area = float(input("Enter area"))
    number_rooms = input("Enter number_rooms:")
    number_floor = input("Enter number_floor:")
    floor = input("Enter floor:")
    parking = input("Enter parking:")
    apart = Apartment(tenant=tenant, owner=owner, mortgage_amount=mortgage_amount, rental_amount=rental_amount,
                      sales_rental=sales_rental, address=address, active_inactive=active_inactive, telephone=telephone,
                      sales_amount=sales_amount, area=area, number_rooms=number_rooms, number_floor=number_floor,
                      floor=floor, parking=parking)

    apartment_dict = apart.change_to_dict()
    apart.show_info()
    return apart


"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
list_person = []
list_apart = []
list_home = []
list_store = []
"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
"""
get info_to_search
"""


def get_info_to_search():
    global search_obj
    type_building = input("Enter the type_building you lik.").strip()
    sales_rental = input("Do you want to rent or sell a bulding? 1_sale 2_rental").strip()
    mortgage_amount = float(input("Enter the mortgage_amount That you like"))
    rental_amount = float(input("Enter the rental_amount That you like"))
    sales_amount = float(input("Enter the sales_mount That you like"))
    area = float(input("Enter the area That you like"))

    seaech_obj = Real_Estate_Advisor(sales_rental, area, mortgage_amount, rental_amount, sales_amount, type_building)
    return seaech_obj


"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
"""
get_info_Transaction
"""


def info_transction():
    owner = input("Enter the name of owner.exampale:zeynab yousefi").split()
    for i in range(len(list_person)):
        if owner[0] == list_person[i]["firstname"] and owner[1] == list_person[i]["lastname"]:
            print("found you")
    buyer = input("Enter the name of buyer.exampale:zeynab yousefi").split()
    for i in range(len(list_person)):
        if buyer[0] == list_person[i]["firstname"] and buyer[1] == list_person[i]["lastname"]:
            print("found you")
    tenant = input("Enter the name of tenant.exampale:zeynab yousefi").split()
    for i in range(len(list_person)):
        if tenant[0] == list_person[i]["firstname"] and tenant[1] == list_person[i]["lastname"]:
            print("found you")

    experition_transaction = input("Enter the experition_transaction.")
    date_of_contract = input("Enter the date_of_contract  ")
    transec = Transaction(owner, tenant, buyer, experition_transaction, date_of_contract)

    return transec


"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"


def menu():
    while True:
        print(
            "class>> 1.Address\t\t2.Person\t\t3.Apartment\t\t4.Home\t\t5.Store\t\t6.Real Estate Advisor\t\t7.Transaction\t\t\tQuit:else")
        number_class = input("Enter a number of class: ")

        if number_class == "1":
            address_obj = give_address()
            address_obj.change_to_dict()

            while True:
                print("method>> 1.Edit\t\t2.show info\t\t\tQuit:else")
                address_number = input("Choose your method: ")
                if address_number == "1":
                    address_obj.Edit()
                elif address_number == "2":
                    address_obj.show_info()
                else:
                    break

        elif number_class == "2":
            info_person = get_info_person()
            p = info_person.change_to_dict()
            list_person.append(p)
            print(list_person)

            while True:
                print(
                    "method>> 1.email_address_validation\t\t2.national_code_validation\t\t3.Edit\t\t4.show_info\t\t\tQuit:else")
                person_number = input("Choose a number of method: ")
                if person_number == "1":
                    info_person.email_address_validation()
                elif person_number == "2":
                    info_person.national_code_validation()
                elif person_number == "3":
                    info_person.Edit()



                elif person_number == "4":
                    info_person.show_info()
                else:
                    break

        elif number_class == "3":
            apartment_obj = get_info_apart()
            q = apartment_obj.change_to_dict()
            df = pd.read_csv("csv_file1.csv")
            i = int(input("Which line do you want to fill?"))
            df.loc[i, ["type_building", "tenant", 'owner', 'address', 'active_inactive', 'telephone', 'area',
                       "mortgage_amount", "rental_amount", "sales_amount", "sales_rental", "number_rooms",
                       "number_floor", "floor",
                       "parking"]] = ["apartment", q["tenant"], q['owner'], q['address'], q['active_inactive'],
                                      q['telephone'],
                                      q['area'],
                                      q["mortgage_amount"], q["rental_amount"], q["sales_amount"], q["sales_rental"],
                                      q["number_rooms"], q["number_floor"], q["floor"],
                                      q["parking"]]
            df.to_csv("csv_file1.csv", index=True)

            list_apart.append(q)

            while True:
                print("method>> 1.Edit\t\t2.show info\t\t\tQuit:else")
                apartment_number = input("Choose your method: ")
                if apartment_number == "1":
                    apart.Edit()
                    df = pd.read_csv("csv_file1.csv")
                    i = int(input("Which line do you want to fill?"))
                    df.loc[i, ["type_building", "tenant", 'owner', 'address', 'active_inactive', 'telephone', 'area',
                               "mortgage_amount", "rental_amount", "sales_amount", "sales_rental", "number_rooms",
                               "number_floor", "floor",
                               "parking"]] = ["apartment", q["tenant"], q['owner'], q['address'], q['active_inactive'],
                                              q['telephone'], q['area'],
                                              q["mortgage_amount"], q["rental_amount"], q["sales_amount"],
                                              q["sales_rental"], q["number_rooms"], q["number_floor"], q["floor"],
                                              q["parking"]]
                    df.to_csv("csv_file1.csv", index=True)



                elif apartment_number == "2":
                    apart.show_info()

                else:
                    break

        elif number_class == "4":
            home = get_info_home()
            home_dict = home.change_to_dict()
            df = pd.read_csv("csv_file1.csv")
            i = int(input("Which line do you want to fill?"))
            df.loc[i, ["type_building", "tenant", 'owner', 'address', 'active_inactive', 'telephone', 'area',
                       "mortgage_amount", "rental_amount", "sales_amount", "sales_rental", "number_rooms",
                       "number_floor", "area_yard"
                       ]] = ["home", home_dict["tenant"], home_dict['owner'], home_dict['address'],
                             home_dict['active_inactive'], home_dict['telephone'],
                             home_dict['area'],
                             home_dict["mortgage_amount"], home_dict["rental_amount"],
                             home_dict["sales_amount"], home_dict["sales_rental"],
                             home_dict["number_rooms"], home_dict["number_floor"],
                             home_dict["area_yard"]]
            df.to_csv("csv_file1.csv", index=True)

            list_home.append(home_dict)
            while True:
                print("method>> 1.Edit\t\t2.show info\t\t\tQuit:else")
                home_number = input("Choose your method: ")
                if home_number == "1":
                    home.Edit()
                    df = pd.read_csv("csv_file1.csv")
                    i = int(input("Which line do you want to fill?"))
                    df.loc[i, ["type_building", "tenant", 'owner', 'address', 'active_inactive', 'telephone', 'area',
                               "mortgage_amount", "rental_amount", "sales_amount", "sales_rental", "number_rooms",
                               "number_floor",
                               "area_yard"]] = ['home', home_dict["tenant"], home_dict['owner'], home_dict['address'],
                                                home_dict['active_inactive'], home_dict['telephone'],
                                                home_dict['area'],
                                                home_dict["mortgage_amount"], home_dict["rental_amount"],
                                                home_dict["sales_amount"], home_dict["sales_rental"],
                                                home_dict["number_rooms"], home_dict["number_floor"],
                                                home_dict["area_yard"]]
                    df.to_csv("csv_file1.csv", index=True)



                elif home_number == "2":
                    home.show_info()
                else:
                    break
        elif number_class == "5":
            store = get_info_store()
            store_dict = store.change_to_dict()
            list_store.append(store_dict)
            df = pd.read_csv("csv_file1.csv")
            i = int(input("Which line do you want to fill?"))
            df.loc[i, ["type_building", "tenant", 'owner', 'address', 'active_inactive', 'telephone', 'area',
                       "mortgage_amount", "rental_amount", "sales_amount", "sales_rental"]] = ["store",
                                                                                               store_dict["tenant"],
                                                                                               store_dict['owner'],
                                                                                               store_dict['address'],
                                                                                               store_dict[
                                                                                                   'active_inactive'],
                                                                                               store_dict['telephone'],
                                                                                               store_dict['area'],
                                                                                               store_dict[
                                                                                                   "mortgage_amount"],
                                                                                               store_dict[
                                                                                                   "rental_amount"],
                                                                                               store_dict[
                                                                                                   "sales_amount"],
                                                                                               store_dict[

                                                                                                   "sales_rental"]]

            df.to_csv("csv_file1.csv", index=True)

            while True:
                print("method>> 1.Edit\t\t2.show info\t\t\tQuit:else")
                store_number = input("Choose your method: ")
                if store_number == "1":
                    store.Edit()
                    df = pd.read_csv("csv_file1.csv")
                    i = int(input("Which line do you want to fill?"))
                    df.loc[i, ["type_building", "tenant", 'owner', 'address', 'active_inactive', 'telephone', 'area',
                               "mortgage_amount", "rental_amount", "sales_amount", "sales_rental"]] = ["store",
                                                                                                       store_dict[
                                                                                                           "tenant"],
                                                                                                       store_dict[
                                                                                                           'owner'],
                                                                                                       store_dict[
                                                                                                           'address'],
                                                                                                       store_dict[
                                                                                                           'active_inactive'],
                                                                                                       store_dict[
                                                                                                           'telephone'],
                                                                                                       store_dict[
                                                                                                           'area'],
                                                                                                       store_dict[
                                                                                                           "mortgage_amount"],
                                                                                                       store_dict[
                                                                                                           "rental_amount"],
                                                                                                       store_dict[
                                                                                                           "sales_amount"],
                                                                                                       store_dict[
                                                                                                           "sales_rental"],
                                                                                                       ]
                    df.to_csv("csv_file1.csv", index=True)


                elif store_number == "2":
                    store.show_info()
                else:
                    break

        elif number_class == '6':
            search_obj = get_info_to_search()
            search_obj.search()
            search_obj.change_to_dict()


        elif number_class == '7':
            transec = info_transction()
            transec.change_to_dict()
            transec.done()
            transec.inactive()
            print(transec)


        else:
            break


menu()
