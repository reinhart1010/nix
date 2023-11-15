---
layout: page
title: linux/dunstify (English)
description: "A notification tool that is an extension of `notify-send`, but has more features based around `dunst`."
content_hash: 3421db5037ba70d04c13ccc0a463e8617cca63f9
last_modified_at: 2023-11-15
tldri18n_status: 2
---
# dunstify

A notification tool that is an extension of `notify-send`, but has more features based around `dunst`.
Accepts all options of `notify-send`.
More information: <https://github.com/dunst-project/dunst/wiki/Guides>.

- Show a notification with a given title and message:

`dunstify "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Title</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Message</span>`"`

- Show a notification with specified urgency:

`dunstify "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Title</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Message</span>`" -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">low|normal|critical</span>

- Specify a message ID (overwrites any previous messages with the same ID):

`dunstify "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Title</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Message</span>`" -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">123</span>

- Display help:

`notify-send --help`
