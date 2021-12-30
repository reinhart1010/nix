---
layout: page
title: common/mu (English)
description: "Index and search emails from a local Maildir."
content_hash: 25925bacb294585387fc2fbeab495857a6154493
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mu

Index and search emails from a local Maildir.
More information: <https://man.cx/mu>.

- Initialize the email database, optionally specifying the Maildir directory and email addresses:

`mu init --maildir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --my-address=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name@example.com</span>

- Index new emails:

`mu index`

- Find messages using a specific keyword (in message body, subject, sender, ...):

`mu find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Find messages to Alice with subject `jellyfish` containing the words `apples` or `oranges`:

`mu find to:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice</span>` subject:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jellyfish</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apples</span>` OR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oranges</span>

- Find unread messages about words starting with `soc` (the `*` only works at the end of the search term) in the Sent Items folder:

`mu find 'subject:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">soc</span>`*' flag:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unread</span>` maildir:'/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Sent Items</span>`'`

- Find messages from Sam with attached images, between 2 KiB and 2 MiB, written in 2021:

`mu find 'mime:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image/*</span>` size:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2k..2m</span>` date:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20210101..20211231</span>` from:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sam</span>

- List contacts with `Bob` in either name or email address:

`mu cfind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Bob</span>
