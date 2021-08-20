# Google Authenticator Export Helper

## Protocol Buffers

A reconstructed definition of the protobuf file is [included in the repo](OtpMigration.proto).

## Bash example

With some regular bash tools and [protoc](https://developers.google.com/protocol-buffers/docs/downloads) you can extract the data like this:

```
$ function urldecode() { : "${*//+/ }"; echo -e "${_//%/\\x}"; }
$ urldecode '<DATA VALUE>' | base64 -d | protoc --decode_raw

1 {
  1: "\r\037)\335\260l\377\216=\0352O+\352\221.o\177\014e\030\217\352NM~V\322\322 \320\351@\314C"
  2: "Demo Issuer:Demo Account"
  4: 1
  5: 1
  6: 2
}
2: 1
3: 1
4: 0
5: 1045125660
```

Note however that this is just raw decoding the protoc buffer and will show field IDs without assigning names. You'll have to lookup the meaning of each field in the [Format description](#format-description).

Alternatively use the provided OtpMigration.proto and instruct `protoc` to decode a `MigrationPayload`:
```
$ urldecode '<DATA VALUE>' | base64 -d | protoc --decode=MigrationPayload OtpMigration.proto

otp_parameters {
  secret: "\r\037)\335\260l\377\216=\0352O+\352\221.o\177\014e\030\217\352NM~V\322\322 \320\351@\314C"
  name: "Demo Issuer:Demo Account"
  algorithm: SHA1
  digits: SIX
  type: TOTP
}
version: 1
batch_size: 1
batch_index: 0
batch_id: 1045125660

```
