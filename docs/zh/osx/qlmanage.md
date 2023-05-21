---
layout: page
title: osx/qlmanage (中文)
description: "QuickLook 服务器工具。"
content_hash: 2ac5e477e60a8c74f0d91a2602e75638e2e5e54b
last_modified_at: 2023-05-21
related_topics:
  - title: English version
    url: /en/osx/qlmanage.html
    icon: bi bi-globe
---
# qlmanage

QuickLook 服务器工具。
更多信息：<https://ss64.com/osx/qlmanage.html>.

- 快速显示一个或多个文件：

`qlmanage -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1个 路径/到/文件2个 ...</span>

- 计算生成当前目录中所有 jpeg 文件的缩略图，300px 宽 png 格式，并将它们放在一个指定目录中：

`qlmanage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` -t -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定目录</span>

- 重置快速查看：

`qlmanage -r`
