# FoundYou
FoundYou is an OSINT tool I created that scrapes multiple search engines to find links with the query in text. It uses an intext:"" query to find the exact username across Google, DuckDuckGo, Bing, and Yahoo.
It's quite simple. It scrapes all 4 of the sources, removes any exact duplicates, and then displays them on the screen.
[![Found-You-Demo.png](https://i.postimg.cc/6367BW8S/Found-You-Demo.png)](https://postimg.cc/94SXpjtt)

Possible ways to be improved:
- Add proxy support to counteract rate limits
- Add additional search engines
- Support more dorking queries
- Implement GUI

USAGE:
```sh
pip install -r requirements.txt
python FoundYou.py
```
