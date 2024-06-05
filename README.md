# Instrument-cluster-automation-testing
## Objective
The objective of this project is to perform Automation testing on a digital Instrument cluster of a car.
## Tools used
Python
HTML
CSS
Javascript
SQL
Selenium webdriver
pytest framework

## Description

Th digital instrument cluster display is developed using the front-end tools HTML, CSS and Javascript as shown below.
![image](https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/dc42240c-5320-431b-b646-76678dc88259)



I have developed an API that will validate the presence of icon in the given full screenshot of the HMI. 
Validation API will pass the test case only when;

the specified icon to be validated comes in the ROI specified by the user
Matching percentage is above a certain threshold value.

## Test Case 1:
## 1. Click on the Tire pressure button in the HMI and wait for 7 secs and Verify the Tire pressure icon is displayed on the HMI.

## For this test case the script is written in test_basic_hmi.py. THe script execution is recorded and presented below




https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/551feaf5-5803-4228-8ae6-25d6aafd99c8




## Here are the logs and screenshots of the Test execution:

### Debug log file : [debug.log](https://github.com/user-attachments/files/15589799/debug.log)24-06-05 07:28:03 PM: INFO: URL SUCCESSFULLY LOADED
24-06-05 07:28:03 PM: INFO: ICON DB sucessfully loaded
24-06-05 07:28:03 PM: INFO: Button with ID:tpms is pressed
24-06-05 07:28:10 PM: INFO: Screenshot successfully captured and saved in path:D:\Automation_testing\Logs\logs_2939447506\screenshot.png
24-06-05 07:28:10 PM: INFO: icn_tpms_icon is sucessfully read from the database
24-06-05 07:28:11 PM: INFO: Detection result for icn_tpms_icon
24-06-05 07:28:11 PM: INFO: TELLTALE STATUS IS ON
24-06-05 07:28:11 PM: INFO: top left coordinates: (893, 289)
24-06-05 07:28:11 PM: INFO: bottom right coordinates: (1251, 623)
24-06-05 07:28:11 PM: INFO: ICON saved as detected_icon_icn_tpms_icon.png
24-06-05 07:28:11 PM: INFO: confidence_detected: 0.7948028445243835
24-06-05 07:28:12 PM: INFO: Button with ID:home is pressed

### Screenshot captured: ![screenshot](https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/dc4187f7-cd67-4c43-a6d8-e89d3e7c13a8)
### Detected icon: ![detected_icon](https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/9c7401a0-2ed5-4778-8143-0df7e9a2d51e)
### Icon present in Database: ![database_icon_icn_tpms_icon](https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/488b582c-1c4e-4b9c-96a6-a43248756ed9)










