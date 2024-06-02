---
layout: page
title: linux/sed (中文)
description: "以脚本方式编辑文本。"
content_hash: 2e5931cb109d23006638cbad571167ad178720f5
last_modified_at: 2024-06-02
related_topics:
  - title: English version
    url: /en/linux/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/sed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

以脚本方式编辑文本。
参见：`awk`, `ed`.
更多信息：<https://www.gnu.org/software/sed/manual/sed.html>.

- 将所有输入行中出现的 `apple`（基本正则语法）替换为 `mango`（基本正则语法），并将结果打印到 `stdout`：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` | sed 's/apple/mango/g'`

- 将所有输入行中出现的 `apple`（扩展正则语法）替换为 `APPLE` （扩展正则语法），并将结果打印到 `stdout`：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` | sed -E 's/(apple)/\U\1/g'`

- 用 `mango`（基本正则语法）替换特定文件中出现的所有 `apple`（基本正则语法），并覆盖原文件：

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 执行特定的脚本，并将结果打印到 `stdout`：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本.sed</span>

- 打印第一行到 `stdout`：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` | sed -n '1p'`

- 删除文件第一行：

`sed -i 1d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 插入新行到文件的第一行：

`sed -i '1i\your new line text\' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
