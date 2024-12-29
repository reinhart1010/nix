---
layout: page
title: common/mysql (中文)
description: "MySQL 命令行工具。"
content_hash: 750bea2b70888a14c90664e969446c49c7f15151
last_modified_at: 2024-12-29
related_topics:
  - title: English version
    url: /en/common/mysql.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mysql.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/mysql.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/mysql.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/mysql.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mysql.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/mysql.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mysql

MySQL 命令行工具。
更多信息：<https://www.mysql.com/>.

- 连接数据库：

`mysql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数据库名</span>

- 连接到数据库，系统将提示用户输入密码：

`mysql -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数据库名</span>

- 连接到另一台主机上的数据库：

`mysql -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数据库地址</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数据库名</span>

- 通过Unix套接字文件连接到数据库：

`mysql --socket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/socket.sock</span>

- 执行脚本文件中的SQL语句：

`mysql -e "source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">脚本.sql</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数据库名</span>

- 从`mysqldump`创建的备份文件中恢复单个数据库（系统将提示用户输入密码）：

`mysql --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数据库名</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/备份文件.sql</span>

- 从备份中恢复所有数据库（系统将提示用户输入密码）：

`mysql --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` --password < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/备份文件.sql</span>
