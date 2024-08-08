# BrowserStack Python On-boarding Assignment
This repo defines the test scripts for the [BrowserStack demo website](https://bstackdemo.com).

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)
## Prerequisite
* Python3

## Setup##

* Clone the repo
* Install dependencies `pip install -r requirements.txt`
* To run your automated tests using BrowserStack, you must provide a valid username and access key. This can be done either by using a .browserstack configuration file in the working directory or your home directory, by setting the BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY environment variables, or by adding user & key to config file.

## About the tests in this repository

This repository contains the following Cucumber tests:

| Module  | Test name                           | Description                                                                                                                                                                                                                                                                       | Tag     |
| ------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| E2E     | End to End Scenario                 | This test scenario verifies successful product purchase lifecycle end-to-end. It demonstrates the [Page Object Model design pattern](https://www.browserstack.com/guide/page-object-model-in-selenium-python) and is also the default test executed in all the single test run profiles. | e2e     |
| Login   | Login with given username           | This test verifies the login workflow with different types of valid login users.                                                                                                                                                                                                  | login   |
| Login   | Login as Locked User                | This test verifies the login workflow error for a locked user.                                                                                                                                                                                                                    | login   |
| Offers  | Offers for Mumbai location          | This test mocks the GPS location for Mumbai and verifies that the product offers applicable for the Mumbai location are shown.                                                                                                                                                    | offers  |
| Product | Apply Apple & Samsung Vendor Filter | This test verifies that only Apple and Samsung products shown if the Apple and Samsung vendor filter option is applied.                                                                                                                                                           | product |
| Product | Apply Lowest to Highest Order By    | This test verifies that the product prices are in ascending order when the product sort "Lowest to Highest" is applied.                                                                                                                                                           | product |
| User    | Login as User with no image loaded  | This test verifies that the product images load for user: "image_not_loading_user" on the e-commerce application. Since the images do not load, the test case assertion fails.                                                                                                    | user    |
| User    | Login as User with existing Orders  | This test verifies that existing orders are shown for user: "existing_orders_user"                                                                                                                                                                                                | user    |



---
# On Premise

This infrastructure points to running the tests on your own machine using a browser (e.g. Chrome) using the browser's driver executables (e.g. ChromeDriver for Chrome). Selenium enables this functionality using WebDriver for many popular browsers.

## On-Prem Prerequisites

-   For this infrastructure configuration (i.e on-premise), ensure that the ChromeDriver is downloaded and added to the [driver](src/driver) directory.

Note: The ChromeDriver version must match the Chrome browser version on your machine.

## Running Your Tests

### Run the entire test suite on your own machine

-   How to run the test?

    To run the entire test suite on your own machine, use the following command:

    ```sh
    paver run single on-prem
    ```

-   Output

    This run profile executes the entire test suite sequentially on a single browser, on your own machine.

# Tech_Assignments
