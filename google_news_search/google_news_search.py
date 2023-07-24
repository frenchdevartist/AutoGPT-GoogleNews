"""google_news search command for Autogpt."""
from __future__ import annotations

import xml.etree.ElementTree as et
import json
import re
from urllib.parse import quote
import base64
import requests

HTML_TAG_CLEANER = re.compile("<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});")


def _google_news_search(query: str, num_results: int = 5) -> str | list[str]:
    """Return the results of a google_news search
    Args:
        query (str): The search query.
        num_results (int): The number of results to return.
    Returns:
        str: The results of the search. The resulting string is a `json.dumps`
             of a list of len `num_results` containing dictionaries with the
             following structure: `{'title': <title>, 'summary': <summary>,
             'url': <url to relevant page>}`
    """
    search_url = (
        f"https://news.google.com/rss/search?q={quote(query)}&hl=en-US&gl=US&ceid=US%3Aen"
    )
    with requests.Session() as session:

        results = session.get(search_url)

        items = []
        try:
            doc = et.fromstring(results.text)

            for item in doc.iter('item'):
                summary = re.sub(HTML_TAG_CLEANER, "", item.find("description").text)

                google_url = item.find("link").text
                base64_url = google_url.replace("https://news.google.com/rss/articles/","").split("?")[0]
                final_url = base64.urlsafe_b64decode(base64_url + "===")[4:-3].decode('utf-8',errors='ignore')
                if final_url.find('\u0001')>=0:
                    final_url = final_url.split('\u0001')[0]
                if final_url!="":
                    items.append(
                        {
                            "title": item.find("title").text,
                            "summary": summary,
                            "url": final_url,
                        }
                    )
                if len(items) == num_results:
                    break
        except Exception as e:
            return f"'google_news_search' on query: '{query}' raised exception: '{e}'"

    return json.dumps(items, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    res=_google_news_search("Large Language Model")
    print(res)

