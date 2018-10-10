"""
#!/usr/bin/env python
# title           : test_suits.py
# description     : This file contains code for running automated tests
# author          : Abhishek <abhishek@artifacia.com>
# License: Closed, Don't use without explicit permission of Artifacia
# python_version  : 2.7
#===============================================================================
"""

import shutil
import unittest

from test.plivo_ui_automation import Homepage

import HTMLTestRunner


def test_suite():
    """
    This function runs automated tests to test plivo_ui_automation
    """
    # get all tests from SearchText and HomePageTest class
    homepage_test_names = unittest.TestLoader().getTestCaseNames(Homepage)
    print homepage_test_names
    test_suite = unittest.TestSuite()

    for homepage_test_name in homepage_test_names:
        test_suite.addTest(Homepage(homepage_test_name))

    # run the suite
    unittest.TextTestRunner(verbosity=2).run(test_suite)
    # open the report file
    outfile = open("SeleniumPythonTestSummary.html", "w")

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=outfile, title='Test Report', description='Acceptance Tests')
    # run the suite using HTMLTestRunner
    runner.run(test_suite)

    # move html report to templates directory
    # if mode == "stage":
    shutil.move("SeleniumPythonTestSummary.html", "./templates/plivo_automation_report.html")
    # elif mode == "prod":
    #     shutil.move("SeleniumPythonTestSummary.html", "./templates/report-prod.html")

test_suite()
