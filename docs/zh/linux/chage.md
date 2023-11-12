---
layout: page
title: linux/chage (中文)
description: "更改用户账户和密码到期信息。"
content_hash: a743e0702f5576ed590e10d26515518ab0b7eb71
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/chage.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/chage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chage

更改用户账户和密码到期信息。
更多信息：<https://manned.org/chage>.

- 列出用户的密码信息：

`chage --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>

- 启用密码在 10 天内过期：

`sudo chage --maxdays `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>

- 关闭密码过期：

`sudo chage --maxdays `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>

- 设置账户到期日期：

`sudo chage --expiredate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>

- 强制用户在下次登录时更改密码：

`sudo chage --lastday `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>
