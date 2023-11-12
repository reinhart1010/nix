---
layout: page
title: common/write (中文)
description: "向某个终端上的特定用户的屏幕写入信息（Ctrl-C 来停止写入）。"
content_hash: 5ba02778bbbf2a6397741ddc7c0a20740ec8a387
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/write.html
    icon: bi bi-globe
tldri18n_status: 2
---
# write

向某个终端上的特定用户的屏幕写入信息（Ctrl-C 来停止写入）。
使用 `who` 命令来获取所有活动用户的终端 id. 参见 `mesg`.
更多信息：<https://manned.org/write>.

- 向指定的终端 ID 上的指定用户写入信息：

`write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">terminal_id</span>

- 向终端 "/dev/tty/5" 上的用户 "testuser" 发送信息：

`write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testuser</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty/5</span>

- 向伪终端 "/dev/pts/5" 上的用户 "johndoe" 发送信息：

`write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">johndoe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pts/5</span>
