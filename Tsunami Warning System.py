
from bs4 import BeautifulSoup
import requests
from pygame import mixer

if __name__ == '__main__':
    High_Tide = ''
    High_Tide_Limit = '20.00'
    Low_Tide = ''
    Low_Tide_Limit = '2.00'

#it's play the siren for High Tide
def alert():
   mixer.init()
   alert = mixer.Sound('Sirens_2.wav')
   alert.play()

#it's play the sound for very low tide
def alert1():
   mixer.init()
   alert=mixer.Sound('beep-07.wav')
   alert.play()


while True:
    url = "https://www.tide-forecast.com/locations/Bombay-India/tides/latest"
    data = requests.get(url)

    soup = BeautifulSoup(data.text,'html.parser')

    hightide = soup.select('.level > span')
    if hightide:
        High_Tide = hightide[1].text.strip('ft')
        print(High_Tide," - High_tide")


    lowtide = soup.select('.level > span')
    if lowtide:
        Low_Tide = hightide[0].text.strip('ft')
        print(Low_Tide," - Low_tide")


    if High_Tide > High_Tide_Limit:
        print("Water Level Is Too High")
        alert() #Actuators For High Tide
    elif Low_Tide < Low_Tide_Limit:
        print("Water Level Is Low")
        alert1() #Actuators For Low Tide
    else:
        print("All Right")




'''
print(soup.prettify())
level = soup.find_all(class_='level')


for imp in soup.find_all('span',class_='imperial'):
    for hightide in imp:
        hightide = imp.text.strip('ft')
        High_Tide = [hightide.strip(' ')]
        print(High_Tide)

filename = 'tide.csv'
with open(filename, 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Name', 'Profession'])
    filewriter.writerow(['Derek', 'Software Developer'])
    filewriter.writerow(['Steve', 'Software Developer'])
    filewriter.writerow(['Paul', 'Manager'])
'''



