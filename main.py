import requests
from bs4 import BeautifulSoup
import  time
import telebot


BOT_TOKEN = ""

bot = telebot.TeleBot(BOT_TOKEN)
KEYWORDS = ["python", "flask", "vue", "tailwind", "frontend", "javascript", "jquery","fresher","frontend", "front-end", "backend", "back-end", "full stack", "full-stack",
    "web developer", "web dev",'js',"tailwind", "tailwindcss", "bootstrap", "css", "fresher", "intern", "internship", "junior", "entry-level",]


def scrap(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Referer": "https://google.com",  # Acts like a real visitor
    }

    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:

        job_dict = {}
        soup = BeautifulSoup(response.text, 'html.parser')
        headings = soup.find_all('td', class_='head')

        for index, heading in enumerate(headings):
            job_dict[f"job_{index + 1}"] = {"title": heading.text.strip()}

        company_names = soup.find_all('td', class_='date')

        for index, company_name in enumerate(company_names):
            job_dict[f"job_{index + 1}"]['company_name'] = company_name.text.strip()

        td_tags = soup.find_all("td", class_="btn-sec")

        for index, td_tag in enumerate(td_tags):
            a_tag = td_tag.find('a')
            job_dict[f"job_{index + 1}"]['detials'] = a_tag['href']

        return  job_dict.values()


    else:
        print("you got error", response.status_code)



def send_message(chatid_list):

    job_list = []
    for i in range(1, 25):
        url = f"https://infopark.in/companies/job-search?page={i}"
        time.sleep(2)
        dicts = scrap(url)
        for job in dicts:
            job_list.append({
                'title': job['title'],
                "company_name": job["company_name"],
                "details": job["detials"]
            })





    if not job_list :
        for chatid in chatid_list:
            bot.send_message(chatid,"⚠️ No new jobs found!")


    for job in job_list:
        job_title_lowercase = job['title'].lower()
        for keyword in KEYWORDS:
            if keyword in job_title_lowercase:

                message = f"*INFOPARK*📝 *{job['title']}*\n🏢 {job['company_name']}\n🔗 [Apply Here]({job['details']})"
                for chatid in chatid_list:
                    
                    bot.send_message(chatid, message, parse_mode="Markdown")
    print("Job update Sent")



# send_message()

chatid_list = []
def get_chatid():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    responese= requests.get(url)
    data = responese.json()
    chatid = data["result"][-1]["message"]["from"]["id"]
    chatid_list.append(chatid)


get_chatid()

print(chatid_list)
send_message(chatid_list)