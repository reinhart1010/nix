---
layout: page
title: linux/logsave (中文)
description: "将一个命令的输出保存在日志文件中。"
content_hash: 3113135ba8806cd4c0592a4f03503c0027f6eee5
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/logsave.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/logsave.html
    icon: bi bi-globe
tldri18n_status: 2
---
# logsave

将一个命令的输出保存在日志文件中。
更多信息：<https://manned.org/logsave>.

- 使用指定的参数执行命令并将其输出保存到日志文件中：

`logsave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/logfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- 从标准输入中获取输入并将其保存在日志文件中：

`logsave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logfile</span>` -`

- 将输出追加到日志文件，而不是替换其当前内容：

`logsave -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- 显示详细输出：

`logsave -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
