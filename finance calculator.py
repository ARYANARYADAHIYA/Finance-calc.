import math

def simple_interest():
    p = float(input("Enter Principal Amount: "))
    r = float(input("Enter Rate of Interest (%): "))
    t = float(input("Enter Time (years): "))
    si = (p * r * t) / 100
    print(f"\nSimple Interest = {si:.2f}")
    print(f"Total Amount = {p + si:.2f}")

def compound_interest():
    p = float(input("Enter Principal Amount: "))
    r = float(input("Enter Annual Interest Rate (%): "))
    t = float(input("Enter Time (years): "))
    n = int(input("Number of times interest is compounded per year: "))
    amount = p * (1 + r / (100 * n)) ** (n * t)
    ci = amount - p
    print(f"\nCompound Interest = {ci:.2f}")
    print(f"Total Amount = {amount:.2f}")

def area_circle():
    radius = float(input("Enter Radius: "))
    area = math.pi * radius ** 2
    print(f"Area of Circle = {area:.2f}")

def area_rectangle():
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))
    print(f"Area of Rectangle = {length * width:.2f}")

def perimeter_rectangle():
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))
    print(f"Perimeter = {2 * (length + width):.2f}")

def bmi():
    weight = float(input("Enter Weight (kg): "))
    height = float(input("Enter Height (m): "))
    bmi_value = weight / (height ** 2)
    print(f"BMI = {bmi_value:.2f}")

def percentage():
    obtained = float(input("Enter Obtained Marks: "))
    total = float(input("Enter Total Marks: "))
    print(f"Percentage = {(obtained / total) * 100:.2f}%")

def celsius_to_fahrenheit():
    c = float(input("Enter Temperature in Celsius: "))
    f = (c * 9 / 5) + 32
    print(f"Temperature = {f:.2f} °F")

def fahrenheit_to_celsius():
    f = float(input("Enter Temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print(f"Temperature = {c:.2f} °C")

def average_numbers():
    nums = input("Enter numbers separated by spaces: ")
    values = list(map(float, nums.split()))
    avg = sum(values) / len(values)
    print(f"Average = {avg:.2f}")

while True:
    print("\n========== MULTI CALCULATOR ==========")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Area of Circle")
    print("4. Area of Rectangle")
    print("5. Perimeter of Rectangle")
    print("6. BMI Calculator")
    print("7. Percentage Calculator")
    print("8. Celsius to Fahrenheit")
    print("9. Fahrenheit to Celsius")
    print("10. Average of Numbers")
    print("11. Exit")

    choice = input("\nEnter your choice (1-11): ")

    if choice == "1":
        simple_interest()
    elif choice == "2":
        compound_interest()
    elif choice == "3":
        area_circle()
    elif choice == "4":
        area_rectangle()
    elif choice == "5":
        perimeter_rectangle()
    elif choice == "6":
        bmi()
    elif choice == "7":
        percentage()
    elif choice == "8":
        celsius_to_fahrenheit()
    elif choice == "9":
        fahrenheit_to_celsius()
    elif choice == "10":
        average_numbers()
    elif choice == "11":
        print("Thank you for using the calculator!")
        break
    else:
        print("Invalid choice. Please try again.")
