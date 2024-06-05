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

The digital instrument cluster display is developed using the front-end tools HTML, CSS, and JavaScript as shown below. This website is developed for testing purpose.In Real time cluster HMI will be live streamed to the browser from the Electronic control unit. Testing will be done on that.

<p align="center">
  <img src="https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/dc42240c-5320-431b-b646-76678dc88259" alt="Instrument Cluster Display">
</p>

I have developed an API that will validate the presence of an icon in the given full screenshot of the HMI. The validation API will pass the test case only when:
- The specified icon to be validated comes in the ROI specified by the user. (Initially full screen ROI is given to the API. After test execution it will return the exact ROI where the icon is found)
- The matching percentage is above a certain threshold value.

## Test Case 1

<b><i>1. Click on the Tire pressure button in the HMI and wait for 7 seconds. Verify the Tire pressure icon is displayed on the HMI.</i></b>

For this test case, the script is written in `test_basic_hmi.py`. The script execution is recorded and presented below.


https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/551feaf5-5803-4228-8ae6-25d6aafd99c8



## Logs and Screenshots of the Test Execution

<b>Debug Log File</b>

[debug.log](https://github.com/user-attachments/files/15589799/debug.log) <br />
<pre>
24-06-05 07:28:03 PM: INFO: URL SUCCESSFULLY LOADED
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
24-06-05 07:28:12 PM: INFO: Button with ID:home is pressed</pre>

### Screenshots

<b>Screenshot captured:</b>

<p align="center">
  <img src="https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/dc4187f7-cd67-4c43-a6d8-e89d3e7c13a8" alt="Screenshot">
</p>

<b>Detected icon:</b>

<p align="center">
  <img src="https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/9c7401a0-2ed5-4778-8143-0df7e9a2d51e" alt="Detected Icon">
</p>

<b>Icon present in Database:</b>

<p align="center">
  <img src="https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/488b582c-1c4e-4b9c-96a6-a43248756ed9" alt="Database Icon">
</p>

## Conclusion
This project demonstrates the effectiveness of automated testing in validating the functionality of a digital instrument cluster in a car. So far I have developed an API that will perfrom the icon validation. If used on a Real time environment where the live cluster HMI is streamed over the browser, these validations through automation ensures that the Instrument cluster works as per the client specifications.

Looking ahead, future plans include the development of an API that will perform text validation within the instrument cluster. This enhancement will further improve the testing process by ensuring that all textual information displayed on the instrument cluster is accurate and correctly formatted, thus maintaining a high level of quality and user experience. And I am also planning to write more test cases.
