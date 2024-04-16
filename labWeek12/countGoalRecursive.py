# Jack Byboth 4/10/24

def countDownGoalRecursive(n, goal):
    if n < goal:
        return
    else:
        print(n)
        countDownGoalRecursive(n-1, goal)
    return n

def countupGoalRecursive(n, goal):
    if n < goal:
        return
    else:
        countupGoalRecursive(n-1, goal)
        print(n)
    return n

def main():
    

    n = int(input("Input:"))
    goal = int(input("Input:"))
    countDownGoalRecursive(n, goal)
    countupGoalRecursive(n, goal)


if __name__ == "__main__":
    main()