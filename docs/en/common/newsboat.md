---
layout: page
title: common/newsboat (English)
description: "An RSS/Atom feed reader for text terminals."
content_hash: 859a1639962733bea3769e63bf8b62e9a564bf0d
last_modified_at: 2023-06-28
related_topics:
  - title: العربية version
    url: /ar/common/newsboat.html
    icon: bi bi-globe
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

- Execute a space-separated list of commands in non-interactive mode:

`newsboat -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reload print-unread ...</span>

- See keyboard shortcuts (the most relevant are visible in the status line):

`?`
