import requests
import re


def get_header(web):
    answer = requests.get(web)
    answer.raise_for_status()

    header = re.findall(r'<h3.*?>(.*?)<\/h3>', answer.text, re.DOTALL)
    header = [re.sub(r'<.*?>', '', heading).strip() for heading in header]

    return header


print(get_header("http://www.columbia.edu/~fdc/sample.html"))