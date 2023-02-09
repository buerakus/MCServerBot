import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from mcstatus import JavaServer


TOKEN = 'vk1.a.7Z4STnkQCQQ9lMlgvBHG5p5_smhdTDXFsm_mnHNt7gSyc17yxbzTH4Efg2tPXVa9j0LAOsLUKjJdGgOrzMQUCiELCyT-DCSv0LomUu' \
	'CPMs0D4hnEstuH-jBo31U47_eQpVgy5_mQJV8f8s9Mb_alm4dJcY24AfgSDS8XpnXQwQsUspHoubxzR6tQzlvMNP-kp2E80TfpTKEJFNF-2RAiFw'
GROUP_ID = '185178283'
def main():
	server = JavaServer.lookup("m3.joinserver.ru:25842")
	vk_session = vk_api.VkApi(token=TOKEN)
	session_API = vk_session.get_api()
	longpoll = VkBotLongPoll(vk_session, GROUP_ID)
	for event in longpoll.listen():
		# answers only
		if event.type == VkBotEventType.MESSAGE_NEW:
			ct =  event.message.text.lower()
			content = str(ct).lower().split(" ")
			user_id = event.message.from_id
			peer_id = event.message.peer_id
			seed = -4252866083268818716
			user_first_name = session_API.users.get(user_ids = (user_id))[0]['first_name']
			user_last_name = session_API.users.get(user_ids = (user_id))[0]['last_name']
			# server ping variable
			latency = server.ping()
			print(f'\n\n\npending: {user_first_name} {user_last_name}\ncontent: {ct}')
			if content[0][0] == '!':
				if content[0][1:] == 'инфо':
					session_API.messages.send(peer_id=peer_id, message=f'IP : m3.joinserver.ru:25842 \n95.216.62.170:25842 '
																	   f'\nCraftBukkit 1.16.5 \nсид - {seed}', random_id=0)
					# server available commands
				elif content[0][1:] == 'команды':
					session_API.messages.send(peer_id=peer_id, message='1. инфо', random_id=0)
					# server players exec
				elif content[0][1:] == 'игроки':
					query = server.query()
					session_API.messages.send(peer_id=peer_id, message=f"на сервере сейчас играет "
																		f"{', '.join(query.players.names)}", random_id=0)
					#server ping exec
				elif content[0][1:] == 'пинг':
					session_API.messages.send(peer_id=peer_id, message=f"пинг {latency}", random_id=0)


if __name__ == '__main__':

	main()
