---
layout: page
title: common/r2e (English)
description: "Forwards RSS feeds to an email address."
content_hash: 758cd0917e850fa89864907d264cbc2527d9c256
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# r2e

Forwards RSS feeds to an email address.
Requires a configured `sendmail` or smtp setup.
More information: <https://github.com/rss2email/rss2email>.

- Create a new feed database that sends email to an email address:

`r2e new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email_address</span>

- Subscribe to a feed:

`r2e add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feed_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feed_URI</span>

- Send new stories to an email address:

`r2e run`

- List all feeds:

`r2e list`

- Delete a feed at a specified index:

`r2e delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index</span>
