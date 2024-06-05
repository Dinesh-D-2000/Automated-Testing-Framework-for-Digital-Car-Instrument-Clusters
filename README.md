# Instrument-cluster-automation-testing

## Objective

The objective of this project is to perform automation testing on a digital instrument cluster of a car.

## Tools Used

- Python
- HTML
- CSS
- JavaScript
- SQL
- Selenium WebDriver
- pytest framework

## Description

The digital instrument cluster display is developed using the front-end tools HTML, CSS, and JavaScript as shown below.
![image](https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/dc42240c-5320-431b-b646-76678dc88259)

I have developed an API that will validate the presence of an icon in the given full screenshot of the HMI. The validation API will pass the test case only when:
- The specified icon to be validated comes in the ROI specified by the user.
- The matching percentage is above a certain threshold value.

## Test Case 1

1. Click on the Tire pressure button in the HMI and wait for 7 seconds. Verify the Tire pressure icon is displayed on the HMI.

For this test case, the script is written in `test_basic_hmi.py`. The script execution is recorded and presented below.

[![Test Case Video](https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/551feaf5-5803-4228-8ae6-25d6aafd99c8)](https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/551feaf5-5803-4228-8ae6-25d6aafd99c8)

## Logs and Screenshots of the Test Execution

### Debug Log File

[debug.log](https://github.com/user-attachments/files/15589799/debug.log)


### Screenshots

- Screenshot captured:
![screenshot](https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/dc4187f7-cd67-4c43-a6d8-e89d3e7c13a8)

- Detected icon:
![detected_icon](https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/9c7401a0-2ed5-4778-8143-0df7e9a2d51e)

- Icon present in Database:
![database_icon_icn_tpms_icon](https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/488b582c-1c4e-4b9c-96a6-a43248756ed9)
