
#
# Host of your jabber server. For regular Jabber something like:
# HOST = 'jabber.org'
#
# For Google Apps For Your Domain your domain goes here
# HOST = 'example.org'
#
# For Google Talk without a gmail address:
# HOST = 'gmail.com'
#
# For Google Talk with a gmail address:
# HOST = 'googlemail.com'

HOST = 'localhost'

#
# Username JIMBo will connect to the server as. This account must already exist.
#

USERNAME = 'machine'

#
# Password JIMBo will connect to the server as. Account must already exist.
#

PASSWORD = 'machine'

#
# The resource for the account JIMBo connects as. 
# This is usually 'Home', so leave the default unless you know otherwise

RESOURCE = 'Home'

#
# A tuple of the proxy and its port.
#
# For Google Talk, or Google Apps For Your Domain:
# PROXY = ('talk.google.com',5223)
#
# If you aren't using a proxy, which is the usual Jabber case, leave this None

PROXY = None

#
# The bare JID (usually an e-mail address) of the person JIMBo will talk to.
# Alerts will be messaged to this address
#

CONTACT = 'graham@localhost'

#
# Users (JIDs - like an email address) who are allowed to contact JIMBo and query it. 
# Usually this is just your user, CONTACT, but you may wish to add friends, team members,
# or other JIDs of yours.
# For example:
# AUTHORIZED_CONTACTS = [ CONTACT, 'friend@jabber.org', 'colleague@jabber.work.com' ]
#

AUTHORIZED_CONTACTS = [ CONTACT ]

