---
layout: page
title: common/ykman-openpgp (中文)
description: "管理 OpenPGP YubiKey 应用程序。"
content_hash: 8d3a26648f23e970a1ada513ee12ebc70c7f2380
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/ykman-openpgp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ykman-openpgp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ykman-openpgp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykman openpgp

管理 OpenPGP YubiKey 应用程序。
注意：你需要使用 `gpg --card-edit` 来进行某些设置。
更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/OpenPGP_Commands.html>.

- 显示有关 OpenPGP 应用程序的一般信息：

`ykman openpgp info`

- 分别设置用户 PIN码、复位代码和管理 PIN码的重试次数：

`ykman openpgp access set-retries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- 更改用户 PIN码、复位代码或管理 PIN码：

`ykman openpgp access change-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pin|reset-code|admin-pin</span>

- 将 OpenPGP 应用程序恢复出厂设置（在超过管理 PIN码 重试次数后需要这样做）：

`ykman openpgp reset`
