---
layout: page
title: common/ykman-config (Nederlands)
description: "In- of uitschakelen van YubiKey applicaties."
content_hash: 4f4fb5e6c87a483a6e8c3600c1fe53db8d2055e7
last_modified_at: 2023-12-11
related_topics:
  - title: English version
    url: /en/common/ykman-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykman config

In- of uitschakelen van YubiKey applicaties.
Opmerking: je kan `ykman info` gebruiken om de huidige ingeschakelde applicaties te zien.
Meer informatie: <https://docs.yubico.com/software/yubikey/tools/ykman/Base_Commands.html#ykman-config-options-command-args>.

- Schakel een applicatie in via USB of NFC (`--enable` kan meerdere keren gebruikt worden om meerdere applicaties te specificeren):

`ykman config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usb|nfc</span>` --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">otp|u2f|fido2|oath|piv|openpgp|hsmauth</span>

- Schakel een applicatie uit via USB of NFC (`--disable` kan meerdere keren gebruikt worden om meerdere applicaties te specificeren):

`ykman config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usb|nfc</span>` --disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">otp|u2f|fido2|oath|piv|openpgp|hsmauth</span>

- Schakel alle applicaties uit via NFC:

`ykman config nfc --disable-all`
