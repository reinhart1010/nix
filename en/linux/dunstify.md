---
layout: page
title: linux/dunstify (English)
description: "A notification tool that is an extension of notify-send, but has more features based around dunst."
content_hash: 808c1398df38ac59c1618813d331a038bf8a8c1c
---
# dunstify

A notification tool that is an extension of notify-send, but has more features based around dunst.
Works with all options that work for notify-send.
More information: <https://wiki.archlinux.org/title/Dunst#Dunstify>.

- Show a notification with a given title and message:

`dunstify "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Title</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Message</span>`"`

- Show a notification with specified urgency:

`dunstify "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Title</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Message</span>`" -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">low|normal|critical</span>

- Specify a message ID (overwrites any previous messages with the same ID):

`dunstify "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Title</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Message</span>`" -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">123</span>

- To see other possible options:

`notify-send --help`
