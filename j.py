from arsein import Messenger
from time import sleep
from re import findall

bot = Messenger("")

text : str = '''تو با چه حقی انقدر خوشگلی؟عزقم من ممبر دزدم از فمای عضو گیری دزدیدمت میخوام ببرت فمم میشه ایگنور نکنی و بیای زیبا.؟
https://rubika.ir/joing/DHCAFFFA0LAGAGCQIBAACBVGNCPWETFB'''

answered,guid_gap = [],[]

link_group = ["https://rubika.ir/joing/CHEACCDA0TDRNBWVFYDOLEGESDAUAJWF","https://rubika.ir/joing/DHCDAHDB0QNKWIPMXQFRLPNLIRPHPDTQ","https://rubika.ir/joing/DGBIBGAC0DSAHKVQZXOVRPERNVLMYIUQ","https://rubika.ir/joing/CAFIIIFB0CVBUEOSMYSUSGRIYXAFKIRZ","https://rubika.ir/joing/DGEGDBGA0LAPLCVRUVBLMWSZNQCYVVNN","https://rubika.ir/joing/CBCBFGCF0XHBUJZHNRPCDIHZPVGDWFMB","https://rubika.ir/joing/CCBFFBAF0PPEFSBEJBEWQRNNFWIWOBNV","https://rubika.ir/joing/CJJFJFAE0GIEJRDVTIYALVZCVJEQOAII","https://rubika.ir/joing/DGCFDCGE0GHYGCJXWQWXWGKDDONOJJEP","http://rubika.ir/joIng/DHHIFEGE0YKAMMIMIYZIBLHDWVZBMPQQ","https://rubika.ir/joing/DHJDEHGA0BOWVPBNKBWQABSRJSETEPQL","https://rubika.ir/joing/DDFFBIIA0EJFEUAPQYVSXEENAMWPQXFQ","https://rubika.ir/joing/DGGCDJIB0OWTEIZGULIZMDNAUALSLVHK","https://rubika.ir/joing/DEHCIDCI0YTEBNTWWCRECIILFFYZIXSQ‌","https://rubika.ir/joing/DGHHGDGD0MRKZZLZPBDZWHXPNRWBOSCK","https://rubika.ir/joing/DHJFDBDC0HYRRDQTXEFPLHAPGJCDKHNE"]

for gap in link_group:
	try:
		group_information = bot.joinGroup(gap)
		group_guid = group_information.get('data').get('group').get('group_guid')
		group_name = group_information.get('data').get('group').get('group_title')
		print("name gap : "+group_name+"\n")
		guid_gap.append(group_guid)
	except : pass
	
print(guid_gap)

guid_send_ok = [guid.replace("\n","") for guid in open("guids.txt","r").readlines()]

listSave = ''

user_guids = []

for group_guid in guid_gap:
		try:
			for messages in bot.getChatGroup(group_guid):
					for user_guid in findall('u0\w{30}', messages.get('author_object_guid')):
						user_guids.append(user_guid)
						listSave += user_guid +'\n'
		except:pass

for user in user_guids:
	try:
			if user not in guid_send_ok:
				sleep(5)
				send_message = bot.sendMessage(user,text)
				name_user = bot.getUserInfo(user).get('data').get('user').get('first_name')
				print("send user : "+name_user)
				bot.deleteUserChat(user,'0')
	except:pass
	
with open(f'guids.txt','a') as file:
                file.write(listSave)
                print('          Save Guid     ' )  	