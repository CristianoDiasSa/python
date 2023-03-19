def print_details(person):
    print("This person name is " + person.name)
    print("This person age is " + str(person.age))


def print_diamond():
    rows = int(input('Enter the number of rows: '))
    for i in range(rows):
        print(" " * (rows - i), "*" * (2 * i + 1))
    for i in range(rows - 2, -1, -1):
        print(" " * (rows - i), "*" * (2 * i + 1))


def read_and_manipulate_text(word_to_search):
    file = open('test.txt')
    text = file.read()
    file.close
    split_text = text.split(' ')
    print(split_text)
    length = len(split_text)
    count = split_text.count(word_to_search)
    print('Total length of the text is ' + str(length) + ".",'\nThe total times that the word '+ word_to_search + 
          " appears is " + str(count))
    #This will return the indexes of all ocurrences of the searched word!
    if count == 1:
        print('The index of the searched word is ' + str(split_text.index(word_to_search)))
    else:
        ocurrences = []
        for index, value in enumerate(split_text):
            if value == word_to_search:
                ocurrences.append(index)
    
        print('The indexes of the word searched is :' + str(ocurrences))

