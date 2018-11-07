# Tech Test - Rationale Behind Steps Taken

This test was quite challenging for me, as I am not familiar with Python. I found some basic Python exercises online and did those, as well as doing a lot of reviewing of websites like [TutorialsPoint](https://www.tutorialspoint.com/python), to help me answer the questions.

## Question 1 - Debugging

### Initial review of sample code

I understand that the ```d``` in the function ```increment_dictionary_values``` represents a dictionary, and the ```i``` represents an integer.
Similarly, the ```k``` within the same function refers to a key, and the ```v``` refers to a value, within a key value pair.

### Key components

For this part of the test, I learned about lists and dictionaries in Python.

Dictionaries elements are accessed via keys, and list elements are accesssed by their position in the list, via indexing.

In Python, dictionaries are a kind of data structure that is also known as an associative array. Dictionaries consist of key/value pairs; each key/value pair maps the key to its corresponding value.

A dictionary is defined using curly braces around a list of key/value pairs separated by commas, as follows:

```
d = {
  key: value,
  key: value,
}
```
It can also be defined using Python's built-in ```.dict()``` function, as follows:

```
d = dict ([
  (key, value),
  (key, value),
  ])
```
### Issue

Currently, the function ```increment_dictionary_values``` takes a dictionary (```d```) and an integer (```i```). The function ```.items()``` returns a tuple (pair of items), when called on the dictionary ```d```. After this, ```i``` is added for each dictionary item.

So with the original function:
```
def increment_dictionary_values(d, i):
  for k, v in d.items():
    d[k] = v + i
  return d
```

If ``` d = {"a":1}```, ```k``` would equal ```a```, and ```v``` would equal ```1```. If ```i``` is ```1```, the ```increment_dictionary_values``` function would alter ```d``` so that it is ```{"a":2}```.

Because we are always operating on the same dictionary in terms of what is being referenced in the code, **and** because dictionaries are mutable, the data contained in the dictionary is being changed in the function. This means that the test cases will all be the same. The test case ```dd``` adds one to the value, which means the dictionary will be ```{"a": 2}```. Test case ```ddd``` removes 1 from the value, and because ```ddd``` is being run after ```dd```, the dictionary will still be ```{"a": 2}```.

### Solutions

#### Solution 1

One way to get around this is to create a new dictionary (```new_dictionary``` in the given solution), and run the function on the dictionary copy.

#### Solution 2

The other alternative is to amend the test cases in the test function, so that the ```ddd``` test case is referencing ```dd```, as follows:

```
  class TestIncrementDictionaryValues(TestCase) :

    def test_increment_dictionary_values(self) :
      d = {'a': 1}
      dd = increment_dictionary_values(d, 1)
      ddd = increment_dictionary_values(dd, -1)
      self.assertEqual(dd['a'], 2)
      self.assertEqual(ddd['a'], 1)
```

## Question 2 - Write a function & tests

I used the [Python.org](https://docs.python.org/2/library/unittest.html) website to learn about testing in Python.

### Setting up

The Python testing framework is ```unittest```, a module which provides classes that are designed to optimise testing. One of these is a base class called ```TestCase```. The _test suite_ is a collection of _test cases_; a _test case_ is the smallest unit of testing. It checks for a specific outcome when applied to certain inputs.

The ```TestCase``` class is used when creating new tests, so I will use that in my code in the same was as it was used in the ```increment_dictionary_values``` code.

I then created a function called ```largest_loss``` which would take ```pricesLst``` as a parameter, and left it empty at first so I could start with the test case.

### Creating the Test Case

For the test case I needed to generate numbers, to go in the ```pricesLst```. I Googled how to generate a list of numbers, and ```range()``` seemed like the most popular option.

I used the [Python.org](https://docs.python.org/2/library/functions.html?highlight=range#range) documentation and [this website](https://www.science-emergence.com/Articles/How-to-create-a-list-of-numbers-in-python-/) to build a ```pricesLst``` test unit using ```range()```.

I also realised that I wanted the number to be created randomly, and decided to use the [```random``` module](https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python) following some research.

To put it all together I used [this](https://stackoverflow.com/questions/22842289/generate-n-unique-random-numbers-within-a-range) Stackoverflow answer.

Then, using the range created for ```pricesLst```, I thought the easiest way of checking for the highest loss would be to simply subtract ```pricesLst[index2]``` from ```pricesLst[index1]```, where ```index1``` is less than ```index2```. I used [this Medium article](https://medium.freecodecamp.org/learning-to-test-with-python-997ace2d8abe) for guidance through building my tests. I also decided to split my function and test cases into two separate files so that I could follow the article more easily.

#### Fixing the test case

I realised that creating a random sample for a test case would not work, as I needed to have specific test data that I knew to be correct in order to run the test and make sure it works. So I manually set a small range of data in a list, using [this link](https://www.programiz.com/python-programming/list) for guidance. (I left in, but commented out, my old code for creating a random sample so my thought process was clear.)

### Writing the function

I first ensured that if the length of the list is less than 2 that a result of 0 would be returned, as it would be impossible to get a loss comparison in this situation. I assigned this to a variable called ```largest_loss```. I didn't realise that I needed a colon after the 2 at first, which resulted in an error.

I wanted to iterate over the list of numbers created, which I did using one of the examples in [this](https://www.science-emergence.com/Articles/How-to-create-a-list-of-numbers-in-python-/) website for guidance. The list had to be the length of ```pricesLst```, which I passed as an argument to the function ```len()``` which I read about [here](https://www.quora.com/How-do-you-get-the-length-of-a-list-in-Python).

I then subtracted ```index2``` from ```index1``` and assigned that to a new variable called ```calculating_loss```. At first I got the indexes the wrong way around, so had to swap them after testing.

If ```calculating_loss``` was bigger than ```largest_loss```, that would mean that the two indexes had been successfully compared. This meant that the largest loss had been found, so I reassigned the value of ```calculating_loss``` to ```largest_loss``` and returned it.

### Running the tests

When I went to run my test, I learned the spectacularly hard way that Python is strict on indentation. I had no idea how to format my code, so this took me a lot of Googling. I left my old code in commented out below for comparison.
