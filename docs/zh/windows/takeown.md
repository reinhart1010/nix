---
layout: page
title: windows/takeown (中文)
description: "取得文件或目录的所有权。"
content_hash: d3615455b2ff2cdccc4400ce03e9ae6df2b1d070
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/takeown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# takeown

取得文件或目录的所有权。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/takeown>.

- 取得指定文件的所有权：

`takeown /f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/文件</span>

- 取得指定目录的所有权：

`takeown /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/目录</span>

- 取得指定目录和所有子目录的所有权：

`takeown /r /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/目录</span>

- 将所有权更改为管理员组，而不是当前用户：

`takeown /a /f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/文件</span>
