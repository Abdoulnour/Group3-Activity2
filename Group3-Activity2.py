""""
Names:- AbdoulNour Ismail, Zayed shatat ,Sama nimer

GitHub:- https://github.com/Abdoulnour/Group3-Activity2.git
"""

"How to change the currency to other currency(AED,ERU,GBP,USD)"
""" AED to ERU = 0.25
    AED to GBP = 0.22
    AED to USD = 0.27
    ERU to AED = 3.98
    GBP to AED = 4.65
    USD to AED = 3.67 """


"changing from AED to ERU"
def convert_AED_to_ERU(mony):
    AED_to_ERU = 0.25
    return float(mony*AED_to_ERU) #we should use float because of decimal numbers

"changing from AED to GBP"
def convert_AED_to_GBP(mony):
    AED_to_GBP = 0.22
    return float(mony*AED_to_GBP) #we should use float because of decimal numbers

"changing from AED to USD"
def convert_AED_to_USD(mony):
    AED_to_USD = 0.27
    return float(mony*AED_to_USD) #we should use float because of decimal numbers

"changing from EUR to AED"
def convert_ERU_to_AED(mony):
    ERU_to_AED = 3.98
    return float(mony*ERU_to_AED) #we should use float because of decimal numbers

"changing from GBP to AED"
def convert_GBP_to_AED(mony):
    GBP_to_AED = 4.65
    return float(mony*GBP_to_AED) #we should use float because of decimal numbers

"changing from USD to AED"
def convert_USD_to_AED(mony):
    USD_to_AED = 3.67
    return float(mony*USD_to_AED) #we should use float because of decimal numbers

"""The main function is to execute the currency converter"""
def main():
    print("Main Menu")
    print("Welcome to Currency Converter")
    print("---------------------------------")

    while True:
        print("Select the conversion direction:")
        print("1. AED to other currencies")
        print("2. Other currencies to AED")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            amount = float(input("Enter your amount you want to convert: "))
            print("\nConvert AED to:")
            print("1. Euro (EUR)")
            print("2. British Pound (GBP)")
            print("3. US Dollar (USD)")
            print("4. Go back to Main Menu")

            sub_choice = input("Enter your choice (1/2/3/4): ")

            if sub_choice == '1':
                result = convert_AED_to_ERU(amount)
                print(f"The converted amount is: {result}")
            elif sub_choice == '2':
                result = convert_AED_to_GBP(amount)
                print(f"The converted amount is: {result}")
            elif sub_choice == '3':
                result = convert_AED_to_USD(amount)
                print(f"The converted amount is: {result}")
            elif sub_choice == '4':
                continue  # Going back to the main menu

        elif choice == '2':
            amount = float(input("Enter your amount you want to convert: "))
            print("\nConvert from:")
            print("1. Euro (EUR)")
            print("2. British Pound (GBP)")
            print("3. US Dollar (USD)")
            print("4. Go back to Main Menu")

            sub_choice = input("Enter your choice (1/2/3/4): ")

            if sub_choice == '1':
                result = convert_ERU_to_AED(amount)
                print(f"The converted amount is: {result}")
            elif sub_choice == '2':
                result = convert_GBP_to_AED(amount)
                print(f"The converted amount is: {result}")
            elif sub_choice == '3':
                result = convert_USD_to_AED(amount)
                print(f"The converted amount is: {result}")
            elif sub_choice == '4':
                continue  # Going back to the main menu

        elif choice == '3':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
