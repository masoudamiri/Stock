# 📈 Django Stock Chart Viewer

This project is a Django-based web application that visualizes stock price and trading volume data from a CSV file. It features an interactive **candlestick chart** with a **bar chart** showing the **traded share percentage** underneath. The charts are rendered using Plotly and allow zooming and filtering via a range slider.

---

## 🚀 Features

- 📊 **Candlestick Chart** for daily open, high, low, and close prices.
- 📉 **Volume Bar Chart** using `TradedShare` (percent-based) scaled to price range for visual clarity.
- 🎚️ **Interactive Range Slider** for exploring specific time ranges.
- 🧾 **CSV-based Input** makes it easy to replace or update stock data.
- 🖥️ Full-screen responsive layout with Plotly interactivity.

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally:

1. **Create and activate a virtual environment:**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

2. **Install dependencies:**

```bash
pip install django pandas plotly
```

3. **Run the Django development server:**

```bash
python manage.py runserver
```

4. **Open the application in your browser:**

```
http://127.0.0.1:8000/
```

---

## 🗂️ Project Structure

```
stock_chart_project/
├── ABAD.csv                  # Stock data (CSV format)
├── manage.py                 # Django project entry point
├── README.md                 # This documentation file
├── stock_chart_project/
│   ├── __init__.py
│   ├── settings.py           # Django configuration
│   ├── urls.py               # Root URL config
│   └── wsgi.py
├── charts/
│   ├── __init__.py
│   ├── views.py              # Chart rendering logic using Plotly
│   ├── urls.py               # App-specific routes
│   ├── templates/
│   │   └── charts/
│   │       └── index.html    # HTML template for chart display
```

---

## 🧾 CSV File Format

Your `ABAD.csv` file must include at least the following columns:

| Column Name     | Description                             |
|------------------|-----------------------------------------|
| `<DTYYYYMMDD>`   | Date in YYYYMMDD format                |
| `<OPEN>`         | Opening price                          |
| `<HIGH>`         | Highest price                          |
| `<LOW>`          | Lowest price                           |
| `<CLOSE>`        | Closing price                          |
| `TradedShare`    | Percentage of shares traded (0–100%)   |

**Example rows:**

```
<DTYYYYMMDD>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,TradedShare
20210101,100,110,95,105,3.5
20210102,106,112,104,110,4.1
```

---

## 🧩 Customization Notes

- You can extend this project to read from a database (PostgreSQL, SQLite, etc.).
- Additional chart types (OHLC, line, scatter, etc.) can be added with Plotly.
- Supports Persian and international market data if format is consistent.

---

## 📃 License

This project is open for educational and internal use. You can modify and use it freely in your own projects.
