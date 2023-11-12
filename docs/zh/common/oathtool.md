---
layout: page
title: common/oathtool (中文)
description: "OATH 一次性密码工具。"
content_hash: 23cc6c934a04e8688aed3778185aede0dd3905d4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/oathtool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# oathtool

OATH 一次性密码工具。
更多信息：<https://www.nongnu.org/oath-toolkit/oathtool.1.html>.

- 生成 TOTP 令牌（行为类似于 Google Authenticator）：

`oathtool --totp --base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 根据给定时间产生特定的 TOTP 令牌：

`oathtool --totp --now `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2004-02-29 16:21:42</span>` --base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 验证 TOTP 令牌：

`oathtool --totp --base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">令牌</span>
