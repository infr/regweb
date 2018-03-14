# Command line tool for Reg@Web

Reg@Web is a web based product to use Timecon 22 working hours monitoring tool. If you found this repo, you probably have something bad to say about the UI/UX design. Runs with Python 3.

## Setup

1. Clone the repo `git clone https://github.com/infr/regweb.git`
2. Add your username, password and domain to [punch.py](punch.py)
3. Add to your `~/.bash_profile` this `alias punch='python3 ~/[SET THE PATH]/regweb/punch.py'`
4. Run `. ~/.bash_profile`

## Usage

`punch [-h] [--time TIME] [--date DATE] [--debug] direction`

positional arguments:
  direction    in or out

optional arguments:
  -h, --help   show this help message and exit
  --time TIME  Punch specific time eg. 10:15
  --date DATE  Punch specific date eg. 01.01.2018
  --debug      Do not really punch
  
### Example usage

```bash
$ punch --time 10:15 in
Balance:  09:43h -> 09:43h
$ punch out
Balance:  09:43h -> 08:50h
```
