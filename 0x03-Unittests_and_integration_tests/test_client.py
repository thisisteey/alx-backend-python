#!/usr/bin/env python3
"""Module for testing the functions in the client file"""
import unittest
from typing import Dict
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, MagicMock, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Unittest for GithubOrgClient class/function"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, mockResp: Dict, mockGet: MagicMock) -> None:
        """Test the org method of the GithubOrgClient class"""
        mockGet.return_value = MagicMock(return_value=mockResp)
        clientInst = GithubOrgClient(org)
        self.assertEqual(clientInst.org(), mockResp)
        mockGet.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self) -> None:
        """Test the public_repos_url method of the GithubOrgClient class"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mockProp:
            mockProp.return_value = {
                    'repos_url': "https://api.github.com/users/google/repos"
            }
            self.assertEqual(GithubOrgClient("google")._public_repos_url,
                             "https://api.github.com/users/google/repos")
