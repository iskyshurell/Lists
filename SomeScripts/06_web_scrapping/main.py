import requests
import re

if __name__ == '__main__':
	file = requests.get("http://www.columbia.edu/~fdc/sample.html")

	text = re.findall(r"<h3.*h3>", file.text)
	text = [re.sub(r"[<, >]", r" ", re.search(r'>.*<', i_str).group()) for i_str in text]
	print(text)
