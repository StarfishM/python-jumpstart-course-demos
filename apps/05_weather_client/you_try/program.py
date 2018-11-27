import requests
import bs4
import collections


WeatherReport = collections.namedtuple("WeatherReport",
                                       "cond, temp, scale, loc")


def main():
    print_the_header()
    place = input("Which city do you want the forecast for? (Berlin/Hamburg/...?)").strip().lower().replace(" ","-")
    # get user location
    print("Wait... getting your weather report... ")

    html = get_html_from_web(place)

    # parse the html
    report = get_weather_from_html(html)
    print("The Temperature in {} is {} {} and it's currently {}".format(
        report.loc,
        report.temp,
        report.scale,
        report.cond,
    ))

    # display the forecast


def print_the_header():
    print('-------------------------')
    print('      Weather client')
    print('-------------------------')
    print()


def get_html_from_web(city):
    url = "https://www.wunderground.com/weather/de/{}".format(city)
    # print(url)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])
    return response.text


def get_weather_from_html(html):

    # print(soup)
    # return soup
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, "html.parser")
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    #print(condition, temp, scale, loc)
    #return condition, temp, scale, loc
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def cleanup_text(text):
    if not text:
        return text

    text = text.strip()
    return text


# def find_city_and_country_location(loc: str):
#    parts = loc.split(',')
#    return parts[0].strip()




if __name__ == "__main__":
    main()
