---
layout: page
title: common/newsboat (English)
description: "An RSS/Atom feed reader for text terminals."
content_hash: 98b8026f04dd02249ca1e0d8a09b9903572ff55e
last_modified_at: 2024-01-31
related_topics:
  - title: العربية version
    url: /ar/common/newsboat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# newsboat

An RSS/Atom feed reader for text terminals.
More information: <https://newsboat.org/>.

- First import feed URLs from an OPML file:

`newsboat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my-feeds.xml</span>

- Alternatively, add feeds manually:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/path/to/feed</span>` >> "${HOME}/.newsboat/urls"`

- Start Newsboat and refresh all feeds on startup:

`newsboat -r`

- Execute one or more commands in non-interactive mode:

`newsboat -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reload print-unread ...</span>

- See keyboard shortcuts (the most relevant are visible in the status line):

`?`
