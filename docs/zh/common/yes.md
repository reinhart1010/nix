---
layout: page
title: common/yes (中文)
description: "重复输出某些内容。"
content_hash: d24f5550167b394513572816155ef6dc506ddc9c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yes.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/yes.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/yes.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yes.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/yes.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/yes.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/yes.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/yes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yes

重复输出某些内容。
此命令通常用于对安装命令（如 apt-get）每个提示回答是。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html>.

- 重复输出“`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">消息</span>`”：

`yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">消息</span>

- 重复输出“y”：

`yes`

- 接受 `apt-get` 命令的所有提示：

`yes | sudo apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">程序</span>

- 重复输出一个换行符以始终接受提示的默认选项：

`yes ''`
