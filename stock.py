import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
def main(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')


    table = soup.find('table')


    df = pd.read_html(str(table))[0]

    output_file = "t.xlsx"
    df.to_excel(output_file, index=False)

    print(f"Table data saved to {output_file}.")



    return 0

def chart():
    data = pd.read_excel('t.xlsx')
    columns_of_interest = ['Last Closing Price', 'Change', '% Change']
    columns_of_interest = columns_of_interest[:5]

    companies = data['Company'][:5]
    last_closing_prices = data['Last Closing Price'][:5]

    fig, ax = plt.subplots()

    for i, column in enumerate(columns_of_interest):
        values = data[column][:5]
        x = [i + 1 for i in range(len(values))]
        ax.scatter(companies, values, label=column)
    plt.xlabel('Company')
    plt.ylabel('Last Closing Price')
    plt.title('Stock Data')
    for i, company in enumerate(companies):
        ax.text(i + 1, last_closing_prices[i], company, ha='center', va='bottom')
    plt.legend()

    plt.show()






main("https://www.stockexchangeofmauritius.com/products-market-data/equities-board/trading-quotes/official")
chart()

