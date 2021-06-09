import amino
import pyfiglet
import concurrent.futures
from colorama import init, Fore, Back, Style
init()
print(Fore.YELLOW + Style.NORMAL)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminolikebo", font="big"))
email = input("Email/Почта: ")
password = input("Password/Пароль: ")
client = amino.Client()
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Выберите сообщество/Select the community: "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)

numberofblogs = int(input("Type the number of blogs/Введите количество блогов: "))

while True:
	try:
		with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
			for i in range(0, 2000, 250):
				blogs = sub_client.get_recent_blogs(start=i, size=numberofblogs).blogId
				for id in blogs:
					_ = [executor.submit(sub_client.like_blog, id)]
					print(f"{id} Liked")
	except:
		pass
