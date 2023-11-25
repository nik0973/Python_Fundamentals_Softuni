## slice notation
# text = "This is Softuni Fundamentals'"
# course_name = text[-12:] # - cut the last 12 synbols
# course_name = text[16:] # leave only last 16 symbols
# course_name = text[8:-13] # print only Softuni
# course_name = text[8:15] # range from string Softuni
# print(course_name)

## 2 with list
# numbers = [1, 2, 3, 4]
# subset = numbers[1:3]

## 3
# text = 'Python Programming'
# slice = text[0:10:2] - # give from 0 to 10 thorough 1
# print(slice)

## 4 isdigig
# data = '12345'
# print(data.isdigit())

## 5 lower upper
# data  = "hello world"
# print(data.upper()) # make symbol upper
# print(data.lower()) # make symbol lower

## 6 islower isupper
# data = 'karam Kola'
# print(data[0:5].islower()) # check some symbol if are lower
# print(data[6:7].isupper()) # check only upper K if is upper

## 7 strip - remove space from left and right
# lstrip remove only left space
# rstrip remove only right space
# data = ' text text '
# print(data.strip())

## 8 capitalize - make first symbol upper
# text = 'hello world'
# print(text.casefold())

## 9 casefold -same as the lower
# text = 'HELLO'
# print(text.casefold())

## 10 endwith - if the string finish with some symbol and startswith
# text = 'hello world'
# print(text.endswith('ld'))
# print(text.startswith('hell'))

## 11 isalpha - if the string contain only from alphabetic and isnumeric if the string contain only numbers
# text = 'hello'
# print(text.isalpha())

## 12 replace
# sentence = 'I like bananas'
# new_sentence = sentence.replace('bananas', 'apples')
# print(new_sentence)
# sentence = 'Mississippi'
# new_sentence = sentence.replace('i', '1', 2) # change i with 1 only 2 times
# print(new_sentence) #result M1ss1ssippi

name = 'Mario'
print(name.replace('M', 'm'))








