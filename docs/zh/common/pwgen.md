---
layout: page
title: common/pwgen (中文)
description: "生成可拼写发音的密码。"
content_hash: c3524505682b021b57fee926086276172d95cb41
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pwgen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pwgen

生成可拼写发音的密码。
更多信息：<https://github.com/tytso/pwgen>.

- 生成指定长度的随机密码：

`pwgen -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">长度</span>

- 生成安全、难以记忆的密码：

`pwgen -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">长度</span>

- 生成至少包含一个大写字母的密码：

`pwgen -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">长度</span>
