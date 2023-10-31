---
layout: page
title: linux/talk (English)
description: "GNU/Talk is a visual communication program which copies lines from your terminal to that of another user."
content_hash: d5a1374b7123fdcbf86c73c9b22270d68c32251d
last_modified_at: 2023-10-31
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># talk

GNU/Talk is a visual communication program which copies lines from your terminal to that of another user.
More information: <https://www.gnu.org/software/inetutils/manual/html_node/talk-invocation.html>.

- Start a talk session with a user on the same machine:

`talk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Start a talk session with a user on the same machine, who is logged in on tty3:

`talk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty3</span>

- Start a talk session with a user on a remote machine:

`talk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Clear text on both terminal screens:

`Ctrl+D`

- Exit the talk session:

`Ctrl+C`
