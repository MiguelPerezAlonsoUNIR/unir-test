import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(response.read().decode(), "4", "El resultado debe ser 4")

    def test_api_add_negative_numbers(self):
        url = f"{BASE_URL}/calc/add/-2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "0")

    def test_api_add_decimals(self):
        url = f"{BASE_URL}/calc/add/1.5/2.5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "4.0")

    def test_api_add_invalid_parameter(self):
        url = f"{BASE_URL}/calc/add/abc/2"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP 400")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_subtract(self):
        url = f"{BASE_URL}/calc/subtract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "2")

    def test_api_subtract_negative_result(self):
        url = f"{BASE_URL}/calc/subtract/2/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "-3")

    def test_api_subtract_with_zero(self):
        url = f"{BASE_URL}/calc/subtract/10/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "10")

    def test_api_subtract_invalid_parameter(self):
        url = f"{BASE_URL}/calc/subtract/5/xyz"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP 400")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "12")

    def test_api_multiply_by_zero(self):
        url = f"{BASE_URL}/calc/multiply/5/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "0")

    def test_api_multiply_negative_numbers(self):
        url = f"{BASE_URL}/calc/multiply/-2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "-6")

    def test_api_multiply_invalid_parameter(self):
        url = f"{BASE_URL}/calc/multiply/abc/4"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP 400")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "5.0")

    def test_api_divide_with_decimals(self):
        url = f"{BASE_URL}/calc/divide/7/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "3.5")

    def test_api_divide_negative_numbers(self):
        url = f"{BASE_URL}/calc/divide/-10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "-5.0")

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/5/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP 400")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_divide_invalid_parameter(self):
        url = f"{BASE_URL}/calc/divide/10/abc"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP 400")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "8")

    def test_api_power_zero_exponent(self):
        url = f"{BASE_URL}/calc/power/5/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "1")

    def test_api_power_negative_exponent(self):
        url = f"{BASE_URL}/calc/power/2/-1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "0.5")

    def test_api_power_invalid_parameter(self):
        url = f"{BASE_URL}/calc/power/abc/2"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP 400")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "2.0")

    def test_api_sqrt_perfect_square(self):
        url = f"{BASE_URL}/calc/sqrt/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "3.0")

    def test_api_sqrt_zero(self):
        url = f"{BASE_URL}/calc/sqrt/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "0.0")

    def test_api_sqrt_negative_number(self):
        url = f"{BASE_URL}/calc/sqrt/-4"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP 400")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_sqrt_invalid_parameter(self):
        url = f"{BASE_URL}/calc/sqrt/abc"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP 400")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "1.0")

    def test_api_log10_hundred(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "2.0")

    def test_api_log10_one(self):
        url = f"{BASE_URL}/calc/log10/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "0.0")

    def test_api_log10_zero(self):
        url = f"{BASE_URL}/calc/log10/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP 400")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_log10_negative_number(self):
        url = f"{BASE_URL}/calc/log10/-10"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP 400")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)

    def test_api_log10_invalid_parameter(self):
        url = f"{BASE_URL}/calc/log10/abc"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP 400")
        except HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
