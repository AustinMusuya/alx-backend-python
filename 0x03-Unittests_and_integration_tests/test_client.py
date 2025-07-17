#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org returns expected result with correct URL"""
        expected_result = {"login": org_name}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected_result)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch("client.GithubOrgClient.org", new_callable=property)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns expected URL based on mocked org"""
        expected_url = "https://api.github.com/orgs/google/repos"
        mock_org.return_value = {"repos_url": expected_url}
        client = GithubOrgClient("google")

        result = client._public_repos_url

        self.assertEqual(result, expected_url)
        mock_org.assert_called_once()
