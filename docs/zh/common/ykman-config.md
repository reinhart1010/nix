---
layout: page
title: common/ykman-config (中文)
description: "启用或禁用 YubiKey 应用程序。"
content_hash: 6ef70796db2a4b49254d237a1b19cb3be68c4501
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/ykman-config.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ykman-config.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ykman-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykman config

启用或禁用 YubiKey 应用程序。
注意：您可以使用 `ykman info` 查看当前已启用的应用程序。
更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/Base_Commands.html#ykman-config-options-command-args>.

- 通过 USB 或 NFC 启用某个应用程序（`--enable` 可以多次使用以指定更多应用程序）：

`ykman config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usb|nfc</span>` --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">otp|u2f|fido2|oath|piv|openpgp|hsmauth</span>

- 通过 USB 或 NFC 禁用某个应用程序（`--disable` 可以多次使用以指定更多应用程序）：

`ykman config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usb|nfc</span>` --disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">otp|u2f|fido2|oath|piv|openpgp|hsmauth</span>

- 禁用 NFC 上的所有应用程序：

`ykman config nfc --disable-all`
