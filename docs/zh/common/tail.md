---
layout: page
title: common/tail (中文)
description: "显示文件的最后一部分。"
content_hash: a72872690dfcab1a72bf1f46e5496cd1b35d0399
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/tail.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tail.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tail.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tail.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tail.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tail.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tail

显示文件的最后一部分。
另请参阅：`head`。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- 显示文件中最后 n 行：

`tail --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 从特定行号开始打印文件后续内容：

`tail --lines +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">行号</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 从给定文件末尾打印特定字节数量的内容：

`tail --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字节数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 打印给定文件的最后几行并保持读取直到 “Ctrl + C”：

`tail --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 保持读取文件直到 “Ctrl + C”，即使文件无法访问：

`tail --retry --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 显示文件中最后 n 行并每 t 秒刷新一次：

`tail --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` --sleep-interval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">t</span>` --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
