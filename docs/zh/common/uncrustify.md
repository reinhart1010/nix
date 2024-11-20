---
layout: page
title: common/uncrustify (中文)
description: "C、C++、C#、D、Java 和 Pawn 源代码格式化工具。"
content_hash: 72503c9ae5776d5065b3742dafc4c3f2beceb04c
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/uncrustify.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/uncrustify.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uncrustify

C、C++、C#、D、Java 和 Pawn 源代码格式化工具。
更多信息：<https://github.com/uncrustify/uncrustify>.

- 格式化单个文件：

`uncrustify -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.cpp</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出文件.cpp</span>

- 从 `stdin` 读取文件名，在写回原始文件路径之前创建备份：

`find . -name "*.cpp" | uncrustify -F - --replace`

- 不进行备份（适用于文件已在版本控制下的情况）：

`find . -name "*.cpp" | uncrustify -F - --no-backup`

- 使用自定义配置文件并将结果写入 `stdout`：

`uncrustify -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/uncrustify.cfg</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.cpp</span>

- 显式设置配置变量的值：

`uncrustify --set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">选项</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>

- 生成新的配置文件：

`uncrustify --update-config -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/新配置文件.cfg</span>
