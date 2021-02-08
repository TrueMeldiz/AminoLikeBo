from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.YELLOW)
print(Style.BRIGHT)
print("Script by Zevi/Скрипт сделан Zevi")
print("┌────────────────────────────────────┐")
print("│Author :  LilZevi                   │")
print("│Github : https://github.com/LilZevi │")
print("└────────────────────────────────────┘")
print("YouTube: https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ")
print("▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄ █░░ ▀ █░▄▀ █▀▀ █▀▄ ▄▀▄")
print("█▀█ █░█░█ █ █░▀█ █░█ █░▄ █ █▀▄░ █▀▀ █▀█ █░█")
print("▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░ ▀▀▀ ▀ ▀░▀▀ ▀▀▀ ▀▀░ ░▀░")
import amino
email=input("Email/Почта:")
password=input("Password/Пароль:")
client = amino.Client()
client.login(email=email, password=password)
for name, id in zip(client.sub_clients().name, client.sub_clients().comId):
	print(f"{name}: {id}")
comid = input("Выберите сообщество(id): ")
sub_client=amino.SubClient(comId=comid,profile=client.profile)
valueofblogs=int(input("Type the number of blogs/Введите количество блогов:"))
num=0
while valueofblogs > num and len:
	lb=sub_client.get_recent_blogs(start=num, size=valueofblogs).blogId
	b=0
	for id in lb:
		try:
			sub_client.like_blog(blogId=id)
			print("liked the blog/поставили лайк на блог =",id)
			b=b+1
		except:
			f=True
			num=num+25
			pass