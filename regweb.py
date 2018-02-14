import requests, datetime

class regweb():
    def __init__(self, username, password, server, cardnum, seluser):
        self.punchUrl = server+"/action-punch-add-worktime.asp?cardnum=%s&pdate=%s&seluser=%s&ptime=%s&pdir=%s&pcom=0&sb-fix-save=Tallenna"
        self.frontUrl = server+"/login.asp"
        self.loginUrl = server+"/action-login.asp"
        self.username = username
        self.password = password
        self.url = ""

        self.cardnum = cardnum
        self.seluser = seluser
        self.pdate = ""
        self.ptime = ""

        self.direction = {
            'out': 0,
            'in': 128
        }

        self.session = requests.Session()
        self.cookies = {}

    def getCookie(self):
        self.url = self.frontUrl
        r = self.session.get(self.url)
        if r.status_code == 200:
            self.cookies = self.session.cookies.get_dict()
        else:
            print("Could not reach login page")
            exit(0)

    def login(self):
        self.url = self.loginUrl
        data = {'username': self.username, 'password': self.password}
        r = requests.post(self.url, data=data, cookies=self.cookies)
        if r.status_code == 200:
            pass
        else:
            print("Could not login")
            exit(0)

    def generatePunchUrl(self):
        self.url = self.punchUrl % (self.cardnum, self.pdate, self.seluser, self.ptime, self.pdir)
       
    def punch(self, direction, time=False):
        self.pdir = self.direction[direction]
        if time:
            self.ptime = time
        else:
            self.ptime = datetime.datetime.now().strftime("%H:%M")
            self.pdate = datetime.datetime.now().strftime("%-d.%m.%Y")
        self.generatePunchUrl()
        # print(self.url)
        r = requests.get(self.url, cookies=self.cookies)
        if r.status_code == 200:
            print("Punch ok! (maybe :-D)")


