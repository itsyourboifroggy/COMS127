# Jack Byboth section 2 3/26/24
# displays scores from the studentdata file that are lower than the threshold value input from the user

def takeInput():        
    thold = int(input("Input threshold value: "))            # takes the input for the threshold tested
    return thold 



def main():

    thold2 = takeInput()                                 # sets thold2 to the value taken from the input function
    with open("studentData.txt", "r") as d:         # uses studentData file to be read as d 
     
        for i in d:                                 # runs the fucntion by amount of items in d 
            
            s = i.strip().split()                   # sets variable s equal to the line its currently running?                                
            if len(s) >= 2:                         # checks if the line has greater than or equal to 2 values ensuring it is not just the name
                s_name = s[0]                       # sets the variable s_name equal to the first value in the list (the students name)
                m = [int(i) for i in s[1:]]            # sets the variable m equal to the list s after index 1 and converts it into an int
            var = sum(1 for score in m if score >= thold2)      # sets var equal to the sum of the amount of answers greater than the inputted threshold value 
            print(f"{s_name} has {var} scores >= {thold2}")         # prints the s_name variable, the sum, and the threshold value together
            
    


if __name__ == "__main__":
    main()