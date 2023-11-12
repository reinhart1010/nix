---
layout: page
title: linux/xfce4-terminal (English)
description: "The XFCE4 terminal emulator."
content_hash: 8b413d6423a885c8e700fc94af9e651864524419
last_modified_at: 2023-11-12
related_topics:
  - title: Indonesia version
    url: /id/linux/xfce4-terminal.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/xfce4-terminal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xfce4-terminal

The XFCE4 terminal emulator.
More information: <https://docs.xfce.org/apps/xfce4-terminal/start>.

- Open a new terminal window:

`xfce4-terminal`

- Set the initial title:

`xfce4-terminal --initial-title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">initial_title</span>`"`

- Open a new tab in the current terminal window:

`xfce4-terminal --tab`

- Execute a command in a new terminal window:

`xfce4-terminal --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_with_args</span>`"`

- Keep the terminal around after the executed command finishes executing:

`xfce4-terminal --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_with_args</span>`" --hold`

- Open multiple new tabs, executing a command in each:

`xfce4-terminal --tab --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_a</span>`" --tab --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_b</span>`"`
