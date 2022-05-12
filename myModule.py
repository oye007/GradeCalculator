def validateInputs(scores):
    error = False
    errorMsg = ""

    # Loop through scores, set error message if any
    for x, y in scores.items():
        print(x, y)
        if len(y) != 0:
            try:
                int(y)
                if ( int(y) > 0 ):
                    if ( int(y) <= 100 ):
                        pass

                    else:
                        errorMsg += x +" must not be more than 100 \n"
                        error = True

                else:
                    errorMsg += x +" must be greater than zero \n"
                    error = True

            except ValueError:
                errorMsg += x +" must be a whole number\n"
                error = True
                    
        else:
            errorMsg += x +" can not be empty \n"
            error = True

    
    # set input validation result
    inputStatus = {
        "error": error,
        "errorMsg": errorMsg
    }

    return inputStatus



def Calculator(scores):
    # initialize scores
    scoreA = scores["scoreA"]
    scoreB = scores["scoreB"]
    scoreC = scores["scoreC"]
    scoreD = scores["scoreD"]
    scoreE = scores["scoreE"]


    # calculate grade
    total, average, percentage, grade = None, None, None, None
    total = int(scoreA) + int(scoreB) + int(scoreB) + int(scoreB) + int(scoreB)
    average = total / 5.0
    percentage = (total / 500.0) * 100

    if average >= 90:
        grade = 'A'
    elif average >= 80 and average < 90:
        grade = 'B'
    elif average >= 70 and average < 80:
        grade = 'C'
    elif average >= 60 and average < 70:
        grade = 'D'
    else:
        grade = 'E'
    
    # set result values
    percentage_msg = str(percentage) + "%"
    results = {
        "percentage": percentage_msg,
        "total": total,
        "average": average,
        "grade": grade
    }
    return results