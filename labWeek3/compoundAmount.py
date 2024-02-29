# Jack Byboth 2/6/24 section 2
# takes 5 inputs and puts them into the formula
# CalculatorSoup, L. (2023, November 10). Compound Interest Calculator. CalculatorSoup. 
# https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php#:~:text=The%20basic%20compound%20interest%20formula,left%20side%20of%20the%20equation.
# accessed 2/6/24

rate = input("interest rate: ")
number_Compounds = input("Times compounded: ")
principal = input("starting amount: ")
time = input("time in years")

converter1 = int(rate)
converter2 = int(number_Compounds)
converter3 = int(principal)
converter4 = int(time)

print(converter3 * (1 + (converter1/100) / converter2)**(converter2 * converter4))