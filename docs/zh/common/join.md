---
layout: page
title: common/join (中文)
description: "在两个已排序的文件中根据一个公共字段合并行。"
content_hash: 0126a52478fb9f8f3fcf2a633968bdd1c01e6eff
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/join.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/join.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/join.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/join.html
    icon: bi bi-globe
tldri18n_status: 2
---
# join

在两个已排序的文件中根据一个公共字段合并行。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/join-invocation.html>.

- 根据第一个（默认）字段合并两个文件：

`join `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件2</span>

- 使用逗号（而不是空格）作为字段分隔符合并两个文件：

`join -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">','</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件2</span>

- 将文件1的字段3与文件2的字段1合并：

`join -1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件2</span>

- 为文件1中的每行未配对的行生成一行：

`join -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件2</span>

- 从 `stdin` 合并一个文件：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1</span>` | join - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件2</span>
