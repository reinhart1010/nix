---
layout: page
title: common/ykman-config (English)
description: "Enable or disable YubiKey applications."
content_hash: 58230d6dbe3d8d4dfd764e9e9c4d920d3b653ec8
last_modified_at: 2023-12-08
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ykman-config.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ykman config

Enable or disable YubiKey applications.
Note: you can use `ykman info` to see currently enabled applications.
More information: <https://docs.yubico.com/software/yubikey/tools/ykman/Base_Commands.html#ykman-config-options-command-args>.

- Enable an application over USB or NFC (`--enable` can be used multiple times to specify more applications):

`ykman config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usb|nfc</span>` --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">otp|u2f|fido2|oath|piv|openpgp|hsmauth</span>

- Disable an application over USB or NFC (`--disable` can be used multiple times to specify more applications):

`ykman config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usb|nfc</span>` --disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">otp|u2f|fido2|oath|piv|openpgp|hsmauth</span>

- Disable all applications over NFC:

`ykman config nfc --disable-all`
