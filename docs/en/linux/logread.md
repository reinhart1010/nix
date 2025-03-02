---
layout: page
title: linux/logread (English)
description: "Read the `logd` ring buffer log."
content_hash: acc362450ef3463c6abfe1f2c1141287f3b4c60d
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/logread.html
    icon: bi bi-globe
tldri18n_status: 2
---
# logread

Read the `logd` ring buffer log.
More information: <https://openwrt.org/docs/guide-user/base-system/log.essentials>.

- Print the log:

`logread`

- Print a specified number of messages:

`logread -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- Filter messages by (Keyword/Regular Expression):

`logread -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Print log messages as they happen:

`logread -f`
