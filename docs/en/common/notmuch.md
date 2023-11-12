---
layout: page
title: common/notmuch (English)
description: "Command-line based program for indexing, searching, reading, and tagging large collections of email messages."
content_hash: 36d6c09f9a09e7f6b9bc0968d88e53d956ccf65c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# notmuch

Command-line based program for indexing, searching, reading, and tagging large collections of email messages.
More information: <https://notmuchmail.org/manpages/>.

- Configure for first use:

`notmuch setup`

- Add a tag for all messages matching a search term:

`notmuch tag +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom_tag</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>`"`

- Remove a tag for all messages matching a search term:

`notmuch tag -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom_tag</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>`"`

- Count messages matching the given search term:

`notmuch count --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">messages|threads</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>`"`

- Search for messages matching the given search term:

`notmuch search --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|text</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">summary|threads|messages|files|tags</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>`"`

- Limit the number of search results to X:

`notmuch search --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|text</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">summary|threads|messages|files|tags</span>` --limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>`"`

- Create a reply template for a set of messages:

`notmuch reply --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default|headers-only</span>` --reply-to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sender|all</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>`"`
