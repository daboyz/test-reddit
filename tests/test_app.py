#!/usr/bin/env python3
from tests import mock_data
from tests.logger import *
from reddit import app, api, ui
import click
from click.testing import CliRunner
import pytest
import subprocess
import os
import sys
from threading import Thread

'''
MVP:
Test accepts function and assert expression (test data and expected result) as params
Test suite should include testing for all parameters
Use pytest-bdd
Run in Docker
HAve nice pattern for docker launch and tests structure
Use TCP/IP networking https://www.ibm.com/developerworks/ru/library/l-python_part_10/index.html
'''

@pytest.fixture(params=['nodict', 'dict'])
def initialize_test_run(request):  # For example purposes only
    LOG_DEBUG("Generate initial parameters and create CLI Runner")
    pass


test_input = mock_data.test_input
expected_output = mock_data.expected_output

runner = CliRunner()     # Create CLI RUNNER ?? TODO


@pytest.mark.usefixtures('mock_api_search_subreddits_response')
class TestSearch:

    @pytest.fixture
    def mock_api_search_subreddits_response(self, monkeypatch):
        LOG_DEBUG("Mock API response setup outside class for Search")
        monkeypatch.setattr('reddit.api.search_subreddits', mock_data.api_search_subreddits)

    def search_result(self, query):
        return runner.invoke(app.search, [query]).output

    def test_search_positive(self):
        LOG_DEBUG("Test Search positive")
        assert self.search_result('configure') == expected_output['search_positive']

    def test_search_two(self):
        LOG_DEBUG("Test Search positive 2")
        assert self.search_result('ShowerThoughts').startswith('# Shower')


@pytest.mark.usefixtures('mock_api_list_subreddits_response')
class TestTop10:

    @pytest.fixture
    def mock_api_list_subreddits_response(self, monkeypatch):
        LOG_DEBUG("Dedicated list_subreddits api response setup")
        monkeypatch.setattr('reddit.api.list_subreddits', mock_data.api_list_subreddits)

    def top10_result(self, sort_order):         # TODO move to utils file
        return runner.invoke(app.top10, [sort_order]).output

    def test_top10_positive(self):
        LOG_DEBUG("Test top10 positive")
        assert self.top10_result('popular').startswith('# Popular')

    def test_top10_negative(self):
        LOG_DEBUG("Test top10 negative")
        assert self.top10_result('gold').startswith('# Gold')


@pytest.mark.usefixtures('mock_api_get_submissions_response')
class TestSubreddit:

        @pytest.fixture
        def mock_api_get_submissions_response(self, monkeypatch):
            LOG_DEBUG("Dedicated get_submissions api response setup")
            monkeypatch.setattr('reddit.api.get_submissions', mock_data.api_get_submissions)

        def subreddit_result(self, name):  # TODO move to utils file
            return runner.invoke(app.subreddit, [name]).output

        def test_subreddit_positive(self):
            LOG_DEBUG("Test subreddit positive")
            #assert self.subreddit_result('gonewild').startswith('Showing first ')

        def test_subreddit_negative(self):
            LOG_DEBUG("Test subreddit negative")
            #assert self.subreddit_result('ShowerThoughts').startswith('Showing first 1 submissions\n\n')
            # GET DATA HERE
            #for r in api.get_submissions('gonewild'): print(r)
            #for d in list(app.search(['configure'])): print(d)
            #for r in (runner.invoke(api.get_submissions, ['gonewild']).output): print(r)
            # for r in app.subreddit(['gonewild']): print(r)
            print(runner.invoke(app.subreddit, ['gonewild']).output)

            print('pure', list(api.get_submissions('ShowerThoughts', 100)))
            print('mock', list(mock_data.api_get_submissions('ShowerThoughts')))


@pytest.mark.usefixtures('mock_api_get_comments_response')
class TestSubmission:

        @pytest.fixture
        def mock_api_get_comments_response(self, monkeypatch):
            LOG_DEBUG("Dedicated get_comments api response setup")
            #monkeypatch.setattr('reddit.api.get_submissions', mock_data.api_get_submissions)

        def submission_result(self, name):  # TODO move to utils file
            return runner.invoke(app.submission, [name]).output

        def qtest_subreddit_positive(self):
            LOG_DEBUG("Test subreddit positive")
            assert self.submission_result('gonewild').startswith('Showing first 10 submissions\n\n')

        def qtest_subreddit_negative(self):
            LOG_DEBUG("Test subreddit negative")
            assert self.submission_result('ShowerThoughts').startswith('Showing first 10 submissions\n\n')
            # GET DATA HERE
            #for r in api.get_submissions('gonewild'): print(r)
            #for d in list(app.search(['configure'])): print(d)
            #print(runner.invoke(app.subreddit, ['ShowerThoughts']).output)
            # for r in app.subreddit(['gonewild']): print(r)
            # print(app.search(['gonewild']))

''' 
def test_initial_transform(generate_initial_parameters):  # Example of how to write test
    test_input = generate_initial_transform_parameters[0]
    expected_output = generate_initial_transform_parameters[1]
    assert app.initial_transform(test_input) == expected_output
        
'''