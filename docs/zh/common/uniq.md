---
layout: page
title: common/uniq (中文)
description: "输出输入或文件中的唯一行。"
content_hash: 36cf734ca0b7a56b6480cc0bd7040606661009a4
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/uniq.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/uniq.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/uniq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uniq

输出输入或文件中的唯一行。
因为它只检测相邻的重复行，所以需要先对它们进行排序。
更多信息：<https://www.gnu.org/software/coreutils/uniq>.

- 仅显示每行一次：

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` | uniq`

- 仅显示唯一的行：

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` | uniq -u`

- 仅显示重复的行：

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` | uniq -d`

- 显示每行的出现次数及其内容：

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` | uniq -c`

- 显示每行的出现次数，并按出现次数从高到低排序：

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` | uniq -c | sort -nr`
