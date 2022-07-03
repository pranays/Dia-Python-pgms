#!/usr/bin/python3

'''
    Sum of two numbers
'''
def sumOfTwoNumbers():
    a = int(input('Enter first value:'))
    b = int(input('Enter second value:'))
    sumVal = a + b
    print('Sum Of two numbers:{}'.format(sumVal))


def exampleDictionary():
    dictionary = {}

    # print type of dictonary
    print('Type of dictonary {}'.format(type(dictionary)))

    dictionary["key1"] = "value1"
    dictionary[42] = "This is a test"
    dictionary[1.2] = "testing is an experiment"
    print(dictionary)

    # print all keys in dictionary
    print("-------------------------------")
    print("Keys:-->")
    for k in dictionary.keys():
        print('\b {}'.format(k)) 

    # print all keys in dictionary
    print("-------------------------------")
    print("Values:-->")
    for v in dictionary.values():
        print('\b {}'.format(v)) 

    print("-------------------------------")
    print("Key Value:-->")
    for k, v in dictionary.items():
        print('\b {} {}'.format(k, v)) 

if __name__ == '__main__':
    #sumOfTwoNumbers()
    exampleDictionary()

