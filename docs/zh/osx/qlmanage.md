---
layout: page
title: osx/qlmanage (中文)
description: "QuickLook 服务器工具。"
content_hash: d6c19c0dc7aac11f4d11c824924dc6970ca89de8
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/qlmanage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qlmanage

QuickLook 服务器工具。
更多信息：<https://keith.github.io/xcode-man-pages/qlmanage.1.html>.

- 快速显示一个或多个文件：

`qlmanage -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1 路径/到/文件2 ...</span>

- 计算生成当前目录中所有 jpeg 文件的缩略图，300px 宽 png 格式，并将它们放在一个指定目录中：

`qlmanage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` -t -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定目录</span>

- 重置快速查看：

`qlmanage -r`
