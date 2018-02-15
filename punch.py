import regweb, argparse
parser = argparse.ArgumentParser()
parser.add_argument("direction", help="in or out")
parser.add_argument("--time", help="Punch specific time eg. 10:15")
parser.add_argument("--date", help="Punch specific date eg. 01.01.2018")
args = parser.parse_args()

r = regweb.regweb('username', 'password', 'http://domain')
r.getCookie()
r.login()
if args.time and args.date:
    r.punch(args.direction, args.time, args.date)
if args.time:
    r.punch(args.direction, args.time)
else:
    r.punch(args.direction)
