---
layout: page
title: common/unar (中文)
description: "从归档文件中提取内容。"
content_hash: c4223f7e7ec00cd32c829ea677ee685c3a666946
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/unar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unar

从归档文件中提取内容。
更多信息：<https://manned.org/unar>.

- 提取一个归档文件到当前目录：

`unar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">归档文件</span>

- 提取一个归档文件到指定目录：

`unar -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">归档文件</span>

- 如果要提取的文件已经存在，则总是覆盖：

`unar -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">归档文件</span>

- 如果要提取的文件已经存在，则总是重命名：

`unar -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">归档文件</span>

- 如果要提取的文件已经存在，则总是跳过：

`unar -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">归档文件</span>
