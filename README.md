# Update-Required

Responsible for implementing a system to determine which app update will be installed on various devices depending on their device operating system and time of last app update on their device.

My system will be provided with a list of user's information, following the following format:  
`['serialNum', 'OS Type', 'OS Version', 'Update Date']`

Each entry in the sub-list is explained below:  
**serialNum**: A string with length 8 that represents the smartphone's serial number.  
**OS Type**: A string representing operating system type with the value iOS or Android.  
**OS Version**: A string representing operating system version.  
**Update Date**: A string representing the latest app update date on that device (YYYY-MM-DD).

The following list of lists provides an example of data used by my system. Each sub-list follows the format given above. There are 3 devices in this example:

```python
devices = [
    ['BX001321', 'iOS', '12.0', '2019-01-03'],
    ['GX021629', 'Android', '11.0', '2019-08-06'],
    ['BX101129', 'iOS', '8.0', '2019-05-22']
]
```
The update considers two operating systems: MAC iOS or ANDROID OS. There are 4 different app updates available, and they are compatible with different devices depending on the OS Type, OS Version, and Update Date. The following table depicts this set of criteria for each update version:

### Table 1: Criteria to determine app update version
| OS Type | OS Version                                | App Update Criteria                   | App Update Version |
|---------|-------------------------------------------|---------------------------------------|--------------------|
| iOS     | Version 8.0 or higher                     | At any date of last update            | Version 1          |
| iOS     | Version less than 8.0                     | At any date of last update            | No Update          |
| Android | Version 10.0 or higher                    | At any date of last update            | Version 2          |
| Android | Version 8.0 to 10.0 (not including 10.0)  | Last update between January and June  | Version 3          |
| Android | Version 8.0 to 10.0 (not including 10.0)  | Last update between July and December | Version 4          |
| Android | Version less than 8.0                     | At any date of last update            | No Update          |

Given this information, my task is to generate a list of devices and their update version required.
