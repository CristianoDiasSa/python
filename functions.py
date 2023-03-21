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

def create_and_write():
    text_to_write = open('test2.txt', 'w')
    text_to_write.write('Hello, this is a test!')
    text_to_write.close()

    file = open('test2.txt')
    test = file.read()
    print(test)



def read_and_write():
    new_created_file = open('test3.txt', 'w')
    new_created_file.close()

    text = open('test.txt', 'r')
    new_text = text.read()
    text.close()
    split_text = new_text.split(' ')

    new_file = open('test3.txt', 'a')
    cardinal = 1
    for words in split_text:
        new_file.write(words)
        new_file.write(" "*(15-len(words)))
        new_file.write(str(cardinal) + 'th word\n')
        cardinal +=1
    new_file.close()

    file_to_print = open('test3.txt')

    print(file_to_print.read())






    