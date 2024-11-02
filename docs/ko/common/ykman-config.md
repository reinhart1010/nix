---
layout: page
title: common/ykman-config (한국어)
description: "YubiKey 애플리케이션 활성화 또는 비활성화."
content_hash: b16094bbb59f1cbaae63fc006211bd9d35ce17e5
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/ykman-config.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ykman-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykman config

YubiKey 애플리케이션 활성화 또는 비활성화.
참고: 현재 활성화된 애플리케이션을 보려면 `ykman info`를 사용할 수 있습니다.
더 많은 정보: <https://docs.yubico.com/software/yubikey/tools/ykman/Base_Commands.html#ykman-config-options-command-args>.

- USB 또는 NFC를 통해 애플리케이션 활성화 (`--enable`을 여러 번 사용하여 더 많은 애플리케이션을 지정할 수 있음):

`ykman config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usb|nfc</span>` --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">otp|u2f|fido2|oath|piv|openpgp|hsmauth</span>

- USB 또는 NFC를 통해 애플리케이션 비활성화 (`--disable`을 여러 번 사용하여 더 많은 애플리케이션을 지정할 수 있음):

`ykman config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usb|nfc</span>` --disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">otp|u2f|fido2|oath|piv|openpgp|hsmauth</span>

- NFC를 통해 모든 애플리케이션 비활성화:

`ykman config nfc --disable-all`
