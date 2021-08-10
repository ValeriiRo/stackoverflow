import requests
import time

def time_in_seconds(named_tuple):
    time_string = time.strftime("%d/%m/%Y %H:%M", named_tuple)
    struct_time = time.strptime(time_string, '%d/%m/%Y %H:%M')
    local_time = time.mktime(struct_time)
    return local_time

def restored_date(seconds):
    local_time = time.ctime(seconds)
    print(f"Время создания вопроса: {local_time}")

named_tuple = time.localtime()
max_time = int(time_in_seconds(named_tuple))
min_time = max_time - 86400 * 2
max_time = str(max_time)
min_time = str(min_time)

params = {
            'order': 'desc',
            'fromdate': min_time,
            'min': min_time,
            'todate': max_time,
            'max': max_time,
            'sort': 'activity',
            'tagged': 'python',
            'site': 'stackoverflow'
      }
API_BASE_URL = 'https://api.stackexchange.com///2.3/'
methods_URL = API_BASE_URL + 'questions'
files_list = requests.get(methods_URL, params=params).json()
print("все вопросы за последние два дня и содержит тэг 'Python':\n")
for question in files_list['items']:
    seconds = question["creation_date"]
    seconds = restored_date(seconds)
    print(f"Автор вопроса: {question['owner']['display_name']}\nТэги Вопроса:{question['tags']}\nВопрос: {question['title']}\nСсылка на вопрос: {question['link']}\n")
