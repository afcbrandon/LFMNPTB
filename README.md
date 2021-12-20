#LFMNPTB
Last.Fm Now Playing Twitter Bio
![](https://i.imgur.com/OUvoxHY.png)


### Features

-  update your twitter bio with your currently playing track from Last.FM
- keep your bio and just add a "now playing" portion
- simple code that is able to run as a cron job every 4 min.
- pulls from last.fm so where you scrobble from will be displayed.

# Install

`$ git clone https://github.com/afcbrandon/LFMNPTB.git`
`$ cd LFMNPTB`
`$ pip install -r requirements.txt`
`$ nano np.py`

Repalce with your information
![](https://i.ibb.co/4pBxj0n/Screen-Shot-2021-12-20-at-12-48-47-AM.png)

save

# Usage

`$ python3 np.py`

# Cron job install

here are my settings for the cron job I set for the script to run every 5 min.

`crontab -e`

make sure to use the direct path python3 and the script

`*/5 * * * * /usr/bin/python3 /direct/path/to/the/script/np.py > /dev/null 2>&1`

"> /dev/null 2>&1" turns of mail and logs for this script since it will be running so much.

[follow me on twitter](https://twitter.com/brandonandrsn)
