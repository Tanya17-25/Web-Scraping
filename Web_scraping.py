import requests
import lxml
from bs4 import BeautifulSoup
import csv
import time
import random

#url_text = 'https://www.booking.com/searchresults.en-gb.html?ss=Dehradun&efdco=1&label=en-in-booking-desktop-CmH43mrsjzqEEFQPgVycoAS652796016141%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9297911%3Ali%3Adec%3Adm&aid=2311236&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-2106102&dest_type=city&checkin=2025-08-01&checkout=2025-08-02&group_adults=2&no_rooms=1&group_children=0'



def web_scrapper2(web_url, name):

    #Greetings

    print("Thank you for sharing the url and file name!\n⏳\nReading the Content!")
    num = random.randint(3,7)

    #processing
    time.sleep(num)

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}


    response = requests.get(web_url, headers=header)

    if response.status_code == 200:
           print('Connected to the website')
           html_content = response.text

           #Creating Soup
           soup = BeautifulSoup(html_content,'lxml')
           #print(soup.prettify())

           #main containers
           hotel_divs = soup.find_all('div', role = "listitem")


           with open(f'{name}.csv', 'w',  encoding='utf-8', newline='') as file_csv:
               writer = csv.writer(file_csv)

               #adding header
               writer.writerow(['Hotel Name','Locality','Price','Rating','Reviews','Link'])

               for hotel in hotel_divs:
                   hotel_name = hotel.find('div', class_="b87c397a13 a3e0b4ffd1").text.strip()
                   hotel_name if hotel_name else 'NA'

                   location = hotel.find('span', class_="d823fbbeed f9b3563dd4").text.strip()
                   location if location else 'NA'

                   #price

                   price = hotel.find('span', class_="b87c397a13 f2f358d1de ab607752a2").text.strip()
                   price if price else 'NA'


                   rating = hotel.find('div', class_="f63b14ab7a f546354b44 becbee2f63").text.strip()
                   rating if rating else 'NA'

                   score = hotel.find('div', class_="fff1944c52 fb14de7f14 eaa8455879").text.strip()
                   score if score else 'NA'

                   #getting url
                   link = hotel.find('a',href=True).get('href')

                   #saving the file in csv
                   writer.writerow([hotel_name,location,price,rating,score,link])

               #print(hotel_name)
               #print(location)
               #print(price)
               #print(rating)
               #print(score)
               #print(link)
               #print('')

    else:
        print(f"Connection failed: {response.status_code}")


#if using this script directly then the below task will be executed

if __name__ == '__main__':
    url=input("Please enter the url you wish to scrape: ")
    file_name=input("Please enter the file name: ")

    #calling the function
    web_scrapper2(url, file_name)
