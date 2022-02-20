---
layout: page
title: linux/asciiart (中文)
description: "将图像转换为 ASCII."
content_hash: 240615f16c0030fa28c3d9b218f59448800f264d
related_topics:
  - title: Deutsch version
    url: /de/linux/asciiart.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/asciiart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/asciiart.html
    icon: bi bi-globe
---
# asciiart

将图像转换为 ASCII.
更多信息：<https://github.com/nodanaonlyzuul/asciiart>.

- 从文件中读取图像并以 ASCII 打印：

`asciiart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/图片.jpg</span>

- 从 URL 中读取图像并以 ASCII 打印：

`asciiart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com/image.jpg</span>

- 选择输出宽度（默认为 100）：

`asciiart -width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/图片.jpg</span>

- 对 ASCII 输出进行着色：

`asciiart --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/图片.jpg</span>

- 选择输出格式（默认格式为文本）：

`asciiart --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text|html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/图片.jpg</span>

- 反转字符映射：

`asciiart --invert-chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/图片.jpg</span>
