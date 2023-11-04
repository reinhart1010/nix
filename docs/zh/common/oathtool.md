---
layout: page
title: common/oathtool (中文)
description: "OATH 一次性密码工具。"
content_hash: 337f549b57a5f75a69eafc73c14b562e68a3199f
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/common/oathtool.html
    icon: bi bi-globe
---
# oathtool

OATH 一次性密码工具。

- 生成 TOTP 令牌（行为类似于 Google Authenticator）：

`oathtool --totp --base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 根据给定时间产生特定的 TOTP 令牌：

`oathtool --totp --now `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2004-02-29 16:21:42</span>` --base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 验证 TOTP 令牌：

`oathtool --totp --base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">令牌</span>
