---
layout: page
title: linux/man (English)
description: "Format and display manual pages."
content_hash: 90e940c890bd4848ca914a1b902ef74d37e9ba74
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/linux/man.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/man.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/man.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/man.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/man.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/man.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/man.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/man.html
    icon: bi bi-globe
tldri18n_status: 2
---
# man

Format and display manual pages.
More information: <https://manned.org/man>.

- Display the man page for a command:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display the man page for a command from section 7:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- List all available sections for a command:

`man --whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display the path searched for manpages:

`man --path`

- Display the location of a manpage rather than the manpage itself:

`man --where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display the man page using a specific locale:

`man --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">locale</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Search for manpages containing a search string:

`man --apropos "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>`"`
