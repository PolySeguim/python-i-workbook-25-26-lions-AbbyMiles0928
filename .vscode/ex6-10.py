"""
Exercise 6: Tax and Tip
The program you create for this exercise will begin by reading the cost
of a meal ordered at a restaurant from the user.  Then your program will
compute the tax and tip for the meal.  Use your local tax rate when 
computing the amount of tax owing.  Compute the tip as 18 percent of  the 
meal amount (without tax).  The output from your program should include
both the tax and the tip.  Format the output so that all of the values
are displayed using two decimal places.  (17 lines)
"""
def tax_and_tip():
    meal_cost = float(input("Enter the cost of the meal: "))
    tax_rate = float(input("Enter the tax rate: "))
    tax = meal_cost * (tax_rate / 100)
    tip = meal_cost * 0.18
    total_cost = meal_cost + tax + tip
    print(round("Tax: $" + format(tax, '.2f'), 2))
    print(round("Tip: $" + format(tip, '.2f'), 2))
    print(round("Total cost: $" + format(total_cost, '.2f'), 2))
#tax_and_tip()
"""
Exercise 7:  Sum of the First n Positive Integers
Write a program that reads a positive integer, n, from the user and 
then displays the sum of all the integers from 1 to n.  The sum of the 
first n positive integers can be computed using the formula:
sum = (n*(n+1))/2
(12 lines)
"""
def sum_of_first_n_positive_integers():
    n = int(input("Enter a positive integer: "))
    sum = (n * (n + 1)) / 2
    print("The sum of the first " + str(n) + " positive integers is " + str(sum))
#sum_of_first_n_positive_integers()
"""
Exercise 8:  Widgets and Gizmos
An online retailer sells two products:   widgets and gizmos.  Each widget 
weighs 75 grams.  Each gizmo weighs 112 grams.  Write a program that reads
the number of gizmos in an order from the user.  Then your program should 
compute and display the total weight of the order.  (15 lines)

"""
def widgets_and_gizmos():
    num_widgets = int(input("Enter the number of widgets: "))
    num_gizmos = int(input("Enter the number of gizmos: "))
    total_weight = (num_widgets * 75) + (num_gizmos * 112)
    print("The total weight is " + str(total_weight) + " grams")
"""
Exercise 9:  Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent
interest per year.  The interest that you earn is paid at the end of the year, 
and is added to the balance of the savings account.  Write a program that begins
by reading the amount of money deposited into the account from the user.  Then 
your program should compute and display the amount in the savings account after
1, 2, and 3 years.  Display each amount so that it is rounded to 2 decimal 
places.  (19 lines)
"""
def compound_interest():
    starting_amount = float(input("Enter the amount of money deposited: "))
    interest_rate = 0.04
    amount_after_1_year = starting_amount * (1 + interest_rate)
    amount_after_2_years = amount_after_1_year * (1 + interest_rate)
    amount_after_3_years = amount_after_2_years * (1 + interest_rate)
    print("Amount after 1 year: " + str(round(amount_after_1_year, 2)))
    print("Amount after 2 years: " + str(round(amount_after_2_years, 2)))
    print("Amount after 3 years: " + str(round(amount_after_3_years, 2)))

"""
Exercise 10:  Arithmetic
Create a program that reads two integers, a and b, from the user.  Your program
should compute and display:
- the sum of a and b
- the difference when b is subtracted from a
- the product of a and b
- the quotient when a is divided by b
- the remainder when a is divided by b
- the result of log10 a
- the result of a to the power of b

Hint:  you will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""
def arithmetic():
    import math
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    sum = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    remainder = a % b
    log10_a = math.log10(a)
    a_to_the_power_of_b = a ** b
    print("Sum: " + str(sum))
    print("Difference: " + str(difference))
    print("Product: " + str(product))
    print("Quotient: " + str(quotient))
    print("Remainder: " + str(remainder))
    print("Log10 of a: " + str(log10_a))
    print("a to the power of b: " + str(a_to_the_power_of_b))
#arithmetic()

