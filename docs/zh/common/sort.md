---
layout: page
title: common/sort (中文)
description: "对文本文件的行进行排序。"
content_hash: a9b635cf619c83ab3a94799306951f1766b08d80
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/sort.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sort

对文本文件的行进行排序。
更多信息：<https://www.gnu.org/software/coreutils/sort>.

- 以升序对文件进行排序：

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 以降序对文件进行排序：

`sort --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 以不区分大小写的方式对文件进行排序：

`sort --ignore-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 用数字而不是字母顺序对文件进行排序：

`sort --numeric-sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 按每行的第 3 个字段对 `/etc/passwd` 进行数字排序，使用 “:” 作为字段分隔符：

`sort --field-separator=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>` --key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/passwd</span>

- 对一个文件进行排序，只保留唯一的行：

`sort --unique `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 对一个文件进行排序，将输出结果打印到指定的输出文件中（可以用来对一个文件进行原地排序）：

`sort --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 对带有指数的数字进行排序：

`sort --general-numeric-sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
