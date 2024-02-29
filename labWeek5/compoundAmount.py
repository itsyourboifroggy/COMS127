# Jack Byboth 2/6/24 section 2
# takes 5 inputs and puts them into the formula
# CalculatorSoup, L. (2023, November 10). Compound Interest Calculator. CalculatorSoup. 
# https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php#:~:text=The%20basic%20compound%20interest%20formula,left%20side%20of%20the%20equation.
# accessed 2/6/24
def compoundAmount(r, n, p, t):
   

    rate = int(r)
    number_Compounds = int(n)
    principal = int(p)
    time = int(t)

    print(rate * (1 + (rate/100) / number_Compounds)**(number_Compounds * time))

def main():
    rate = input("interest rate: ")
    number_Compounds = input("Times compounded: ")
    principal = input("starting amount: ")
    time = input("time in years")
    compoundAmount(rate, number_Compounds, principal, time)

if __name__ == "__main__":
    main()