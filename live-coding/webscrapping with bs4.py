from bs4 import BeautifulSoup
import requests
from datetime import date, timedelta

def url_parser(date):
    return f"https://si3.bcentral.cl/Bdemovil/BDE/IndicadoresDiarios?parentMenuName=Indicadores%20diarios&fecha={date}"

class CurrencyService():
    """
    Currency service can retrive UF and US values from a date range
    """
    def values(self, from_date, to_date):
        date_currency = {}
        previous_uf = 0
        previous_us = 0
        delta = timedelta(days=1)

        while from_date <= to_date:
            pageContent = requests.get(url_parser(f"{str(from_date.day).zfill(2)}-{str(from_date.month).zfill(2)}-{from_date.year}"), allow_redirects=False)
            pageContent.encoding = 'utf-8'
            soup = BeautifulSoup(pageContent.text, "html.parser")
            data = soup.find_all('td', {'class': 'col-xs-2 text-center'})
            td_tag_uf = data[0].find('p').text
            td_tag_us = data[1].find('p').text

            date_currency[f"{str(from_date.day).zfill(2)}-{str(from_date.month).zfill(2)}-{from_date.year}"] = {'us': {'today': float(td_tag_us.replace(',','')), 'diff': float(td_tag_us.replace(',','')) - previous_us},
                                        'uf': {'today': float(td_tag_uf.replace(',','')), 'diff': float(td_tag_uf.replace(',','')) - previous_uf}}
            previous_us = float(td_tag_us.replace(',',''))
            previous_uf = float(td_tag_uf.replace(',',''))
            from_date += delta
            
        return date_currency

if __name__ == "__main__":
    currencyObj = CurrencyService()
    currencyObj.values(date(2022, 1, 1), date(2022, 2, 14))