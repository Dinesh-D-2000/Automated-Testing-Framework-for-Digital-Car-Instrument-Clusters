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

## For this test case the script is written in test_basic_hmi.py.
All the APIs required for this test case is written in api.py under test_lib package.

Here ar the logs and screenshots of the Test execution:

![screenshot](https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/d5ba96d3-a3f9-4788-b4a9-098e70c118a3)
![database_icon_icn_tpms_icon](https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/faf9b745-6dc1-493d-abe7-98f16c8800a0)
[debug.log](https://github.com/user-attachments/files/15588686/debug.log)
[detected_icon](https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/f605dfe2-12c1-4ef3-8bd9-50f6d2fa5afd)





