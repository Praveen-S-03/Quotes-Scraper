
# Quotes Scraper 📝

This project scrapes famous quotes and their authors from [Quotes to Scrape](https://quotes.toscrape.com/) using **Python**, **Requests**, and **BeautifulSoup**, then saves the results into a JSON file.

---

## 📌 Features
- Scrapes **quotes** and **authors** from the first 10 pages of the website
- Cleans and formats the data
- Saves results to `Quotes.json` with proper indentation
- Lightweight and beginner-friendly

---

## ⚙️ Requirements
Make sure you have Python 3 installed, then install dependencies:

```bash
pip install requests beautifulsoup4 lxml
🚀 Usage

```

## Clone the repository:
```bash
git clone https://github.com/your-username/quotes-scraper.git
cd quotes-scraper
```
## Run the script:
python scraper.py
After running, you’ll find a file called Quotes.json in the same directory.

## 📂 Output Example
json
```
[
    {
        "Quote": "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.",
        "Author": "Albert Einstein"
    },
    {
        "Quote": "It is our choices, Harry, that show what we truly are, far more than our abilities.",
        "Author": "J.K. Rowling"
    }
]
```
## 📌 Future Improvements
Add tags for each quote

Support saving to CSV or database

Build a simple UI to view/search quotes

## 📜 License
This project is licensed under the MIT License – feel free to use and modify it.

yaml
Copy code
