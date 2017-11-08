import requests, datetime

class regweb():
    def __init__(self, username, password):
        #self.punchingUrl = "http://regweb.sanoma.fi/action-punch.asp?ptype=0&pdate="+pdate+"&pstat=32&seluser="+seluser+"&ptime="+ptime+"&pdir="+pdir+"&pcom=0&sb-fix-save=Tallenna"
        # % (pdate, seluser, ptime, pdir)
        self.punchUrl = "http://regweb.sanoma.fi/action-punch.asp?ptype=0&pdate=%s&pstat=32&seluser=%s&ptime=%s&pdir=%s&pcom=0&sb-fix-save=Tallenna"
        self.loginUrl = "http://regweb.sanoma.fi/rtp.asp"
        self.username = username
        self.password = password

        self.seluser = "625071450"
        self.pdate = ""
        self.ptime = ""

        self.direction = {
            'out': 0,
            'in': 128
        }

        self.cookies = {
            'ASPSESSIONIDQQRASBBQ':'AMFPGDEBBMNLJBBOPFPKMCIP'
        }

    def login(self):
        self.url = self.loginUrl
        self.request()

    def generatePunchUrl(self):
        self.url = self.punchUrl %  (self.pdate, self.seluser, self.ptime, self.pdir)
       
    def punch(self, direction, time=False):
        self.pdir = self.direction[direction]
        if time:
            self.ptime = time
        else:
            self.ptime = datetime.datetime.now().strftime("%H:%M")
            self.pdate = datetime.datetime.now().strftime("%-d.%m.%Y")
        self.generatePunchUrl()
        print(self.url)
        self.request()

    def request(self):
        r = requests.get(self.url, timeout=5, cookies=self.cookies)

        if r.status_code == 200:
            for cookie in r.cookies:
                print(cookie)

        print(r)

