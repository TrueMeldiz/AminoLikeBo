from colorama import init, Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.YELLOW)
print(Style.NORMAL)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi
▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄ █░░ ▀ █░▄▀ █▀▀ █▀▄ ▄▀▄
█▀█ █░█░█ █ █░▀█ █░█ █░▄ █ █▀▄░ █▀▀ █▀█ █░█
▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░ ▀▀▀ ▀ ▀░▀▀ ▀▀▀ ▀▀░ ░▀░""")
import amino
email=input("Email/Почта:")
password=input("Password/Пароль:")
client = amino.Client()
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Выберите сообщество/Select the community: "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)

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
