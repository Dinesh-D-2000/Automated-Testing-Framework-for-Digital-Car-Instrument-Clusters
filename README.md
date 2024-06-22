<h1 style="display: flex; align-items: center;">
  <img src="https://github.com/Dinesh-D-2000/cluster_hmi_tests/assets/109975786/75670ab4-9b35-4e21-8ce7-6333f3991cf6" alt="Python-logo-notext svg" style="width: 30px; height: 30px; margin-right: 10px;">
  PYTHON'S MASTERY IN AUTOMATION TESTING ON DIGITAL INSTRUMENT CLUSTERS
</h1>

## Objective

The objective of this project is to perform automation testing on a custom developed digital instrument cluster of a car.

## Tools

- Python
- HTML
- CSS
- JavaScript
- SQL
- Selenium WebDriver
- Pytest Framework
- [cluster_hmi_test_lib](https://github.com/Dinesh-D-2000/cluster_hmi_test_lib)
- [cluster_hmi_resources](https://github.com/Dinesh-D-2000/cluster_hmi_resources)

## Description

The digital instrument cluster display is developed using the front-end tools HTML, CSS, and JavaScript as shown below. This website is developed for testing purpose.In Real time cluster HMI will be live streamed to the browser from the Electronic control unit. Testing will be done on that. The API libraries are provided by the [cluster_hmi_test_lib](https://github.com/Dinesh-D-2000/cluster_hmi_test_lib) repository and the resources for this project is provided by [cluster_hmi_resources](https://github.com/Dinesh-D-2000/cluster_hmi_resources) reopsitory.

<p align="center">
  <img src="https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/dc42240c-5320-431b-b646-76678dc88259" alt="Instrument Cluster Display">
</p>



## Test Cases
<table>
  <tr>
    <th>Steps to perform</th>
    <th>Validation to perform</th>
  </tr>
  <tr>
<td><b><i>1. Click on the Tire pressure button in the HMI and wait for 7 seconds.</i></b></td>
<td> <b><i> Verify the Tire pressure icon is displayed on the HMI.</i></b></td>
  </tr>
    <tr>
<td><b><i>2. Click on the Drive mode button in the HMI and wait for 4 seconds.</i></b></td>
<td> <b><i> Verify the Warning, W123 with text "Active ParkSense Searching" displayed on the HMI.</i></b></td>
  </tr>
  <tr>
<td><b><i>3. Click on the Fuel economy button in the HMI and wait for 4 seconds.</i></b></td>
<td> <b><i>  Verify the Warning, W456 with text "Fuel Economy" displayed on the HMI.</i></b></td>
  </tr>
</table>



For these test cases, the script is written in [test_basic_hmi.py](https://github.com/Dinesh-D-2000/cluster_hmi_tests/blob/main/hmi_tests/tests/test_basic_hmi.py). The script execution is recorded and presented below.


https://github.com/Dinesh-D-2000/Instrument-cluster-automation-testing/assets/109975786/551feaf5-5803-4228-8ae6-25d6aafd99c8



## Logs and Screenshots of the Test Execution
<b><i>Test case 1: Click on the Tire pressure button in the HMI and wait for 7 seconds and Verify the Tire pressure icon is displayed on the HMI</i></b>
<b>Debug Log File</b>

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
-----------------------------------------------------------------------------------------------------------------------------------------------------------
<b><i>Test case 2: Click on the Drive mode button in the HMI and wait for 4 seconds and Verify the Warning, W123 with text "Active ParkSense Searching" displayed on the HMI</i></b>
<b>Debug Log File</b>


<pre>
24-06-21 09:01:39 PM: INFO: URL SUCCESSFULLY LOADED
24-06-21 09:01:39 PM: INFO: ICON DB sucessfully loaded
24-06-21 09:01:39 PM: INFO: Button with ID:drive_mode is pressed
24-06-21 09:01:44 PM: INFO: Screenshot successfully captured and saved in path:D:\MY_OFFICIAL_PROJECTS\CLUSTER_HMI_TESTING\\cluster_hmi_tests\hmi_tests\Logs\logs_1003445403\screenshot.png
24-06-21 09:01:45 PM: INFO: Warning W123 with text Active ParkSense Searching is ON
24-06-21 09:01:45 PM: INFO: top_left_coordinates: [660, 182]
24-06-21 09:01:45 PM: INFO: bottom_right_coordinates: [1530, 285]
24-06-21 09:01:45 PM: INFO: Button with ID:home is pressed</pre>


<b>Screenshot captured:</b>


<p align="center">
  <img src="https://github.com/Dinesh-D-2000/cluster_hmi_tests/assets/109975786/a38ee3bb-4c4b-47b4-aeb3-7e02051e7e74" alt="Screenshot">
</p>

<b>Detected Region:</b>


<p align="center">
  <img src="https://github.com/Dinesh-D-2000/cluster_hmi_tests/assets/109975786/aacde164-8490-4780-9dc1-d25a6799c106" alt="Detected Region">
</p>
-----------------------------------------------------------------------------------------------------------------------------------------------------------


<b><i>Test case 3: Click on the Fuel economy button in the HMI and wait for 4 seconds and Verify the Warning, W456 with text "Fuel Economy" displayed on the HMI</i></b>
<b>Debug Log File</b>

<pre>
24-06-21 08:35:32 PM: INFO: URL SUCCESSFULLY LOADED
24-06-21 08:35:32 PM: INFO: ICON DB sucessfully loaded
24-06-21 08:35:32 PM: INFO: Button with ID:fuel_economy is pressed
24-06-21 08:35:37 PM: INFO: Screenshot successfully captured and saved in path:D:\MY_OFFICIAL_PROJECTS\CLUSTER_HMI_TESTING\\cluster_hmi_tests\hmi_tests\Logs\logs_0038082456\screenshot.png
24-06-21 08:35:37 PM: INFO: Warning W456 with text Fuel Economy is ON
24-06-21 08:35:37 PM: INFO: top_left_coordinates: [660, 182]
24-06-21 08:35:37 PM: INFO: bottom_right_coordinates: [1530, 285]
24-06-21 08:35:37 PM: INFO: Button with ID:home is pressed</pre>


<b>Screenshot captured:</b>


<p align="center">
  <img src="https://github.com/Dinesh-D-2000/cluster_hmi_tests/assets/109975786/026559b6-c8f4-4f73-bc93-bacf359e054d" alt="Screenshot">
</p>

<b>Detected Region:</b>

<p align="center">
  <img src="https://github.com/Dinesh-D-2000/cluster_hmi_tests/assets/109975786/13039f3b-bb0f-4da2-a01c-21e30d64b80d" alt="Detected Region">
</p>


## Conclusion
This project demonstrates the effectiveness of automated testing in validating the functionality of a digital instrument cluster in a car. I have developed 3 test cases. If used on a Real time environment where the live cluster HMI is streamed over the browser, these validations through automation ensures that the Instrument cluster works as per the client specifications. These Image and text validation ensures that all information displayed on the instrument cluster is accurate and correctly formatted, thus maintaining a high level of quality and user experience.
