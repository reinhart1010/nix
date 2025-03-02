---
layout: page
title: common/jwt (中文)
description: "使用 JSON Web Tokens (JWTs) 进行操作。"
content_hash: d93a084b22a264a68d7bad1b296e904228752dec
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jwt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jwt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/jwt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jwt

使用 JSON Web Tokens (JWTs) 进行操作。
可用的加密算法包括 HS256、HS384、HS512、RS256、RS384、RS512、ES256、ES384。
更多信息：<https://github.com/mike-engel/jwt-cli>.

- 解码一个 JWT：

`jwt decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jwt字符串</span>

- 将 JWT 解码为 JSON 字符串：

`jwt decode -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jwt字符串</span>

- 将 JSON 字符串编码为 JWT：

`jwt encode --alg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HS256</span>` --secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234567890</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json字符串</span>`'`

- 将键值对载荷编码为 JWT：

`jwt encode --alg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HS256</span>` --secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234567890</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键=值</span>
