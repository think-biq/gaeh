#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''   
    Utility to export google authenticator accounts.

    2021-∞ (c) blurryroots innovation qanat OÜ. All rights reserved.
    See license.md for details.

    https://think-biq.com
'''

__all__ = ['MigrationPayload', 'Algorithm', 'DigitCount', 'OtpType', 'DigitCount']


from .OtpMigration_pb2 import \
    MigrationPayload, \
    Algorithm, \
    DigitCount, \
    OtpType, \
    DigitCount
from urllib.parse import urlparse, parse_qs
import sys
import base64


def extract_payload_from_url(google_authenticator_export_url):
    url = urlparse(google_authenticator_export_url)

    if url.scheme != 'otpauth-migration':
        raise Exception('Only otpauth-migration URLs can be parsed!')

    qs = parse_qs(url.query)

    if 'data' not in qs:
        raise Exception('Missing `data` field in query string!')

    if 0 == len(qs['data']):
        raise Exception('No entry in data field!')

    data = base64.b64decode(qs['data'][0])
    payload = MigrationPayload.FromString(data)