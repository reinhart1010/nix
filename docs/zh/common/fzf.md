---
layout: page
title: common/fzf (中文)
description: "命令行模糊查找器。"
content_hash: b2736961a0439309998a5a6371f0ef918ae06c00
last_modified_at: 2024-11-28
related_topics:
  - title: English version
    url: /en/common/fzf.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/fzf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fzf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/fzf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fzf

命令行模糊查找器。
类似于 `sk`.
更多信息：<https://github.com/junegunn/fzf>.

- 对指定目录中的所有文件启动 `fzf`:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>` -type f | fzf`

- 为正在运行的进程启动 `fzf`:

`ps aux | fzf`

- 使用 `Shift + Tab` 选择多个文件并将结果写入文件：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>` -type f | fzf --multi > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 使用指定查询词启动 `fzf`:

`fzf --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查询词</span>`"`

- 对以 core 开头、以 go, rb 或 py 结尾的条目启动 `fzf`:

`fzf --query "^core go$ | rb$ | py$"`

- 对不匹配 pyc 且完全匹配 travis 的条目启动 `fzf`:

`fzf --query "!pyc 'travis"`
