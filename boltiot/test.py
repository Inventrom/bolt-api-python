from bolt import Bolt

#Creating all test cases

#Creating a client
client = Bolt('768d64d5-05b2-463b-95bc-98eedfc5abe7', 'BOLT3432361')

#Testing digitalWrite
result = client.digitalWrite('0','HIGH')

#Testing digitalRead
#result = client.digitalRead('0')

#Testing analogWrite
#result = client.analogWrite('A0','127')

#Testing analogRead
#result = client.analogRead('A0')

#Testing UART commands

#result = client.serialBegin('9600')
#result = client.serialRead('12')
#result = client.serialWrite('hello')

#Version check
#result = client.version()

#Device Restart
#result = client.restart()

#Device status
#result = client.isAlive()

print(result)
