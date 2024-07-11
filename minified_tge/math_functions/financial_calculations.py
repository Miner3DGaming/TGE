def calculate_present_value(principal,rate,years):'\n    Calculate the present value of an investment based on the given parameters.\n\n    Parameters:\n    principal (float): The initial investment amount.\n    rate (float): The annual interest rate as a percentage.\n    years (int): The number of years the investment will be held.\n\n    Returns:\n    float: The present value of the investment after the specified number of years.\n    ';return principal*pow(1+rate/100,years)
def percentage_increase(old_grade,new_grade):'\n    Calculate the percentage increase from an old grade to a new grade.\n\n    Parameters:\n        old_grade (float): The initial grade.\n        new_grade (float): The updated grade.\n\n    Returns:\n        float: The percentage increase from the old grade to the new grade.\n               The result is represented as a decimal value (e.g., 0.10 for 10% increase).\n\n    Example:\n        >>> percentage_increase(80.0, 90.0)\n        0.125  # 12.5% increase from 80.0 to 90.0\n    ';A=old_grade;return(new_grade-A)/A
def percentage_decrease(old_grade,new_grade):'\n    Calculate the percentage decrease between an old grade and a new grade.\n\n    Parameters:\n        old_grade (float): The original grade or value.\n        new_grade (float): The new grade or value.\n\n    Returns:\n        float: The percentage decrease as a decimal value.\n    ';A=old_grade;return(A-new_grade)/A
def discount_price(price,discount):'\n    Calculate the discounted price based on the original price and discount percentage.\n\n    Parameters:\n    price (float): The original price before applying the discount.\n    discount (float): The discount percentage to be applied, expressed as a decimal value.\n\n    Returns:\n    float: The discounted price calculated by multiplying the original price by (1 - discount).\n    ';return price*(1-discount)
def body_mass_index(weight,height):"\n    Calculate the Body Mass Index (BMI) using weight and height.\n\n    The Body Mass Index (BMI) is a numerical value calculated using a person's\n    weight (in kilograms) divided by the square of their height (in meters).\n\n    Args:\n        weight (float): The weight of the individual in kilograms.\n        height (float): The height of the individual in meters.\n\n    Returns:\n        float: The Body Mass Index (BMI) calculated as weight divided by height squared.\n    ";return weight/height**2