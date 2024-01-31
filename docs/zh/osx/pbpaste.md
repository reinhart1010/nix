---
layout: page
title: osx/pbpaste (中文)
description: "将剪贴板的内容发送到标准输出。"
content_hash: b5e696aca9557301507d178c5ff16b37ceea972b
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/osx/pbpaste.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/pbpaste.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/pbpaste.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/pbpaste.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/osx/pbpaste.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbpaste

将剪贴板的内容发送到标准输出。
相当于在键盘上按下 Cmd + V.
更多信息：<https://keith.github.io/xcode-man-pages/pbpaste.1.html>.

- 将剪贴板的内容写入文件：

`pbpaste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 将剪贴板的内容用作命令的输入：

`pbpaste | grep foo`
