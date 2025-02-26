import requests

def guess_color(color, server_url = 'http://localhost:5000/get_random_color'):
    payload = {'color' : color}
    try:
        response = requests.post(server_url, json = payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'Http Error occurence: {http_err} - {response.json().get("error")}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err} ')
        return None
    else:
        data = response.json()
        return data.get('random_color')

if __name__ == '__main__':
    try:
        colorInput = input("Enter your color: ")
    except valueErr:
        print("Please enter a valid color")
        exit(1)
    random_color = guess_color(colorInput)
    if random_color is not None:
        print(f"Your guess is {colorInput} our server's color is {randomColor}")
        