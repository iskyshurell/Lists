import json
import requests
from typing import Dict


def request(url: str) -> Dict:
	my_res = requests.get(url)
	text = json.loads(my_res.text)
	return text


def s_value(dictionary: Dict, searching: str) -> str:
	return f"{searching}:{dictionary.get(searching, 'Key-Error')}"


def main_sort(episodes, death):
	result = {f'{i_episode["season"]}:{i_episode["episode"]}'.replace(' ', ''): i_episode["episode_id"] for i_episode in
	          episodes if i_episode["series"] == "Breaking Bad"}

	info = {}  # Информация хранитсья в таком виде {"сезон:епизод":{"id":int_num, "death":[death_list], "all_death":int_num}}
	for i_episode in death:
		key = f'{i_episode["season"]}:{i_episode["episode"]}'
		if key not in info:
			info[key] = {}

			info[key]['id'] = result[key]
			info[key]["death"] = []
			info[key]['all_death'] = 0

		info[key]['death'].append(i_episode["death"])
		info[key]['all_death'] += i_episode["number_of_deaths"]
	return info, result

def the_biggest_kill_count(info):
	return sorted([(i_value, info[i_value]["all_death"]) for i_value in info], key = lambda x: int(x[-1]))[-1][0] #Нахождение серии с наибольшим количеством убийств

if __name__ == '__main__':


	result = request("https://www.breakingbadapi.com/api/")
	death = request(result['deaths'])
	episodes = request(result['episodes'])


	info, result = main_sort(episodes, death)


	temp = the_biggest_kill_count(info)


	temp_l = temp.split(':')
	season = temp_l[0]
	episode = temp_l[-1]


	info = {'season':season,"episode":episode, "info":info[temp]}
	print(info)
	with open("result.json", 'w') as file:
		json.dump(info, file, indent = 4)





