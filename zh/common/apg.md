---
layout: page
title: common/apg (中文)
description: "生成任意复杂度的随机密码。"
content_hash: c167356d2777d9f1d86fb4a847f0c0e3843a72c7
related_topics:
  - title: English version
    url: /en/common/apg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/apg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/apg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/apg.html
    icon: bi bi-globe
---
# apg

生成任意复杂度的随机密码。
更多信息：<https://manned.org/apg>.

- 生成随机密码（默认密码长度为 8 位）：

`apg`

- 生成密码，包含至少 1 个符号 (S), 1 个数字 (N), 1 个大写字母 (C), 1 个小写字母 (L)：

`apg -M SNCL`

- 生成 16 个字符的密码：

`apg -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- 生成最大长度为 16 位的密码：

`apg -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- 生成未出现在字典中的密码（必须提供字典文件）：

`apg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字典文件</span>
