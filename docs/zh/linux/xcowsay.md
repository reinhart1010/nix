---
layout: page
title: linux/xcowsay (中文)
description: "在您的 Linux 桌面上显示一头可爱的牛和指定的消息。"
content_hash: 6a2f064422c288c1f0ccb410abc666b685e1a027
related_topics:
  - title: English version
    url: /en/linux/xcowsay.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xcowsay

在您的 Linux 桌面上显示一头可爱的牛和指定的消息。
牛的显示时间是固定的或则是根据文本大小计算得出的。 点击牛即马上关闭。
更多信息： <https://www.doof.me.uk/xcowsay/>.

- 显示一头说 “hello, world” 的牛：

`xcowsay "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello, world</span>`"`

- 显示一头牛和消息，该消息是另一个命令的输出：

`ls | xcowsay`

- 显示一头有指定 X 和 Y 坐标的牛：

`xcowsay --at=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Y</span>

- 显示一头不同大小的牛：

`xcowsay --cow-size=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">small|med|large</span>

- 显示思想泡泡而不是说话泡泡：

`xcowsay --think`

- 用指定的照片来代替默认的牛：

`xcowsay --image=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
