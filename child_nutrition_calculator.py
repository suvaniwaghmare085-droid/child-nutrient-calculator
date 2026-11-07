# Child Nutrition Calculator
# Calculates BMI and estimates daily calorie intake based on the assignment criteria.

def get_number(prompt, allow_zero=False):
    """Read a valid numeric value from the user."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value > 0 or (allow_zero and value == 0):
                return value
            print("Invalid input. Please enter a number greater than "
                  "or equal to zero." if allow_zero
                  else "Invalid input. Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_non_empty_text(prompt):
    """Read text that is not empty or whitespace."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def main():
    print("=" * 48)
    print("             CHILD NUTRITION CALCULATOR")
    print("=" * 48)

    # 1. Collect and validate the child's details.
    name = get_non_empty_text("Enter the child's name: ")
    age = get_number("Enter the child's age in years (0-8): ", allow_zero=True)

    while age > 8:
        print("This calculator supports ages from 0 through 8 years.")
        age = get_number("Enter the child's age in years (0-8): ",
                         allow_zero=True)

    gender = get_non_empty_text("Enter the child's gender: ")
    height = get_number("Enter height in inches: ")
    weight = get_number("Enter weight in pounds: ")

    # 2. Calculate BMI using the formula specified in the assignment.
    bmi = (weight / (height ** 2)) * 703

    # 3. Determine the recommended daily calories.
    # Age 2 belongs to the 2-4 group; age 4 belongs to the 4-8 group.
    if age < 2:
        recommended_calories = 800
    elif age < 4:
        recommended_calories = 1400
    else:
        recommended_calories = 1800

    # 4. Calories per 100 grams for each food.
    calories_per_100g = {
        "Milk": 100,
        "Egg": 155,
        "Rice": 130,
        "Lentils": 113,
        "Vegetable": 85,
        "Meat": 143
    }

    # 5. Collect food quantities and calculate calories.
    total_calories = 0.0
    food_details = {}

    print("\nEnter the quantity of each food eaten today in grams.")
    print("Enter 0 if the child did not eat a particular food.\n")

    for food, calories_per_100 in calories_per_100g.items():
        quantity = get_number(
            f"Quantity of {food} consumed (grams): ",
            allow_zero=True
        )
        food_calories = (quantity / 100) * calories_per_100
        food_details[food] = (quantity, food_calories)
        total_calories += food_calories

    # 6. Display the report.
    print("\n" + "=" * 48)
    print("                 NUTRITION REPORT")
    print("=" * 48)
    print(f"Name:   {name}")
    print(f"Age:    {age:g} years")
    print(f"Gender: {gender}")
    print(f"Height: {height:g} inches")
    print(f"Weight: {weight:g} pounds")
    print(f"BMI:    {bmi:.2f}")

    print("\nFOOD CONSUMPTION")
    print("-" * 48)
    for food, (quantity, food_calories) in food_details.items():
        print(f"{food:<12} {quantity:>8g} g  {food_calories:>10.2f} calories")

    print("-" * 48)
    print(f"Total calories consumed:      {total_calories:.2f}")
    print(f"Recommended daily calories:    {recommended_calories:.2f}")

    # 7. Compare the intake with the assignment's recommendation.
    difference = total_calories - recommended_calories

    if total_calories < recommended_calories:
        print("\nStatus: Below the recommended calorie amount.")
        print(f"Difference: {abs(difference):.2f} calories below recommendation.")
        print("This simplified comparison does not diagnose undernutrition.")
    else:
        print("\nStatus: Recommended calorie amount met or exceeded.")
        print(f"Difference: {difference:.2f} calories above recommendation.")
        print("This simplified comparison does not determine overall nutrition.")

    print("=" * 48)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram stopped. Goodbye.")
