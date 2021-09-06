# Google Authenticator Export Helper

Based on the efforts by [Chris van Marle](https://github.com/qistoph/otp_export).

## Setup

After cloning the repository, you can create a virtual environment, build and install the library via:
```bash
make prepare install-wheel
```

## Usage

```python
import gaeh

url = 'otpauth-migration://offline?data=CjMKFDFENjc5QzE3RTkzRTJFRTAyMkZBEgl0ZXNzZXJhY3QaCm11bHRpdmVyc2UgASgBMAIQARgBIAA%3D'
accounts = gaeh.export_otp_accounts(url)

print(accounts)
```
Example result:
```python
{'version': 1, 'batch_size': 1, 'batch_index': 0, 'batch_id': 0, 'accounts': [{'key': 'GFCDMNZZIMYTORJZGNCTERKFGAZDERSB', 'name': 'tesseract', 'issuer': 'multiverse', 'algorithm': 'SHA1', 'digits': 'SIX', 'type': 'TOTP', 'counter': 0}]}
```

## References

Checkout [gabut](https://github.com/think-biq/gabut) for a comprehensive cli tool for managing google authentictor backups using gaeh.