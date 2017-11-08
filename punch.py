import regweb, sys
direction = sys.argv[1]
r = regweb.regweb('user', 'password')
r.punch(direction)
#r.punchOut()
#r.punchIn()