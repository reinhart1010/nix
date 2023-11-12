---
layout: page
title: linux/asterisk (中文)
description: "电话和交换（手机）服务器。"
content_hash: 363980bfd1d34903eef220651d1384f88745db53
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/asterisk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asterisk

电话和交换（手机）服务器。
用于管理服务器自身和管理已经在运行的实例。
更多信息：<https://wiki.asterisk.org/wiki/display/AST/Home>.

- 重新连接一个正在运行的服务器，并打开 3 级的日志详细度：

`asterisk -r -vvv`

- 重新连接一个正在运行的服务器，执行一个命令，然后返回：

`asterisk -r -x "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>`"`

- 显示 chan_SIP 客户端（手机）：

`asterisk -r -x "sip show peers"`

- 显示激活的通话和频道：

`asterisk -r -x "core show channels"`

- 显示语音邮箱：

`asterisk -r -x "voicemail show users"`

- 终止一个频道：

`asterisk -r -x "hangup request `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">频道 ID</span>`"`

- 重新载入 chan_SIP 设置：

`asterisk -r -x "sip reload"`
