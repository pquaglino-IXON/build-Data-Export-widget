## Build "Data Export" widget - For IXON Studio ##
This Python program creates a "Data export" widget, automatically configured with a list of tags. \
This is specially useful if you have a lot of tags and you want to easily backup data manually.

Follow these steps:
1. Go to the [Fleet Manager](https://portal.ixon.cloud/fleet-manager/devices), pick a datasource from a device, go to Tags and click "Export to CSV file". Name the file "data-tags.csv"
2. Edit the file keeping the tags you are interested in
3. Execute the program, it will create a json file (output.json)
4. Open the json file and copy the content
5. Go to the [IXON Studio](https://portal.ixon.cloud/studio/pages/device), open a page for editing
6. Right-click and paste (or Ctrl-v / Cmd-v)

Done!\
Now open the page from the [Portal](https://portal.ixon.cloud/portal/devices), pick a suitable time period, click the button and download the data.

__Notes__
- This program adds only the tags sampled by interval. To change this edit lines 10-11
- The file data-tags.csv here is provided as an example.
- The device you choose is only important for its Tags list. The widget will work with any device with the same tags.