# Testing the SI507F17_project_cards.py file

This is code for a very fun card game. It is pretty trivial so run it and have fun. The project is also an attempt by a mediocre (even novice) programmer to write a bunch of tests for a Card game script. The script has at least 3 bugs, therefore the goal of the tests were to uncover the bugs.
In the test file there are two class defined: the first class are the test functions for the class Cards and the second are test functions for Deck. The last also includes code to test the game.  

## Getting Started & Installing

I would suggest running this on a virtual environment. For some reason you might have to download the requests module. If this is the case used this code in your terminal:

```
pip3 install requests
import requests
```



## Running the tests

Just run the test file titled: "SI507F17_project_tests.py". Make sure you place the file and the other files in this repository in the same directory.


### Break down into end to end tests

The first set of tests have the class description:

```
class ClassTests(uniitest.Testcase):
```

The second set of tests have the class description:

```
class DeckTests(uniitest.Testcase):
```
It tests to ensure that the functions in the file do exactly what they are supposed to do. Deck is a class that instiates objects that are composed of Class objects. These test are intended to make sure things go smoothly.  



## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* The Python IDLE and unreasonable amounts of time spent doing a weeks worth of work in 2 days. :)

## Versioning

The one and only version. 

## Authors

* **Innocent Obi Jr**

## Acknowledgments

* The Internet
* Google
* Murach's Python Textbook
