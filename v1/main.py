print("welcom to APA citation maker! v.1.1")
def go():
	print()
	fname = input("Author first name: ")
	lname = input("Author last name: ")
	date = input("Publishing date: ")
	title = input("Article title: ")
	webname = input("Website name: ")
	url = input("URL: ")
	try:
		publishername = lname+" "+fname[0]
		if fname == lname or lname == "":
			publishername = fname
		if date == "":
			date = "n.d."
		if webname == "YouTube":
			title = title+" [Video]"
		print("%s. (%s). %s. %s. Retrieved from: %s" % (publishername, date, title, webname, url))
		print("(%s. %s)" % (publishername, date))
	except:
		pass
	input("Press Enter for another citation >")
	go()
go()
