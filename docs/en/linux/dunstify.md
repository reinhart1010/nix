---
layout: page
title: linux/dunstify (English)
description: "A notification tool that is an extension of `notify-send`, but has more features based around `dunst`."
content_hash: e3b4e91e239695298fe22738ed73d92998c039eb
last_modified_at: 2024-10-02
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/dunstify.html
    icon: bi bi-globe
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

`dunstify --help`
