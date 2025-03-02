---
layout: page
title: common/yazi (中文)
description: "用 Rust 编写的极速终端文件管理器。"
content_hash: d7511a1755338ae88ae5e9147aa7ddc695210698
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yazi.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/yazi.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yazi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yazi

用 Rust 编写的极速终端文件管理器。
提供高效、用户友好且可定制的文件管理体验。
更多信息：<https://github.com/sxyazi/yazi>.

- 从当前目录启动 Yazi：

`yazi`

- 打印调试信息：

`yazi --debug`

- 在退出时将当前工作目录写入文件：

`yazi --cwd-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/cwd_文件</span>

- 清除缓存目录：

`yazi --clear-cache`
