# Simple FPL USER WAYPOINT extractor

### Background
I needed a way to create custom flight plan waypoints and then import them into my Garmin GTN-650.  The GTN series navigators don't natively recognize .fpl or even garmin .gpx files, instead opting to let you *import waypoints from a file named user.wpt*. 
Ref: https://support.garmin.com/en-US/?faq=3mcdU37gXi88ipwjJIxJo7 

### Solution
I use SkyVector (https://www.skyvector.com/) to create my flight paths, and it lets you export the flight plan as an (XML format) .fpl file.  So, I wrote a quick & dirty python utility to convert the USER WAYPOINTS into custom user.wpt waypoints.

**Note:**  I'm only importing and converting the FPL waypoints marketd "USER WAYPOINT".  The GTN series won't import a user waypoint that's colocated with a known database waypoint anyway, so you'll have to manually add those to your flight plan in between the appropriate user waypoints when you construct it in the GTN.  This would be the case whether I exported the known waypoints or not.  :shrug:

### Usage
- Export a .fpl file
- run ```fpl-to-csv.py filename```
- rename ```filename.csv ``` to ```user.wpt``` and copy it to a SD card
- Follow the instructions in https://support.garmin.com/en-US/?faq=3mcdU37gXi88ipwjJIxJo7 to import user.wpt into your GTN
- Create a new flight plan with the newly imported user waypoints

You can optionally add a PREFIX to the command line and it'll replace the first two letters of the user waypoints in the .fpl file with that prefix.  Useful if you're creating / importing multiple flight plans and want to keep the waypoints identifyable in the GTN.

### Disclaimer
Use at your own risk.  I make no warranties as to whether this code works or not, nor do I support it.
