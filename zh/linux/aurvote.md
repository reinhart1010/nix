---
layout: page
title: linux/aurvote (中文)
description: "为 AUR 中的包投票。"
content_hash: baa210c7eeb28924d6eecfe15744740cef36d65c
related_topics:
  - title: English version
    url: /en/linux/aurvote.html
    icon: bi bi-globe
---
# aurvote

为 AUR 中的包投票。
为了投票成功，文件 `~/.config/aurvote` 必须存在并包含你的 AUR 身份凭证。
更多信息：<https://github.com/archlinuxfr/aurvote>.

- 交互式创建包含你的 AUR 用户名和密码的 `~/.config/aurvote` 文件：

`aurvote --configure`

- 为一个或多个 AUR 包投票：

`aurvote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- 为一个或多个 AUR 包取消投票：

`aurvote --unvote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- 检查一个或多个 AUR 包是否已投票：

`aurvote --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- 查看 `aurvote` 的帮助信息：

`aurvote --help`
