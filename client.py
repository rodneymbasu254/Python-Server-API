import requests

def get_circle_area(radius, server_url = 'http://localhost:5000/calculate_area'):
    payload = {'radius': radius}
    try:
        response = requests.post(server_url, json=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurence: {http_err} - {response.json().get("error")}')
        return None
    except Exception as err:
        print(f'Other error occurrence: {err}')
        return None
    else:
        data = response.json()
        return data.get('area')

if __name__ == '__main__':
    try:
        radius_input = float(input('Please enter the radius: '))
    except ValueError:
        print('please enter a valid value: ')
        exit(1)

    area = get_circle_area(radius_input)
    if area is not None:
        print(f'The area of the circle with a radius of {radius_input} is: {area: .2f}') 
