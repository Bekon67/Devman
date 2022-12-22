import requests


def get_response():
    response_for_print = []
    locations = ['Лондон', 'SVO', 'Череповец']
    for location in locations:
        response = requests.get(f'https://wttr.in/{location}?nTqmM&lang=ru')
        response.raise_for_status()
        response_for_print.append(response.text)
    return response_for_print


def main():
    print(*get_response())


if __name__ == '__main__':
    main()
