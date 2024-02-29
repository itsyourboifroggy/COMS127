# Jack Byboth 2/6/24 section 2
# plugs inputs into a formula
# Website, N. (2022, December 2). What is the body mass index (BMI)? nhs.uk. 
# https://www.nhs.uk/common-health-questions/lifestyle/what-is-the-body-mass-index-bmi/#:~:text=The%20body%20mass%20index%20(BMI)%20is%20a%20measure%20that%20uses,of%2025%20means%2025kg%2Fm2.
# accessed 2/6/24

weight = input("weight: ")
height = input("height in inches: ")

converter1 = int(weight)
converter2 = int(height)

print(converter1 / (converter2 ** 2) * 703)