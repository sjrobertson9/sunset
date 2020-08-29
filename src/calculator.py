import functions

# call function that returns a dictionary of the relevant weather values
# call function that returns calculated score based on dictionary
# returns values to be printed in main
def calculate():
    weather = functions.get_weather()

    # dictionary of values to be inserted in default message
    # date
    # time
    # score_message
    # score_factors
    
    score = functions.get_score(weather)

    return weather #score