import unittest
import operative
import datetime

from caliendo.patch import patch
from nose.tools import eq_, ok_
from operative.settings import TEST_FTP_LOGIN


class ReportTest(unittest.TestCase):

    """
    Test the various reports.

    """

    @patch('operative.FTPConnection.get_files')
    @patch('operative.FTPConnection._establish_connection')
    @patch('operative.FTPConnection._close_connection')
    def test_line_item_report(self):
        """
        Test LineItemReport

        """
        from operative.reports.line_item_report import LineItemReport
        from fixtures.line_item import line_items as line_item_fixtures

        def __get_and_test(path, since, num_expected_files):
            ftp_creds = operative.FTPCredentials(**TEST_FTP_LOGIN)
            line_item_reports = LineItemReport().get_report_files(ftp_credentials=ftp_creds, ftp_path=path, since=since)
            line_item_reports.reverse()

            eq_(len(line_item_reports), num_expected_files)
            for i, lir in enumerate(line_item_reports):
                eq_(lir.data[0].to_json(return_dict=True), line_item_fixtures[i])

        # get all files
        __get_and_test(path='/flatfile', since=None, num_expected_files=2)

        # get one file - using "since"
        __get_and_test(path='/flatfile', since=datetime.datetime(2014, 1, 7, 0, 42), num_expected_files=1)

        # get zero files - using "since"
        __get_and_test(path='/flatfile', since=datetime.datetime(2014, 2, 1), num_expected_files=0)

        # get zero files - only directories in path
        __get_and_test(path='/', since=None, num_expected_files=0)
