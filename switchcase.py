from fuzzywuzzy import process
from fuzzywuzzy import fuzz

def switch(lang):
    

    # opening the file in read mode
    my_file = open("selection.txt", "r")
  
    # reading the file
    data = my_file.read()
  
    # replacing end splitting the text 
    # when newline ('\n') is seen.
    data_into_list = data.split("\n")

    my_file.close()




    selection = process.extractOne(lang,data_into_list)
    print(selection)
    command = str(selection[0])
    return command
##
##switch(str(selection[0]))


