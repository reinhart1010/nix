---
layout: page
title: common/ykman (中文)
description: "YubiKey 管理器 - 配置 YubiKey。"
content_hash: a38bb80657984cb99adc5984ef19a52660275a4f
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/ykman.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ykman.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ykman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykman

YubiKey 管理器 - 配置 YubiKey。
如果连接了多个 YubiKey，您必须在子命令之前添加 `--device serial_number`。
更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/index.html>.

- 显示 YubiKey 的一般信息（序列号、固件版本、功能等）：

`ykman info`

- 列出已连接 YubiKey 的简短单行描述（包括序列号）：

`ykman list`

- 查看关于启用和禁用应用程序的文档：

`tldr ykman config`

- 查看关于管理 FIDO 应用程序的文档：

`tldr ykman fido`

- 查看关于管理 OATH 应用程序的文档：

`tldr ykman oath`

- 查看关于管理 OpenPGP 应用程序的文档：

`tldr ykman openpgp`
