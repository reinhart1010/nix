---
layout: page
title: common/carbon-now (中文)
description: "创建漂亮的代码图片。"
content_hash: 33bd7b8c37b88b1ccf709c0f8c196a7363d1c9b8
related_topics:
  - title: English version
    url: /en/common/carbon-now.html
    icon: bi bi-globe
---
# carbon-now

创建漂亮的代码图片。
更多信息：<https://github.com/mixn/carbon-now-cli>.

- 使用默认设置从文件创建图片：

`carbon-now `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 使用默认设置从剪贴板创建图片：

`carbon-now --from-clipboard`

- 使用默认设置从标准输入创建图片：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输入</span>` | carbon-now`

- 以交互方式创建图片以进行自定义设置，还可以选择保存预设：

`carbon-now -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 从先前保存的预设创建图片：

`carbon-now -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">预设</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 从指定的文本行开始：

`carbon-now -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">行号</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 结束于指定的文本行：

`carbon-now -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">行号</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 在浏览器中打开图片而不是保存：

`carbon-now --open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>
