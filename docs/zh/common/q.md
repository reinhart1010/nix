---
layout: page
title: common/q (中文)
description: "在 CSV 和 TSV 文件上执行类似 SQL 的查询。"
content_hash: 3e5e5339529a27bce3b0a6fe4e5283d03c6b193e
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/q.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/q.html
    icon: bi bi-globe
tldri18n_status: 2
---
# q

在 CSV 和 TSV 文件上执行类似 SQL 的查询。
更多信息：<https://harelba.github.io/q>.

- 指定分隔符为 ',' 来查询 CSV 文件：

`q -d',' "SELECT * from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>`"`

- 查询 TSV 文件：

`q -t "SELECT * from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>`"`

- 查询带有表头行的文件：

`q -d`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分隔符</span>` -H "SELECT * from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>`"`

- 从 `stdin` 读取数据；查询中的 '-' 代表来自 `stdin` 的数据：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输出</span>` | q "select * from -"`

- 在列 `c1` 上连接两个文件（在例子中别名为 `f1` 和 `f2`）：

`q "SELECT * FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1</span>` f1 JOIN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件2</span>` f2 ON (f1.c1 = f2.c1)"`

- 使用包含输出标题行的输出分隔符来格式化输出（注意：命令将根据输入文件标题或在查询中覆盖的列别名输出列名）：

`q -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分隔符</span>` -O "SELECT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">列</span>` as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">别名</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>`"`
