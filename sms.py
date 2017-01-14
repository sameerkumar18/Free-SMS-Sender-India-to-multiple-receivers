import requests

username = '__smsidea_registered_mobile_number'
password = '__smsidea_password__'
channel = 'SMSWEB' #usually this until you don't buy paid plan
receiver_number = '__mobile_no_to_which_sms_is_to_be_sent__'
#for many numbers
#receiver_number = '__mobile_no_1__,__mobile_no_2__,__mobile_no_3__'
#all separeated by a comma (inside '')

message = '__body_of_message__' #spaces should be replaced by '%20', {usually '%20' is automatically applied}

url = 'http://www.smsidea.co.in/sendsms.aspx?mobile=%s&pass=%s&senderid=%s&to=%s&msg=%s' % (username, password, channel, receiver_number, message)

requests.get(url)
# fyi smsidea has some limitations also
