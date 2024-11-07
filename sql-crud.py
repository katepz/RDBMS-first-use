from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()

#create a class-based model for the "Programmer " table
# class Programmer(base):
#     __tablename__ = "Programmer"
#     id = Column(Integer, primary_key = True)
#     first_name = Column(String)
#     last_name = Column(String)
#     gender = Column(String)
#     nationality = Column(String)
#     famous_for = Column(String)

#create a class-based model for the "Pet" table
class Pet(base):
    __tablename__ = "Pet"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    species = Column(String)
    colour = Column(String)
    age = Column(Integer, primary_key= False)

#instead of connecting to the database directly we eill ask for a seesion
#create a new instance of sessionmaker, then point to our engine ( the database)
Session = sessionmaker(db)
#opens an actual session by calling the Session() subclass defined above
session = Session()
#creating the database using the declarative_base subclass
base.metadata.create_all(db)

#creating records for our "Pet" table
barney = Pet(
    name = "Barney",
    species = "Cat",
    colour = "Tabby",
    age = 6
)

betty = Pet(
    name = "Betty",
    species = "Cat",
    colour = "Black & white",
    age = 6
)

cody = Pet(
    name = "Cody",
    species = "Dog",
    colour = "White & black",
    age = 13
)

mo = Pet(
    name = "Mo",
    species = "Hamster",
    colour = "Brown",
    age = 2
)

polar = Pet(
    name = "Polar",
    species = "Hamster",
    colour = "White",
    age = 3
)

percy = Pet(
    name = "Percy",
    species = "Bird",
    colour = "Grey",
    age = 4
)

ollie = Pet(
    name = "Ollie",
    species = "Dog",
    colour = "Black",
    age = 15
)

# session.add(barney)
# session.add(betty)
# session.add(cody)
# session.add(mo)
# session.add(polar)
# session.add(percy)
# session.add(ollie)

#updating a single record
# pet = session.query(Pet).filter_by(name = "Barney").first()
# pet.species = "Muppet"

#updating multiple records
pets = session.query(Pet)
for pet in pets:
    if pet.species == "Cat":
        pet.species = "Feline"
    elif pet.species == "Dog":
        pet.species = "Canine"
    else:
        pet.species
    session.commit()

#commit our session to the database
session.commit()

#query the database to find all pets 
pets = session.query(Pet)
for pet in pets:
    print(
        pet.id,
        pet.name,
        pet.species,
        pet.colour,
        pet.age,
        sep = " | "
    )

#creating records on our "Programmer" table
# ada_lovelace = Programmer(
#     first_name = "Ada",
#     last_name = "Lovelace",
#     gender = "F",
#     nationality = "British",
#     famous_for = "First Programmer",
# )

# alan_turing = Programmer(
#     first_name = "Alan",
#     last_name = "Turing",
#     gender = "M",
#     nationality = "British",
#     famous_for = "Modern Computing",
# )

# grace_hopper = Programmer(
#     first_name = "Grace",
#     last_name = "Hopper",
#     gender = "F",
#     nationality = "American",
#     famous_for = "COBOL Language",
# )

# margaret_hamilton = Programmer(
#     first_name = "Margaret",
#     last_name = "Hamilton",
#     gender = "F",
#     nationality = "American",
#     famous_for = "Apollo 11",
# )

# bill_gates = Programmer(
#     first_name = "Bill",
#     last_name = "Gates",
#     gender = "M",
#     nationality = "American",
#     famous_for = "Microsoft",
# )

# tim_berners_lee = Programmer(
#     first_name = "Tim",
#     last_name = "Berners-Lee",
#     gender = "M",
#     nationality = "Britsh",
#     famous_for = "World Wide Web",
# )

# kate_eaves = Programmer(
#     first_name = "Kate",
#     last_name = "Eaves",
#     gender = "F",
#     nationality = "Britsh",
#     famous_for = "Oldest BBC Apprentice",
# )

#add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(kate_eaves)

#commit our session to the database
# session.commit()

#updating a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"

#commit our session to the database
# session.commit()

#updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not specified")
#     session.commit()

#deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

# #defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this programmer? (y/n)")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer has not been deleted")
# else:
#     print("No records found")



#query the database to find all programmers - test to see if ada is there
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep = " | "
#     )