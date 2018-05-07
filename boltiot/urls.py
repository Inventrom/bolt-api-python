#Creating a key value store for all the urls
BASE_URL = 'http://cloud.boltiot.com/remote/'

url_list = {
    'digitalWrite' : '{}/digitalWrite?pin={}&state={}&deviceName={}',
    'digitalRead' : '{}/digitalRead?pin={}&deviceName={}',
    'analogWrite' : '{}/analogWrite?pin={}&value={}&deviceName={}',
    'analogRead' : '{}/analogRead?pin={}&deviceName={}',
    'serialBegin' : '{}/serialBegin?baud={}&deviceName={}',
    'serialWrite' : '{}/serialWrite?data={}&deviceName={}',
    'serialRead' : '{}/serialRead?till={}&deviceName={}',
    'version' : '{}/version?&deviceName={}',
    'restart' : '{}/restart?&deviceName={}',
    'isAlive' : '{}/isAlive?&deviceName={}',
    'isOnline' : '{}/isOnline?&deviceName={}',
}

def url(operation):
    return BASE_URL+url_list[operation]
