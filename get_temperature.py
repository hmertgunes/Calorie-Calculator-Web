import requests
from selectorlib import Extractor

h = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}


class Temperature:
    url = " https://www.timeanddate.com/weather/"

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def build_url(self):
        current_url = self.url + self.country + "/" + self.city
        return current_url

    def get_temp(self):
        extractor = Extractor.from_yaml_file("temperature.yaml")
        page = requests.get(self.build_url(), headers=h)
        c = page.text
        raw_content = extractor.extract(c)
        return raw_content

    def get(self):
        scraped_content = self.get_temp()
        return float(scraped_content["temperature"].replace("°C", "").strip())


if __name__ == "__main__":
    temperature = Temperature(country="turkey", city="istanbul")
    print(temperature.get_temp())
