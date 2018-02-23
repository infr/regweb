import regweb, argparse
parser = argparse.ArgumentParser()
parser.add_argument("direction", help="in or out")
parser.add_argument("--time", help="Punch specific time eg. 10:15")
parser.add_argument("--date", help="Punch specific date eg. 01.01.2018")
parser.add_argument("--debug", help="Do not really punch", action="store_true", default=False)
args = parser.parse_args()

r = regweb.regweb('username', 'password', 'http://domain', debug=args.debug)
r.getCookie()
r.login()
if args.time and args.date:
    r.punch(args.direction, time=args.time, date=args.date)
elif args.time and not args.date:
    r.punch(args.direction, time=args.time)
elif args.date:
    r.punch(args.direction, date=args.date)
else:
    r.punch(args.direction)
