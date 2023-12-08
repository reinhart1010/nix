---
layout: page
title: common/ykman (English)
description: "YubiKey Manager - configure YubiKeys."
content_hash: 52160a44bfd560a22d651e851877d927437ea48e
last_modified_at: 2023-12-08
tldri18n_status: 2
---
# ykman

YubiKey Manager - configure YubiKeys.
If there are multiple YubiKeys connected, you have to add `--device serial_number` before a subcommand.
More information: <https://docs.yubico.com/software/yubikey/tools/ykman/index.html>.

- Display general information about a YubiKey (serial number, firmware version, capabilities, etc.):

`ykman info`

- List connected YubiKeys with short, one-line descriptions (including the serial number):

`ykman list`

- View documentation for enabling and disabling applications:

`tldr ykman config`

- View documentation for managing the FIDO applications:

`tldr ykman fido`

- View documentation for managing the OATH application:

`tldr ykman oath`

- View documentation for managing the OpenPGP application:

`tldr ykman openpgp`
