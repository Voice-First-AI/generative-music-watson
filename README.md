Getting Started

1. Clone Repo.
2. Setup Python 2.7 env. This Repo DOES NOT WORK with Python 3.
3. `virtualenv -p /usr/bin/python2.7  temp-python  `
4. Activate your virtual environment: `source temp-python/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. `cd src/`
7. `python wbDev.py -m Midi/hello.mid -i Ini/Chill.ini`
8. Tada! Your song should be in the output folder.