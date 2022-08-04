---
layout: page
title: windows/takeown (中文)
description: "取得文件或目录的所有权。"
content_hash: d6c34f3921f472a522b98a3110589085abc87f52
related_topics:
  - title: English version
    url: /en/windows/takeown.html
    icon: bi bi-globe
---
# takeown

取得文件或目录的所有权。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/takeown>.

- 取得指定文件的所有权：

`takeown /f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/文件</span>

- 取得指定目录的所有权：

`takeown /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/目录</span>

- 取得指定目录和所有子目录的所有权：

`takeown /r /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/目录</span>

- 将所有权更改为管理员组，而不是当前用户：

`takeown /a /f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/文件</span>
