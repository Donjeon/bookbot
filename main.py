
def main():
    franekstein_string = returnFrankensteinAsString()
    frankenstein_list = returnStringAsListOfWords(franekstein_string.lower())
    #countCharacterOccurrencesInList(frankenstein_list)
    bookReport(countCharacterOccurrencesInString(franekstein_string.lower()))


def returnFrankensteinAsString():
    with open("/home/v/workspace/github.com/Donjeon/bookbot/books/frankenstein.txt") as f:
        frankString = f.read()
        return frankString

def returnStringAsListOfWords(string):
    list_of_words = string.split()
    return list_of_words

def printString(string):
    print(string)

#My initial implementation
def countCharacterOccurrencesInList(frankenstein):
    character_dictionary = {}

    for word in frankenstein:
        for character in word:
            if character in character_dictionary:
                character_dictionary[character] += 1
            else: 
                character_dictionary[character] = 1

    print(character_dictionary)

#Realising I can remove the nested for loop by iterating through whole text
#after looking at the solution
def countCharacterOccurrencesInString(frankenstein):
    character_dictionary = {}

    for character in frankenstein:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else: 
            character_dictionary[character] = 1

    return character_dictionary

    #Making this into report version
    #add each dictionary key:value pair and add them to a list
    #Can I iterate through each entry of the list and compare value as I go
    #Say we have list(100, 10, 50)
    #I have num, which has value 30. 
    #I do if num

    #?????
    #return list (which has been put in descending order)

    #Convert character_dictionary into a list called list
    #ordered_numbers.append(list.pop(max(list)))
    #and just loop through the list?

def sort_on(dict):
    return dict["occurrences"]

def bookReport(dictionary):
    #Convert character_dictionary into a list called list
    #ordered_numbers.append(list.pop(max(list)))
    #and just loop through the list?

    #Create list of just numbers. Compare the dictionary entries to the number
    #in the list. if it matches, print out the number and the character
    #Just feels too unhinged and complicated to write it like that

    #using the boot.dev hint
    #need to make a list of dictionaries
    #so for i in dictionary: "character" = the character, "count" = the number. Use .items()
    #then do the sorting as described 
    #then make a loop that iterates through the dictionary and prints each bit

    list = []
    for character, occurrences in dictionary.items():
        toAdd = {}
        toAdd["character"] = character
        toAdd["occurrences"] = occurrences
        list.append(toAdd)

    list.sort(reverse=True, key=sort_on)

    franekstein_as_string = returnFrankensteinAsString()
    word_list = returnStringAsListOfWords(franekstein_as_string.lower())
    word_count = len(word_list)

    print("---Oh my word my variables have such poor names---")
    print(f"{word_count} words found in the document")
    print(" ")

    for dictionary in list:
        char = dictionary["character"] 
        num = dictionary["occurrences"]
        print(f"The '{char}' character was found {num} times!")
    
    print("---5k XP chest here we come---")

    

    
    

main()
