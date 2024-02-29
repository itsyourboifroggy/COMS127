#Jack Byboth 1/31/24 section 2
#allows for the input of number to be made into an area
#Kumar, A., & Kumar, A. (2023, March 23). What is Area in Math? Definition, Formulas, Shapes, Examples. SplashLearn - Math Vocabulary. 
#https://www.splashlearn.com/math-vocabulary/geometry/area#:~:text=The%20table%20below%20summarizes%20some,r%202%20(%20%CF%80%20%3D%203.14%20) Accessed 2/6/24

def areaOfRectangle(base, height):
    
    converter1 = (base)
    converter2 = (height)

    print(converter1 * converter2)
def main():
    base = int(input("Base of Rectangle: "))
    height = int(input("Height of Rectangle: "))
    value = areaOfRectangle(base, height)
    
if __name__ == "__main__":
    main()