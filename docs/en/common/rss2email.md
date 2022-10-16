---
layout: page
title: common/rss2email (English)
description: "Tool for delivering news from RSS feeds to an email program."
content_hash: cdef3d6b4488b80e2933d3792e774eee7784605b
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rss2email

Tool for delivering news from RSS feeds to an email program.
More information: <https://github.com/rss2email/rss2email>.

- List all feeds:

`r2e list`

- Convert RSS entries to email:

`r2e run`

- Add a feed:

`r2e add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feed_address</span>

- Add a feed with a specific email address:

`r2e add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feed_address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_email@example.com</span>

- Delete a specific feed:

`r2e delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_feed_in_list</span>

- Display help:

`r2e -h`
