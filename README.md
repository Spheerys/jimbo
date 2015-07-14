JIMBO 0.2.3
===========
Original source page of the project : http://www.darkcoding.net/software/jimbo/

JIMBO runs on your server, connects to a Jabber server, and adds you as its friend. This way you know your server is up.

There are also some commands available - message 'help' to the bot for details

WHAT'S NEW
----------
0.2.3: Initial project forked on github by Spheerys
0.2.2: Added RedHat startup script. Thanks Ken Staton.
0.2.1: Now runs properly as a daemon.
0.2: Added auto-reconnect, and using a class internally.

CONFIGURING
-----------

Edit jimbo_config.py. There is lots of help in that file in the comments.

INSTALLING
----------

Run the following:

sudo cp jimbo_config.py /usr/local/sbin/
sudo cp jimbo.py /usr/local/sbin/
sudo cp pyDaemon.py /usr/local/sbin/
sudo chmod u+x /usr/local/sbin/jimbo.py

sudo cp jimbo /etc/init.d/

You then need to make sure the init script gets runs when your server starts and stop.

On Gentoo 'sudo rc-update add jimbo default'.

On Redhat: sudo cp redhat-jimbo /etc/init.d/jimbo
- /sbin/service jimbo start
- /sbin/service jimbo stop

On most other Linux distributions you need to create two symlinks:
- from /etc/rc3.d/S99jimbo to /etc/init.d/jimbo
- from /etc/rc3.d/K99jimbo to /etc/init.d/jimbo.

RUNNING
-------

Start it: sudo /etc/init.d/jimbo start
Stop it: sudo /etc/init.d/jimbo stop
 
It it doesn't look right, check the log file /var/log/jimbo.log

When JIMBo starts up, it will ask to be your friend by subscribing to CONTACT. There is no real point to this, except usually your Jabber client will ask if you want to reciprocate, saving you from having to enter JIMBo's details as a contact. It also gives the impression that the machine is watching you. I'm not saying it isn't.

JIMBo will also authorize everyone in AUTHORIZED_CONTACTS to view it's status.

If it gets disconnected it will try and re-connect automatically every five seconds.

ADDING COMMANDS
---------------

*Advanced users only*

Add a method who's name starts with 'cmd_', and takes three arguments - a connection object, the authorized sender's JID, and an optional argument array. Take a look at the current commands. Give your method a docstring, and the 'help' command will pick it up automatically.


