

class ResponseValidator:
    def __init__(self, prompt):
        self.prompt = prompt
        
    def yesNoValidate(self,yesReturnValue=True, noReturnValue=False):
        yesResponses = ['yes', 'y', 'ye', 'yep', 'sure', 'ok', 'okay']
        noResponses = ['no', 'n', 'nah', 'nope', 'never', 'not really']
        while True:
            response = input(self.prompt).strip().lower()
            if response in yesResponses:
                return yesReturnValue
            elif response in noResponses:
                return noReturnValue
            else:
                print("Invalid response. Please answer with 'yes' or 'no'.")
    def intValidate(self, min_value=None, max_value=None):
        while True:
            try:
                response = int(input(self.prompt).strip())
                if (min_value is not None and response < min_value) or (max_value is not None and response > max_value):
                    print(f"Please enter a number between {min_value} and {max_value}.")
                else:
                    return response
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    def strValidate(self, min_char_length=0, max_char_length=float('inf'), min_word_length=0, max_word_length=float('inf'), regex=None, rexexFailiedMessage=None, allowNumbers=False, allowOnlyNumbers=False):
        if regex is not None:
            import re
            pattern = re.compile(regex)
        else:
            pattern = None
        while True:
            response = input(self.prompt).strip()
            if len(response) < min_char_length:
                print(f"Input must be at least {min_char_length} characters long.")
            elif len(response) > max_char_length:
                print(f"Input must be no more than {max_char_length} characters long.")
            elif len(response.split()) < min_word_length:
                print(f"Input must contain at least {min_word_length} words.")
            elif len(response.split()) > max_word_length:
                print(f"Input must contain no more than {max_word_length} words.")
            elif not allowOnlyNumbers and response.isdigit():
                print("Input may not be only numbers.")
            elif not allowNumbers and any(char.isdigit() for char in response):
                print("Input many not contain numbers.")
            elif pattern and not pattern.match(response):
                if rexexFailiedMessage is not None:
                    print(rexexFailiedMessage)
                else:
                    print("Input does not match the required format.")
            else:
                return response