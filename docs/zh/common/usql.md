---
layout: page
title: common/usql (中文)
description: "通用 SQL 数据库的命令行界面。"
content_hash: be29eeab8c1205d37d84d9fd230a918f4628973d
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/usql.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/usql.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/usql.html
    icon: bi bi-globe
tldri18n_status: 2
---
# usql

通用 SQL 数据库的命令行界面。
更多信息：<https://github.com/xo/usql>.

- 连接到一个特定的数据库：

`usql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sqlserver|mysql|postgres|sqlite3|...</span>`://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">端口</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数据库名</span>

- 从文件中执行命令：

`usql --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.sql</span>

- 执行一个特定的 SQL 命令：

`usql --command="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sql命令</span>`"`

- 在 `usql` 提示符下运行一个 SQL 命令：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`=> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sql命令</span>

- 显示数据库架构：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`=> \d`

- 将查询结果导出到一个特定文件：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`=> \g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/结果文件</span>

- 从 CSV 文件导入数据到一个特定表：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`=> \copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/data.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">表名</span>
