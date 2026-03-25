# 📚 Books Scraper (Python)

## 📝 Overview
This project is a web scraping tool that extracts book data from **Books to Scrape**, a practice website for scraping.

It collects data from both listing pages and detail pages, and saves the results in CSV and JSON formats.

---

## 🚀 Features

- Scrape book data from multiple pages (pagination support)
- Extract detailed information from each product page
- Remove duplicate records
- Save data in CSV and JSON formats
- Separate successful and failed data
- Log failed URLs for retry or debugging

---

## 📊 Extracted Data

Each book contains the following fields:

- `title` – Book title  
- `detail_url` – URL of the detail page  
- `price` – Price of the book  
- `stock` – Availability status  
- `rating` – Rating (One to Five)  
- `upc` – Unique product code  
- `description` – Book description  
- `category` – Book category  
- `fetched_at` – Timestamp of scraping  
- `source_url` – Source listing page URL  

---

## 🧱 Project Structure

