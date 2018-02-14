import regweb, sys
r = regweb.regweb('username', 'password', 'http://domain', "seluser/tunniste", "cardnum/henkilönumero")
r.getCookie()
r.login()
if len(sys.argv) == 2:
    direction = sys.argv[1]
    r.punch(direction)