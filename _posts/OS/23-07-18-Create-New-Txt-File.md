---
title: Create New Txt File
date: 2023-07-18 08:00:00 -700
categories: [OS,Mac]
tags: [mac,mac-tricks]
---

## Create New Txt File in Any Folder on Mac
One great feature in Windows is the ability to create a new blank text file from the right-click context menu, but this feature doesn’t exist on Mac natively. However, it is possible, though more complex than a simple right-click. The best way to do this on a Mac is to create a Quick Action.

1. Launch the Automator app to create a script, which will help you create a new blank text file in any folder.
2. Select the Quick Actions.
3. From here, you’ll want to drag the action named "Run AppleScript" from the Actions panel on the left and drop it into the workflow panel on the right. Note that you may need to search for it using the small search bar at the top.
4. You’ll notice an AppleScript editor appear in the workflow panel. Clear out the contents and paste the following script:
```
tell application "Finder" to make new file at (the target of the front window) as alias
```
5. Click on the "File" menu on the top and select "Save" and name it "New Text File"
6. To use navigate to the “Finder -> Services” menu, within the toolbar, and find your new Quick Action called "New Text File". Go to any folder and give your quick action a try.