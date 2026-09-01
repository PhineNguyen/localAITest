from selenium import webdriver #mở browser
from selenium.webdriver.common.by import By #chỉ định tìm phần tử
from selenium.webdriver.common.keys import Keys #tương tác với bàn worphím trong browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException #2 loại lỗi cụ thể selenium có thể ném ra khi tìm phần tử hoặc chờ phần tử quá lâu
from urllib.parse import quote_plus


class BrowserController:
    tools = [{
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search Google and return top search result title ",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to look up on Google"
                    }
            },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
            "function": {
                "name": "browser_open_url",
                "description": "Open a specific URL or web page in Chrome browser",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "The URL to open in Chrome"
                        }
                    },
                    "required": ["url"]
                }
            }
        }
    ]
    def __init__(self):
        self.driver = None

    def _ensure_driver(self):
        """Chỉ mở Chrome nếu chưa có driver đang chạy"""
        if self.driver is None:
            self.driver = webdriver.Chrome()

    def search(self, query: str) -> str:
        self._ensure_driver()
        try:
            self.driver.get("https://www.google.com")
            search_box = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_box.send_keys(query) #nhập từ khóa tìm kiếm vào ô tìm kiếm
            search_box.send_keys(Keys.RETURN) #nhấn Enter để tìm kiếm

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
            )

            results = self.driver.find_elements(By.CSS_SELECTOR, "h3")
            top_titles = [r.text for r in results[:3] if r.text]
            return f"Top results for '{query}': " + "; ".join(top_titles)

        except TimeoutException:
            return f"Searched for '{query}', but couldn't read results in time."
        except Exception as error:
            return f"Search failed: {error}"

    def open_url(self, url: str) -> str:
        self._ensure_driver()
        if not url.startswith(("http://", "https://")):
            url = f"https://{url}"
        try:
            self.driver.get(url)
            return f"Opened {url}"
        except Exception as error:
            return f"Couldn't open {url}: {error}"

    def close(self):
        if self.driver:
            self.driver.quit()
            self.driver = None