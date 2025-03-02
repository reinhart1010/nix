---
layout: page
title: common/paste (中文)
description: "合并文件行。"
content_hash: f2b5db06462b90a5821e3711335890dc10190f78
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/paste.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/paste.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/paste.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paste

合并文件行。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/paste-invocation.html>.

- 将所有行合并为一行，使用 tab 作为分隔符：

`paste -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 使用指定的分隔符将所有行合并为一行：

`paste -s -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分隔符</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 并排合并两个文件，每个文件以 tab 分隔为单独的列：

`paste `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件2</span>

- 并排合并两个文件，每个文件以指定的分隔符分隔为单独的列：

`paste -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分隔符</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件2</span>

- 将两个文件中的所有行，交替合并：

`paste -d '\n' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件2</span>
