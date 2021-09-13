import functions

# call function that returns a dictionary of the relevant weather values
# call function that returns calculated score based on dictionary
# returns values to be printed in main
def calculate():
    weather = functions.get_weather()

    score = functions.calculate_score(weather)

    return functions.interpret_score(score)
