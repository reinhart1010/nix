---
layout: page
title: common/autoflake (中文)
description: "一个工具，用于检查 Python 代码中未被使用的引入和变量。"
content_hash: 3d83a7cf4510056125ab08c01d06f32dc29129da
related_topics:
  - title: English version
    url: /en/common/autoflake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autoflake.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/autoflake.html
    icon: bi bi-globe
---
# autoflake

一个工具，用于检查 Python 代码中未被使用的引入和变量。
更多信息：<https://github.com/myint/autoflake>.

- 移除指定文件中未使用的变量，并展示 diff:

`autoflake --remove-unused-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.py</span>

- 移除多个文件中未使用的引入，并展示 diffs:

`autoflake --remove-all-unused-imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件1.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件2.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件3.py</span>

- 移除未被使用的变量，并覆盖更新：

`autoflake --remove-unused-variables --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.py</span>

- 递归地移除指定文件夹下层所有文件中未使用的变量，并覆盖更新：

`autoflake --remove-unused-variables --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>
