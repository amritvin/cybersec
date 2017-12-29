import webbrowser

url = 'http://docs.python.org/'

# MacOS
chrome_path = 'open  /Applications/Google\ Chrome.app %s'

# Windows
# chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

webbrowser.open(url)
