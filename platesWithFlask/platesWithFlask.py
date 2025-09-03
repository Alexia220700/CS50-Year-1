from flask import Flask, request, render_template_string

# initialize flask app
app = Flask(__name__)

# function to validate car license plate
def is_valid(s):
    # Check if the car plate has the correct number of characters
    if len(s) < 2 or len(s) > 6:
        return False

    # check if the first two characters are letters and uppercase
    if not (s[0].isalpha() and s[0].isupper()):
        return False
    if not (s[1].isalpha() and s[1].isupper()):
        return False

    # check if all characters are letters
    nrLetters = 0
    nrCharacters = 0

    # iterate through each character in the string
    for i, char in enumerate(s):
        nrCharacters += 1
        if char.isalpha():
            nrLetters += 1
        else:
            break

    # if all characters are letters, it's a valid license plate
    if nrCharacters == nrLetters:
        return True

    # check if the numbers come at the end of the license plate
    for i, char in enumerate(s):
        if s[i].isnumeric():
            # store the index of the first numeric character
            aux = i
            # if the first number is '0', it's invalid
            if s[aux] == '0':
                return False
            break

    # check if the characters after the first number are all numbers
    # starting from the first character after the first number
    for i, char in enumerate(s[aux + 1:]):
        if not char.isnumeric():
            return False

    # If all checks are passed
    return True


# HTML template for the form and result display
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <!-- ensure proper rendering and touch zooming on mobile devices -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car License Plate Validator</title>
</head>

<body>
    <h1>Car Plate Validator</h1>

    <!-- form to input the car license plate -->
    <!-- using the POST method to send data to the server -->
    <form method="POST">

        <!-- Label for the input field -->
        <label for="plate">Enter car plate:</label>

        <!-- the "id" attribute links the input to the label -->
        <!-- the "name" attribute is used to identify the input data when the form is submitted -->
        <!-- the "required" attribute ensures the user cannot submit the form without filling this field -->
        <input type="text" id="plate" name="plate" required>

        <button type="submit">Validate plate</button>
    </form>

    <!-- display the validation result if available -->
    <!-- tag used for control structures like loops, conditionals -->
    <!-- Python, None is a special constant that represents the absence of a value or a null value -->
    {% if result is not none %}


        <p>Result: {{ result }}</p>
    {% endif %}
</body>

</html>
'''

# route for the main page, handles both GET and POST requests
@app.route("/", methods=["GET", "POST"])
def index():
    # initialize the result as None
    result = None
    if request.method == "POST":

        # get the car plate from the form input
        plate = request.form.get("plate", "").strip()

        # validate the car plate using the is_valid function
        if is_valid(plate):
            result = "Valid"
        else:
            result = "Invalid"

    # render the HTML template with the result
    return render_template_string(HTML_TEMPLATE, result=result)

# run the Flask application
if __name__ == "__main__":
    app.run(debug = True)
