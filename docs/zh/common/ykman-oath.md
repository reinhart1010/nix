---
layout: page
title: common/ykman-oath (中文)
description: "管理 OATH YubiKey 应用程序。"
content_hash: cf3a3afe02e7728b1e73e56c12008b1fd06e92a0
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/ykman-oath.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ykman-oath.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ykman-oath.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykman oath

管理 OATH YubiKey 应用程序。
`关键词` 可以是名称或发行者的一部分。
更多信息：<https://docs.yubico.com/software/yubikey/tools/ykman/OATH_Commands.html>.

- 显示有关 OATH 应用程序的一般信息：

`ykman oath info`

- 更改用于保护 OATH 账户的密码（添加 `--clear` 以移除密码）：

`ykman oath access change`

- 添加一个新账户（`--issuer` 是可选的）：

`ykman oath accounts add --issuer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">发行者</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 列出所有账户（及其发行者）：

`ykman oath accounts list`

- 列出所有账户及其当前的 TOTP/HOTP 代码（可通过关键词过滤列表）：

`ykman oath accounts code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键词</span>

- 重命名一个账户：

`ykman oath accounts rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键词</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">发行者:名称|名称</span>

- 删除一个账户：

`ykman oath accounts delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键词</span>

- 删除所有账户并恢复出厂设置：

`ykman oath reset`
