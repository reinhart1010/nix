---
layout: page
title: linux/eselect-news (English)
description: "An `eselect` module for reading Gentoo news items."
content_hash: c40a40d0a5dbaa428ccd672a94fb5a34933610a5
last_modified_at: 2024-10-05
tldri18n_status: 2
---
# eselect news

An `eselect` module for reading Gentoo news items.
Note: Portage will print a notice when a repository is synchronized and there are unread news items.
More information: <https://wiki.gentoo.org/wiki/Eselect#News>.

- List available news items with their numbers (all by default):

`eselect news list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all|new</span>

- Print the specified news items:

`eselect news read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number1 number2 ...</span>

- Print all unread news items:

`eselect news read`

- Mark the specified news items as unread:

`eselect news unread `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number1 number2 ...</span>

- Delete all read news items:

`eselect news purge`

- Print the number of available news items (new by default):

`eselect news count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all|new</span>
