import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
# def 
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip=0
    tax=0
    tip = (tip_percent/100) * meal_cost
    tax = (tax_percent/100) * meal_cost
    final = round(meal_cost+tip+tax)
    print(final)
    
