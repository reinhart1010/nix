---
layout: page
title: linux/talk (English)
description: "A visual communication program which copies lines from your terminal to that of another user."
content_hash: a6e6de010c9e6fd98e41ae4103b039b6824d3344
last_modified_at: 2023-12-29
tldri18n_status: 2
---
# talk

A visual communication program which copies lines from your terminal to that of another user.
More information: <https://www.gnu.org/software/inetutils/manual/html_node/talk-invocation.html>.

- Start a talk session with a user on the same machine:

`talk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Start a talk session with a user on the same machine, who is logged in on tty3:

`talk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty3</span>

- Start a talk session with a user on a remote machine:

`talk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Clear text on both terminal screens:

`<Ctrl>+D`

- Exit the talk session:

`<Ctrl>+C`
