---
layout: page
title: common/ykinfo (中文)
description: "从 YubiKey 获取基本信息。"
content_hash: 846f7898359f01ea6ebd425fe8c9e2ae1340b252
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/ykinfo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ykinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykinfo

从 YubiKey 获取基本信息。
更多信息：<https://developers.yubico.com/yubikey-personalization/Manuals/ykinfo.1.html>.

- 显示 YubiKey 的所有信息：

`ykinfo -a`

- 仅获取 YubiKey 的十进制序列号：

`ykinfo -s -q`

- 获取 YubiKey 的功能：

`ykinfo -c`
