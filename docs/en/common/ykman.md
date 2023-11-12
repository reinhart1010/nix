---
layout: page
title: common/ykman (English)
description: "The YubiKey Manager can be used to configure all aspects of the YubiKey."
content_hash: fca1cf4ca33b4e044706188472c0117798e945b3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ykman

The YubiKey Manager can be used to configure all aspects of the YubiKey.
More information: <https://docs.yubico.com/software/yubikey/tools/ykman/index.html>.

- Get information from YubiKey:

`ykman info`

- Get information for a given application from YubiKey:

`ykman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fido|oath|openpgp|otp|piv</span>` info`

- Get a list of enabled applications over NFC from YubiKey:

`ykman config nfc --list`

- Enable application over USB on YubiKey:

`ykman config usb --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">OTP|U2F|FIDO2|OATH|PIV|OPENPGP|HSMAUTH</span>
