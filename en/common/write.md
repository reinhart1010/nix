---
layout: page
title: common/write (English)
description: "Write a message on the terminal of a specified logged in user (ctrl-C to stop writing messages)."
content_hash: 4cbe221d7be65d13f00f6b8c69503e8fb445d54b
related_topics:
  - title: 中文 version
    url: /zh/common/write.html
    icon: bi bi-globe
---
# write

Write a message on the terminal of a specified logged in user (ctrl-C to stop writing messages).
Use the `who` command to find out all terminal_ids of all active users active on the system. See also `mesg`.

- Send a message to a given user on a given terminal id:

`write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">terminal_id</span>

- Send message to "testuser" on terminal `/dev/tty/5`:

`write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testuser</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty/5</span>

- Send message to "johndoe" on pseudo terminal `/dev/pts/5`:

`write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">johndoe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pts/5</span>
