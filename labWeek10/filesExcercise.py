# Jack Byboth section 2 3/26/24
# placeholder   
def studentId():                                                                
    with open("students.txt", "r") as idList:                                   # opens students.txt in read mode as the name idlist
        
        lines = idList.readlines()[1:]                                          # sets variable lines euqal to all lines idlist after index 1
        s_id = [line.strip().split(',')[0] for line in lines]                   # sets variable s_id equal to each line in lines with the 
                                                                                # whitespace stripped and makes them individual strings in the list while making the spaces contain a comma
        names = {line.strip().split(',')[0]: line.strip().split(',')[1] for line in lines}     # does the same thing as previous but to take the names


    return s_id, names

def assignments():
    s_id2, names2 = studentId()              # sets the 2 variables equal to the returned values in the function studentid
    scores_dict = {student_id: [] for student_id in s_id2}  

    with open("scores.txt", "r") as scoreFile:
          
        var2 = scoreFile.readlines()[1:]
        
        for i in var2:
    
            parts = i.strip().split(',')
            s_id3 = parts[0]
            score = int(parts[2])

            if s_id3 in s_id2:
                scores_dict[s_id3].append(score)
    with open("grades.txt", "w") as newFile:
        newFile.write("Student ID,Name,Total Scores,Sum of All Scores,Score Average\n")
    
        for student_id, scores in scores_dict.items():
            total_scores = len(scores)
            sum_of_scores = sum(scores)
            score_average = sum_of_scores / total_scores if total_scores > 0 else 0
            student_name = names2.get(student_id, "Unknown")
            newFile.write(f"{student_id},{student_name},{total_scores},{sum_of_scores},{score_average:.1f}\n")
        
def main():
    assignments()




if __name__ == "__main__":
    main()

