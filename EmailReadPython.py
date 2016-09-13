import urllib2
import untangle

myUser = "testertestertester402@gmail.com"
myPass = "****"

FEED_URL = 'https://mail.google.com/mail/feed/atom'
 
def get_msgs(user, passwd):
    auth_handler = urllib2.HTTPBasicAuthHandler()
    print "Getting Messages for " + user + " at " + passwd
    auth_handler.add_password(
        realm='mail.gmail.com',
        uri='https://mail.gmail.com',
        user='%s@gmail.com' % user,
        passwd=passwd
    )
    print "Opening"
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    print "Getting feed"
    feed = urllib2.urlopen(FEED_URL)
    print "Got feed"
    return feed.read()
 
##########

if __name__ == "__main__":
    import getpass
 
    #user = raw_input('Username: ')
    #passwd = getpass.getpass('Password: ')
    #print get_unread_msgs(user, passwd)

    xml = get_msgs(myUser, myPass)
    print "Got XML"
    o = untangle.parse(xml)
    try:
    	for i in range[0, 3]:
    		title = o.entry[i]
    		fullTitle = fullTitle + title
    except IndexError:
        pass # no new mail

print fullTitle



