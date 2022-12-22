import requests


def main():
    while True:
        lang = input('Выберите язык представления информации (en/ru): ')
        try:
            if lang not in ['en', 'ru']:
                raise ValueError
            break
        except ValueError:
            print('Вы ошиблись. Попробуйте ещё раз...')

    while True:
        try:
            location = input('Введите Вашу локацию (Лондон, Череповец, аэропорт Шереметьево(SVO): ')
            domain = 'https://wttr.in/'
            url = f'https://wttr.in/{location}'

            # TODO заголовки убрать совсем?
            # headers = {
            #     'Accept': '* / *',
            #     'User-Agent': 'curl'
            # }
            params = {
                'nTqmM': '',
                'lang': lang,
            }
            response = requests.get(
                url,
                params=params,
                # headers=headers
            )
            response.raise_for_status()
            print(response.url)
            break
        except requests.exceptions.HTTPError:
            print('Нет такой локации. Попробуйте ещё раз...')

    return response


if __name__ == '__main__':
    print(main().text)
