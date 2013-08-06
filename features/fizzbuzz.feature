Feature: Check that multiples of 3 are fizz

    Scenario: Multiples of 3
        Given I have the number 6

        When I check whether is Fizz
        Then I see Fizz

        Given I have the number 9
        When I check whether is Fizz
        Then I see Fizz


        Given I have the number 33
        When I check whether is Fizz
        Then I see Fizz

        Given I have the number 5
        When I check whether is Fizz
        Then I see Fizz

#etc