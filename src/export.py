#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''    
    Utility to export google authenticator accounts.

    2021-∞ (c) blurryroots innovation qanat OÜ. All rights reserved.
    See license.md for details.

    https://think-biq.com
'''

__all__ = ['extract_payload_from_url']


import base64
from .protobuf_migration import *


def export_otp_accounts(google_authenticator_export_url):
    payload = extract_payload_from_url(google_authenticator_export_url)
    
    export_data = {}    
    export_data['version'] = payload.version
    export_data['batch_size'] = payload.batch_size
    export_data['batch_index'] = payload.batch_index
    export_data['batch_id'] = payload.batch_id
    export_data['accounts'] = []
    for params in payload.otp_parameters:
        entry = {}
        entry['key'] = base64.b32encode(params.secret).encode('utf8')
        entry['name'] = params.name
        entry['issuer'] = params.issuer
        entry['algorithm'] = Algorithm.Name(params.algorithm)
        entry['digits'] = DigitCount.Name(params.digits)
        entry['type'] = OtpType.Name(params.type)
        entry['counter'] = params.counter
        export_data['accounts'].append(entry)

    return export_data