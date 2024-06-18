---
layout: page
title: common/man (English)
description: "Format and display manual pages."
content_hash: c4e7f88c6034aa319e44650432269d58625547d2
last_modified_at: 2024-06-18
related_topics:
  - title: italiano version
    url: /it/common/man.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/man.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/man.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/man.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/man.html
    icon: bi bi-globe
tldri18n_status: 2
---
# man

Format and display manual pages.
More information: <https://www.manned.org/man>.

- Display the man page for a command:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display the man page for a command from section 7:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- List all available sections for a command:

`man -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display the path searched for manpages:

`man --path`

- Display the location of a manpage rather than the manpage itself:

`man -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display the man page using a specific locale:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">locale</span>

- Search for manpages containing a search string:

`man -k "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>`"`
