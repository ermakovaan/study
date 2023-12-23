import requests
import re


class WebParser:
    """
    Класс для получения информации с веб-ресурсов.
    """
    @staticmethod
    def get_header(url: str) -> list[str]:
        """
        Получение списка подзаголовков из тегов <h3> на указанной веб-странице.

        Args:
        - url: URL веб-страницы.

        Returns:
        - List[str]: Список подзаголовков.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return []

        header_tags = re.findall(r'<h3.*?>(.*?)<\/h3>', response.text, re.DOTALL)
        headers = [re.sub(r'<.*?>', '', heading).strip() for heading in header_tags]

        return headers


if __name__ == "__main__":
    try:
        wp = WebParser()
        headers_list = wp.get_header(url='http://www.columbia.edu/~fdc/sample.html')
        print(headers_list)
    except (requests.RequestException, Exception) as e:
        print(e)
