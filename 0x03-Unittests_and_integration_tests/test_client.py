#!/usr/bin/env python3
"""Module for testing the functions in the client file"""
import unittest
from typing import Dict
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, MagicMock, PropertyMock, Mock
from fixtures import TEST_PAYLOAD
from requests import HTTPError


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

    @patch("client.get_json")
    def test_public_repos(self, mockget_json: MagicMock) -> None:
        """Test the public_repos method of the GithubOrgClient class"""
        mockResp = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mockget_json.return_value = mockResp["repos"]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mockReposUrl:
            mockReposUrl.return_value = mockResp["repos_url"]
            self.assertEqual(GithubOrgClient("google").public_repos(),
                             ["episodes.dart", "kratu"])
            mockReposUrl.assert_called_once()
        mockget_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False)
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Test the has_license method of the GithubOrgClient class"""
        clientInst = GithubOrgClient("google")
        has_licenseResult = clientInst.has_license(repo, key)
        self.assertEqual(has_licenseResult, expected)

    @parameterized_class([
        {
            "org_payload": TEST_PAYLOAD[0][0],
            "repos_payload": TEST_PAYLOAD[0][1],
            "expected_repos": TEST_PAYLOAD[0][2],
            "apache2_repos": TEST_PAYLOAD[0][3]
        }
    ])
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """Integration tests for GithubOrgClient class/function"""
        @classmethod
        def setUpClass(cls) -> None:
            """SetsUp class-level fixtures before running tests"""
            mockRoutes = {
                "https://api.github.com/orgs/google": cls.org_payload,
                "https://api.github.com/orgs/google/repos": cls.repos_payload
            }

            def mock_response(url):
                """Gets and returns a mock response for a given url request"""
                if url in mockRoutes:
                    return Mock(**{"json.return_value": mockRoutes[url]})
                return HTTPError
            cls.get_patcher = patch("requests.get", side_effect=mock_response)
            cls.get_patcher.start()

        @classmethod
        def tearDownClass(cls) -> None:
            """Deletes the class-level fixtures after running all tests"""
            cls.get_patcher.stop()

        def test_public_repos(self) -> None:
            """Test the public_repos method of the GithubOrgClient class"""
            self.assertEqual(GithubOrgClient("google").public_repos(),
                             self.expected_repos)

        def test_public_repos_with_license(self) -> None:
            """Test the public_repos_with_license method of the class"""
            self.assertEqual(
                GithubOrgClient("google").public_repos(license="apache-2.0"),
                self.apache2_repos)
