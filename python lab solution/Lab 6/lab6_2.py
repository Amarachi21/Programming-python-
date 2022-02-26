def safe_input(prompt, prompt_type):  # prompt_type: str, int, float

    if type(prompt) == prompt_type:
        return prompt

    while True:
        try:
            converted = prompt_type(prompt)  # int(prompt), float(prompt), str(prompt)
        except ValueError:
            print(prompt, "cannot be converted to", prompt_type)
            prompt = input("Please input a new prompt: ")
        else:
            return converted


# Main code
number = safe_input(input("Please enter a number: "), int)
floating_point = safe_input(input("Please enter a float: "), float)
string = safe_input(input("Please enter a string: "), str)
