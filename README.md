# what are you doing? (wayd)

Couldn't find a program to do what I wanted, so I built my own. Currently very hacky.

wayd is a python script that uses `launchd` to pop up every 15 minutes to ask what you're doing with a text input box. Fill in your current activity and it creates/appends a markdown file named with today's date with the current time and your activity.

If this is the first time wayd has run today, it creates a new file named dd-mm-yyyy.md that looks like this:

> # dd.mm.yyyy
>## today i will
>>==thrive (`or your own goal`)==
>
>## ideas // thoughts // things i did
>* time: activity

If wayd has already run or there's already a file named dd-mm-yyyy.md in the directory, then it just appends `* time: activity` to the end of the file.

You can keep the file open and add your own content to it as well, giving you a daily file with a mix of thoughts and timestamped activities.

## dependencies
* PySimpleGUI
* datetime
* schedule

## to use
* download `wayd.py` and `com.kailanathaniel.wayd.plist`
* download dependencies with `pip3 install PySimpleGUI datetime schedule`
* open `wayd.py` in your text editor and set `folder_path` to where you want your files saved
* open `com.kailanathaniel.wayd.plist` in your text editor and set the first string under `ProgramArguments` to where your python executable is stored and the second string to where you've stored `wayd.py`
* use terminal to navigate to the folder with `com.kailanathaniel.wayd.plist` and move it to your `LaunchAgents` folder with `mv com.kailanathaniel.wayd.plist ~/Library/LaunchAgents/`
* start the agent with `launchctl bootstrap gui/<user id> ~/Library/LaunchAgents/com.kailanathaniel.wayd.plist`

## tips
* find your user ID by running `id -u` in terminal
* find where your python executable is stored by running `which python` in terminal
* stop the agent with `launchctl bootout gui/<user id> ~/Library/LaunchAgents/com.kailanathaniel.wayd.plist`
* if you want to be able to stop and start the agent with a single command, add these two lines to your `.bash_profile` to start/stop the agent by running `wayd_start` and `wayd_pause` in your terminal
    * `alias wayd_start="launchctl bootstrap gui/<user id> ~/Library/LaunchAgents/com.kailanathaniel.wayd.plist"`
    * `alias wayd_pause="launchctl bootout gui/<user id> ~/Library/LaunchAgents/com.kailanathaniel.wayd.plist"`
* customize how often wayd runs by changing the number under `StartInterval` in `com.kailanathaniel.wayd.plist` (it's in seconds)
* customize the new file template by changing the string under `#if file doesn't exist` line in `wayd.py`


## future
* [ ] add ability to save settings
* [ ] package as standalone app
* [ ] make it prettier
