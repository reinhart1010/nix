---
layout: page
title: linux/xfce4-terminal (English)
description: "The XFCE4 terminal emulator."
content_hash: 93163c70e8783b3b5819a00a247cb11e19f2adb2
last_modified_at: 2024-01-31
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

`xfce4-terminal --tab --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1</span>`" --tab --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command2</span>`"`
