Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Olivia Busk
... 
... # Problem 1
>>> type("Rosewater")
<class 'str'>
>>> type(0.001)
<class 'float'>
>>> type(37)
<class 'int'>
>>> type(False)
<class 'bool'>
>>> # Problem 2
... 
... # using comma in print allows for use of space
>>> print("Hello", "World!")
Hello World!
>>> # using space in print takes away space
>>> print("Hello"+ "World!")
HelloWorld!
>>> # Problem 3
... # int, float, str
>>> int(6.45)
6
>>> int(-15.67)
-15
>>> float(76)
76.0
>>> float('32.45')
32.45
>>> str('Olivia')
'Olivia'
>>> str('14.24')
'14.24'
>>> # Problem 4
... # \n - song lyrics from Mumford and Sons
>>> print("It's empty in the valley of your heart, \nThe sun, it rises slowly as you walk, \nAway from all the fears, \nAnd all the faults you've left behind, \nThe harvest left no food for you to eat")
It's empty in the valley of your heart, 
The sun, it rises slowly as you walk, 
Away from all the fears, 
And all the faults you've left behind, 
The harvest left no food for you to eat
# Problem 5
flour=2
milk=5
egg=4
oil=.4
vanilla=0.12
cake = 2 * flour + 0.5 * (milk - egg + vanilla) + oil**2
print(cake)
4.720000000000001
