"""
#!/usr/bin/env python
# title           : test_suits.py
# description     : This file contains code for running automated tests
# author          : Abhishek <abhishek@artifacia.com>
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
    # get all tests from Homepage class
    homepage_test_names = unittest.TestLoader().getTestCaseNames(Homepage)
    print homepage_test_names
    test_suite = unittest.TestSuite()

    for homepage_test_name in homepage_test_names:
        test_suite.addTest(Homepage(homepage_test_name))

    # run the suite
    unittest.TextTestRunner().run(test_suite)
    # open the report file
    outfile = open("SeleniumPythonTestSummary.html", "w")

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=outfile, title='Test Report', description='UI Automation Test')
    # run the suite using HTMLTestRunner
    runner.run(test_suite)

    # move html report to templates directory
    shutil.move("SeleniumPythonTestSummary.html", "./templates/plivo_automation_report.html")

test_suite()
