---
layout: page
title: common/ykman-fido (中文)
description: "管理 YubiKey FIDO 应用程序。"
content_hash: e3eaedb99721d2832a6a872c0777f397f68b0a60
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/ykman-fido.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ykman-fido.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ykman-fido.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykman fido

管理 YubiKey FIDO 应用程序。
更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/FIDO_Commands.html>.

- 显示 FIDO2 应用程序的一般信息：

`ykman fido info`

- 更改 FIDO 密码：

`ykman fido access change-pin`

- 列出存储在 YubiKey 上的常驻凭证：

`ykman fido credentials list`

- 从 YubiKey 中删除一个常驻凭证：

`ykman fido credentials delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID</span>

- 列出存储在 YubiKey 上的指纹（需要带有指纹传感器的密钥）：

`ykman fido fingerprints list`

- 向 YubiKey 添加一个新指纹：

`ykman fido fingerprints add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 从 YubiKey 删除一个指纹：

`ykman fido fingerprints delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 清除所有 FIDO 凭证（在超过密码重试次数之后需要执行此操作）：

`ykman fido reset`
