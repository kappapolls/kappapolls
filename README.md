# kappapolls

## if you're going to clone this

There's a couple things you have to do for it to work other than the usual `pip install -r requirements.txt`

1. take the kappa_polls_bot_settings_skeleton.py file and 
use it to make a polls_bot_settings.py file that has actual login information

2. move the local_settings.py file in kappapolls/settings_extras up a directory so the 
settings file will override the production settings

3. create a file called extra.py in kappapolls/settings_extras/ that has a SECRET_KEY
and something defined for DATABASES (which can just be an empty string, as it'll be overwritten by the DATABASES
in local_settings.py

There might be other stuff too, I forget.  If there is just send me a message at /u/kappapolls and I'll add it here
