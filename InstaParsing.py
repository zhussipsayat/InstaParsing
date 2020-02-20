import requests
from time import sleep
text = input('Здравствуйте, введите имя искомого аккаунта:')
sleep(2)
print('Вы ищете: '+text)
response = requests.get('https://www.instagram.com/'+text+'?__a=1')
a = response.json()
print('Имя: '+a['graphql']['user']['full_name'])
print('Инфа в био: '+a['graphql']['user']['full_name'])
print('Количество постов: '+str(a['graphql']['user']['edge_owner_to_timeline_media']['count']))
print('Количество подписчиков: '+str(a['graphql']['user']['edge_followed_by']['count']))

posts = a['graphql']['user']['edge_owner_to_timeline_media']['edges']
posts_text = ''

for i in posts:
	url = i['node']['shortcode']
	like = i['node']['edge_liked_by']['count']
	cmnt = i['node']['edge_media_to_comment']['count']
	sleep(2)
	print(str(url)+' Лайков '+str(like)+','+'Комментов '+str(cmnt)+';')


