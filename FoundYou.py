import os, sys
import googlesearch
import yahoo_search
from duckduckgo_search import DDGS
from bing_results_scraper import BingScraper

def googleSearch(searchquery : str, amount : int):
	try:
		linksfound = 0
		gsearch = googlesearch.search(f'intext:"{searchquery}"', num=int(amount), start=0, stop=None, pause=2)
		formatted = []
		for link in gsearch:
			formatted.append(link)
			linksfound += 1
			if linksfound > int(amount):
				break
		return formatted
	except Exception as e:
		return []
		pass

def duckduckgoSearch(searchquery : str, amount : int):
	try:
		#ddgs = DDGS(proxy="PROXY", timeout=20)
		ddgs = DDGS()
		unformatted = ddgs.text(f'intext:"{searchquery}"', max_results=int(amount))
		formatted = []
		for entry in unformatted:
			formatted.append(entry["href"])
		return formatted
	except Exception as e:
		return []
		pass

def py_bing_s(searchquery : str, amount : int):
	try:
		formatted = []
		linksfound = 0
		bing = BingScraper()
		results = bing.get_results(q=f'intext:"{searchquery}"')
		list2 = results['organic_results']
		for entry in list2:
		    formatted.append(entry["link"])
		    linksfound += 1
		    if linksfound > int(amount):
		    	break
		return formatted
	except Exception as e:
		return[]
		pass

def yahoo_search_function(searchquery : str, amount : int):
	try:
		linksfound = 0
		ysearch = yahoo_search.search(f'intext:"{searchquery}"')
		formatted = []
		for link in ysearch.pages:
			formatted.append(link.link)
			linksfound += 1
			if linksfound > int(amount):
				break
		return formatted
	except Exception as e:
		return[]
		pass

def remove_dupes(dupelist):
	return list(dict.fromkeys(dupelist))

os.system("title Found You! - OSINT Tool - Developed By Eric")
os.system("mode con: cols=160 lines=35")

print("""             ______              
          .-'      `-.           
        .'            `.         
       /                \\        
      ;                 ;`       
      |       \x1b[38;2;255;0;187mYOU\x1b[0m       |;       
      ;                 ;|
      '\\               / ;       
       \\`.           .' /        
        `.`-._____.-' .'         
          / /`_____.-'           
         / / /    ________                                    __        __      __                    __                                
        / / /    |        \\                                  |  \\      |  \\    /  \\                  |  \\          
       / / /     | \x1b[38;2;255;0;187m$$$$$$$$\x1b[0m______   __    __  _______    ____| \x1b[38;2;255;0;187m$$       \x1b[0m\\\x1b[38;2;255;0;187m$$\x1b[0m\\  /  \x1b[38;2;255;0;187m$$\x1b[0m______   __    __ | \x1b[38;2;255;0;187m$$\x1b[0m     
      / / /      | \x1b[38;2;255;0;187m$$\x1b[0m__   /      \\ |  \\  |  \\|       \\  /      \x1b[38;2;255;0;187m$$\x1b[0m        \\\x1b[38;2;255;0;187m$$\x1b[0m\\/  \x1b[38;2;255;0;187m$$\x1b[0m/      \\ |  \\  |  \\| \x1b[38;2;255;0;187m$$\x1b[0m    
     / / /       | \x1b[38;2;255;0;187m$$\x1b[0m  \\ |  \x1b[38;2;255;0;187m$$$$$$\x1b[0m\\| \x1b[38;2;255;0;187m$$\x1b[0m  | \x1b[38;2;255;0;187m$$\x1b[0m| \x1b[38;2;255;0;187m$$$$$$$\x1b[0m\\|  \x1b[38;2;255;0;187m$$$$$$$\x1b[0m         \\\x1b[38;2;255;0;187m$$  $$\x1b[0m|  \x1b[38;2;255;0;187m$$$$$$\x1b[0m\\| \x1b[38;2;255;0;187m$$  \x1b[0m| \x1b[38;2;255;0;187m$$\x1b[0m| \x1b[38;2;255;0;187m$$\x1b[0m   
    / / /        | \x1b[38;2;255;0;187m$$$$$ \x1b[0m| \x1b[38;2;255;0;187m$$  \x1b[0m| \x1b[38;2;255;0;187m$$\x1b[0m| \x1b[38;2;255;0;187m$$  \x1b[0m| \x1b[38;2;255;0;187m$$\x1b[0m| \x1b[38;2;255;0;187m$$  \x1b[0m| \x1b[38;2;255;0;187m$$\x1b[0m| \x1b[38;2;255;0;187m$$  \x1b[0m| \x1b[38;2;255;0;187m$$\x1b[0m          \\\x1b[38;2;255;0;187m$$$$ \x1b[0m| \x1b[38;2;255;0;187m$$  \x1b[0m| \x1b[38;2;255;0;187m$$\x1b[0m| \x1b[38;2;255;0;187m$$  \x1b[0m| \x1b[38;2;255;0;187m$$\x1b[0m \\\x1b[38;2;255;0;187m$$\x1b[0m  
   / / /         | \x1b[38;2;255;0;187m$$    \x1b[0m| \x1b[38;2;255;0;187m$$\x1b[0m__/ \x1b[38;2;255;0;187m$$\x1b[0m| \x1b[38;2;255;0;187m$$\x1b[0m__/ \x1b[38;2;255;0;187m$$\x1b[0m| \x1b[38;2;255;0;187m$$  \x1b[0m| \x1b[38;2;255;0;187m$$\x1b[0m| \x1b[38;2;255;0;187m$$\x1b[0m__| \x1b[38;2;255;0;187m$$\x1b[0m          | \x1b[38;2;255;0;187m$$\x1b[0m  | \x1b[38;2;255;0;187m$$\x1b[0m__/ \x1b[38;2;255;0;187m$$\x1b[0m| \x1b[38;2;255;0;187m$$\x1b[0m__/ \x1b[38;2;255;0;187m$$\x1b[0m __  
  / / /          | \x1b[38;2;255;0;187m$$     \x1b[0m\\\x1b[38;2;255;0;187m$$    $$ \x1b[0m\\\x1b[38;2;255;0;187m$$    $$\x1b[0m| \x1b[38;2;255;0;187m$$  \x1b[0m| \x1b[38;2;255;0;187m$$ \x1b[0m\\\x1b[38;2;255;0;187m$$    $$          \x1b[0m| \x1b[38;2;255;0;187m$$   \x1b[0m\\\x1b[38;2;255;0;187m$$    $$ \x1b[0m\\\x1b[38;2;255;0;187m$$    $$\x1b[0m|  \\
 / / /            \\\x1b[38;2;255;0;187m$$      \x1b[0m\\\x1b[38;2;255;0;187m$$$$$$   \x1b[0m\\\x1b[38;2;255;0;187m$$$$$$  \x1b[0m\\\x1b[38;2;255;0;187m$$   \x1b[0m\\\x1b[38;2;255;0;187m$$  \x1b[0m\\\x1b[38;2;255;0;187m$$$$$$$\x1b[0m           \\\x1b[38;2;255;0;187m$$    \x1b[0m\\\x1b[38;2;255;0;187m$$$$$$   \x1b[0m\\\x1b[38;2;255;0;187m$$$$$$  \x1b[0m\\\x1b[38;2;255;0;187m$$\x1b[0m
 \\/_/
	                                       Created By Eric\n\n""")

username = str(input("\x1b[0mEnter The Username \x1b[38;2;255;0;187m-->\x1b[0m "))
amount = int(input("\x1b[0mEnter The Desired Amount Of Results Per Engine\x1b[38;2;255;0;187m-->\x1b[0m "))

unformattedresults = []
for result in googleSearch(username, amount):
	unformattedresults.append(result)
for result in duckduckgoSearch(username, amount):
	unformattedresults.append(result)
for result in py_bing_s(username, amount):
	unformattedresults.append(result)
for result in yahoo_search_function(username, amount):
	unformattedresults.append(result)
results = remove_dupes(unformattedresults)

counter = 0
for link in results:
	counter += 1
	print(f"\x1b[0mFound You! \x1b[38;2;255;0;187m| \x1b[0m{counter} \x1b[38;2;255;0;187m| \x1b[0m{link}\x1b[0m")


print(f"\n\n- \x1b[38;2;255;0;187m{counter}\x1b[0m results found for the query: \x1b[38;2;255;0;187m{username}\x1b[0m -")
os.system("pause")
sys.exit()