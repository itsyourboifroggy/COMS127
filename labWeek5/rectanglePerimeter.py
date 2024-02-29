#Jack Byboth 2/6/24 section 2
#Takes the input of numbers and makes them into the perimeter
#Kumar, A., & Kumar, A. (2024, January 29). How to find perimeter? Definition, formulas, examples, facts. SplashLearn - Math Vocabulary. https://www.splashlearn.com/math-vocabulary/geometry/perimeter
#accessed 2/6/24
def rectanglePerimeter(length, width):

    converter1 = int(length)
    converter2 = int(width)

    return (converter1 + converter2) * 2


def main():
    l = int(input("Length of Rectangle: "))
    w = int(input("Width of Rectangle: "))
    value = rectanglePerimeter(l, w)
    print(value)

if __name__ == "__main__":
    main()