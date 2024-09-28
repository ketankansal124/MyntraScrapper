# 🛍️ Myntra Review Scrapper

### **Overview**
The **Myntra Review Scrapper** project focuses on automating the extraction of product reviews from the Myntra website. This scrapper allows users to collect detailed reviews, which can be used for sentiment analysis, product feedback aggregation, or market research. By scraping reviews in real-time, this project helps users understand customer sentiments and product performance over time.

The scrapped reviews are stored in a **MongoDB** database for efficient querying and long-term storage, and a simple **Streamlit** interface is provided for user interaction.

### **Dataset**
- Reviews are scrapped directly from **Myntra** product pages.
- Data collected includes:
  - **Product name**
  - **User reviews**
  - **Ratings**
  - **Date of review**
  
All scrapped data is stored in **MongoDB** for further analysis.

## 💿 Installation & Setup

### **1. Environment Setup**
To get started with this project, you need to set up a 1. 1. Python virtual environment:
```
conda create --prefix venv python==3.10 -y
```
```
conda activate venv/
```

2. Install Requirements and setup
```
pip install -r requirements.txt
```

3. MongoDB Setup
Make sure you have a running instance of MongoDB, and update the connection string in the project as per your MongoDB credentials.

4. Run the Scrapper Application
```
python app.py
```

## 🔧 Technologies Used

- **Python 3.10**: Core programming language for the scrapping logic and data management.
- **Streamlit**: Used to build a user-friendly interface for scrapping and viewing results.
- **MongoDB**: A NoSQL database used to store the scrapped reviews for easy querying and data persistence.
- **BeautifulSoup**: A Python library for parsing HTML and extracting data from web pages.
- **Requests**: A Python library for sending HTTP requests to Myntra’s website and fetching the HTML content.
- **Pandas**: For handling the scrapped data and preparing it for storage in MongoDB.

## 🛠️ Features

- **Real-time Review Scraping**: Fetches the latest reviews of products from Myntra.
- **Sentiment Analysis Ready**: Scrapped reviews can be easily processed for sentiment analysis and other NLP tasks.
- **Scalable Storage**: Stores the collected data in MongoDB, allowing for scalable storage and retrieval.
- **User Interface**: An easy-to-use interface built with Streamlit for product selection and data scrapping.

## 🚀 How It Works

1. **Input Product URL**: Users input the Myntra product URL they want to scrape reviews from.
2. **Scraping**: The scrapper fetches the reviews, ratings, and metadata for the product.
3. **Data Storage**: The scrapped data is stored in MongoDB for easy access and analysis.
4. **Streamlit Interface**: A front-end interface is provided to view the scrapped reviews and perform further actions such as exporting the data.

## 💡 Potential Use Cases

- **Sentiment Analysis**: Use the scrapped reviews to perform sentiment analysis and gauge customer satisfaction.
- **Product Review Aggregation**: Aggregate reviews to understand the strengths and weaknesses of different products.
- **Market Research**: Gain insights into customer preferences and product performance over time.

## 📈 Results & Performance

- Scraps reviews efficiently with detailed information such as review text, rating, and date of review.
- Supports batch processing of multiple product URLs.
- Data stored in MongoDB can be used for large-scale analytics and reporting.

## 🏗️ Future Enhancements

- **Automated Sentiment Analysis**: Integrate a sentiment analysis model to classify reviews into positive, neutral, and negative categories.
- **Enhanced Scrapping Capabilities**: Add features to scrape additional product information such as pricing and availability.
- **Review Visualization**: Build visual dashboards to summarize review trends and product feedback over time.

## 📚 References

- Myntra: [https://www.myntra.com/](https://www.myntra.com/)
- MongoDB Documentation: [https://www.mongodb.com/docs/](https://www.mongodb.com/docs/)
