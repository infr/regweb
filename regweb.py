import requests, datetime
from bs4 import BeautifulSoup

class regweb():
    def __init__(self, username, password, server, debug=False):
        self.punchUrl = server + "/action-punch-add-worktime.asp?cardnum=%s&pdate=%s&seluser=%s&ptime=%s&pdir=%s&pcom=0&sb-fix-save=Tallenna"
        self.debugPunchUrl = server + "/fixpunch.asp?curdate=%s&ptype=0"
        self.frontUrl = server+"/login.asp"
        self.loginUrl = server+"/action-login.asp"
        self.username = username
        self.password = password
        self.url = ""
        self.debug = debug

        self.cardnum = ""
        self.seluser = ""
        self.pdate = ""
        self.ptime = ""
        self.balance = ""
        self.daybalance = ""

        self.direction = {
            'out': 0,
            'in': 128
        }

        self.session = requests.Session()
        self.cookies = {}

    def getCookie(self):
        self.url = self.frontUrl
        try:
            self.session.get(self.url)
            self.cookies = self.session.cookies.get_dict()
        except:
            print("Could not reach login page")
            exit(0)

    def login(self):
        self.url = self.loginUrl
        data = {'username': self.username, 'password': self.password}
        r = requests.post(self.url, data=data, cookies=self.cookies)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            soup_user = soup.find_all("div", "user")[0].find_all("p")[0]
            self.seluser = soup_user.find_all("span")[1].string.strip()
            self.cardnum = soup_user.find_all("span")[2].string.strip()
            self.balance = soup.find_all("div", "tbpp-balances")[0].find_all("td")[1].string.strip()
        else:
            print("Could not login")
            exit(0)

    def generatePunchUrl(self):
        if self.debug:
            self.url = self.debugPunchUrl % (self.pdate)
        else:
            self.url = self.punchUrl % (self.cardnum, self.pdate, self.seluser, self.ptime, self.pdir)
       
    def punch(self, direction, time=False, date=False):
        self.pdir = self.direction[direction]
        if time:
            self.ptime = time
        else:
            self.ptime = datetime.datetime.now().strftime("%H:%M")
        if date:
            self.pdate = date
        else:
            self.pdate = datetime.datetime.now().strftime("%-d.%m.%Y")

        self.generatePunchUrl()

        r = requests.get(self.url, cookies=self.cookies)
        if r.status_code == 200:
            try:
                soup = BeautifulSoup(r.text, 'html.parser')
                self.dailybalance = soup.find_all("div", "stamps-heading")[0].find_all("p")[1].find_all("span")[0].string.strip()
                print("This day you worked " + self.dailybalance + "h")
            except:
                pass
            oldbalance = self.balance
            self.login()
            print("Balance: " + self.balance + "h (was " + oldbalance + "h)")


