---
layout: page
title: osx/qlmanage (中文)
description: "QuickLook 服务器工具。"
content_hash: 181bb364b12a7a9158dbb311915d02e601950048
related_topics:
  - title: English version
    url: /en/osx/qlmanage.html
    icon: bi bi-globe
---
# qlmanage

QuickLook 服务器工具。

- 快速显示一个或多个文件：

`qlmanage -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名 2</span>

- 计算生成当前目录中所有 jpeg 文件的缩略图，300px 宽 png 格式，并将它们放在一个指定目录中：

`qlmanage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` -t -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定目录</span>

- 重置快速查看：

`qlmanage -r`
