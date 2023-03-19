import model as model
import functions as functions


first_person = model.Person('Cristiano', 29)
second_person = model.Person('Dias', 29)
people = [first_person, second_person]
for person in people:
    functions.print_details(person)

functions.print_diamond()
