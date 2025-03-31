# JobRadar-
Job Alert Bot is an automated web scraper that fetches the latest job listings from the  website and sends real-time updates directly to your Telegram. Whether you're actively searching for a job or just keeping an eye on new opportunities, this bot ensures you never miss an important listing.



## Features

✅ **Automated Job Scraping** – Extracts job postings based on predefined keywords.  
✅ **Telegram Notifications** – Sends job alerts directly to your Telegram chat.  
✅ **Custom Keyword Filtering** – Matches job titles against specific keywords (e.g., Python, JavaScript, Vue, Frontend, etc.).  
✅ **Multi-Page Scraping** – Fetches job listings across multiple pages for a broader search.  
✅ **Real-Time Updates** – Ensures you get notified as soon as new job listings are available.  

---

## Installation

### Prerequisites
Ensure you have Python installed (Python 3.7 or higher). You will also need a Telegram bot token.

### Setup Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/Sangeeth722/JobRadar-.git
  
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your **Telegram Bot Token**:
   ```ini
   BOT_TOKEN=your_telegram_bot_token
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

---

## How It Works
1. The script scrapes job listings from the specified website.
2. It filters job postings based on **predefined keywords**.
3. If a matching job is found, the bot sends a notification to your Telegram chat.
4. The bot continues checking for new jobs at regular intervals.

---

## Configuration
- Modify the `KEYWORDS` list in `main.py` to track job postings based on your interests.
- The bot fetches chat IDs automatically when you send a message to it.
- Adjust the `time.sleep(2)` value in the script to control the scraping frequency.

---

## Contributing
Feel free to fork this repository, add features, or fix bugs. Pull requests are welcome!

---

## License
This project is licensed under the **MIT License**.
