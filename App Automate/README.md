# python-appium-app-browserstack

This repository demonstrates how to run Appium Python tests on BrowserStack App Automate.

## Based on

These code samples are currently based on:

- **Appium-Python-Client:** `2.9.0`
- **Protocol:** `W3C`

## Setup

### Requirements

1. Python 3.7+

   > **_NOTE:_** Since v1.0.0, only Python 3.7+ is supported.

   - For Windows, download latest python version from [here](https://www.python.org/downloads/windows/) and run the installer executable
   - For Mac and Linux, run `python --version` to see what python version is pre-installed. If you want a different version download from [here](https://www.python.org/downloads/)

2. Package Manager pip

   Note : `pip` comes installed with python 3.4+

   - If `pip` is not installed, follow these instructions:

     - Securely download get-pip.py by following this link: [get-pip.py](https://bootstrap.pypa.io/get-pip.py) or use following cURL command to download it:

     ```sh
     curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
     ```

     - After dowloading, run the file :

       - For Python 3

         ```sh
         python3 get-pip.py
         ```

### Install the dependencies

To install the dependencies, run the following command in project's base directory:

- For Python 3

  ```sh
  pip3 install -r requirements.txt
  ```

## Getting Started

Getting Started with Appium tests in Python on BrowserStack couldn't be easier!

### Run your first test :

**1. Upload your Android or iOS App**

Upload your Android app (.apk or .aab file) or iOS app (.ipa file) to BrowserStack servers using our REST API. Here is an example cURL request :

```
curl -u "YOUR_USERNAME:YOUR_ACCESS_KEY" \
-X POST "https://api-cloud.browserstack.com/app-automate/upload" \
-F "file=@/path/to/apk/file"
```

Ensure that @ symbol is prepended to the file path in the above request. Please note the `app_url` value returned in the API response. We will use this to set the application under test while configuring the test later on.

**Note**: If you do not have an .apk or .ipa file and are looking to simply try App Automate, you can download and test using our [sample Android app](https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk) or [sample iOS app](https://www.browserstack.com/app-automate/sample-apps/ios/BStackSampleApp.ipa).

**2. Configure and run your first test**

- Run `python3 android/browserstack_sample.py`


## Getting Help

If you are running into any issues or have any queries, please check [Browserstack Support page](https://www.browserstack.com/support/app-automate) or [get in touch with us](https://www.browserstack.com/contact?ref=help).
