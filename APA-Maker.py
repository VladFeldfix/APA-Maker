# Download SmartConsole.py from: https://github.com/VladFeldfix/Smart-Console/blob/main/SmartConsole.py
from SmartConsole import *

class main:
    # constructor
    def __init__(self):
        # load smart console
        self.sc = SmartConsole("APA Maker", "1.0")

        # set-up main memu
        self.sc.add_main_menu_item("RUN", self.run)

        # start
        self.sc.start()
    
    def run(self):
        fname = self.sc.input("Author first name")
        lname = self.sc.input("Author last name")
        date = self.sc.input("Publishing date")
        title = self.sc.input("Article title")
        webname = self.sc.input("Website name")
        url = self.sc.input("URL")
        try:
            publishername = lname+" "+fname[0]
            if fname == lname or lname == "":
                publishername = fname
            if date == "":
                date = "n.d."
            if webname.upper() == "YOUTUBE" or webname.upper() == "YT":
                title = title+" [Video]"
            self.sc.print("\nReferences:")
            self.sc.print("%s. (%s). %s. %s. Retrieved from: %s" % (publishername, date, title, webname, url))
            self.sc.print("\nIn text citations:")
            self.sc.print("(%s. %s)" % (publishername, date))
        except:
            pass
        # restart
        if self.sc.question("\nMake another?"):
            self.sc.hr()
            self.run()
        else:
            self.sc.exit()

main()