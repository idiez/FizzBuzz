from lettuce import *
from mathclass.fizzbuzz import *

@step('I have the number (\d+)')
def have_the_number(step, number):
    world.number = int(number)

@step('I check whether is Fizz')
def check_whether_is_fizz(step):
    world.fizz = isFizz(world.number)

@step('I see Fizz')
def check_number(step):
    assert world.fizz == True

def factorial(number):
    return -1