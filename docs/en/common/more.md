---
layout: page
title: common/more (English)
description: "Open a file for interactive reading, allowing scrolling and search."
content_hash: 68c739dfb086b75d2283cbdf15b68d8923823c44
last_modified_at: 2024-01-30
related_topics:
  - title: español version
    url: /es/common/more.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/more.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/more.html
    icon: bi bi-globe
tldri18n_status: 2
---
# more

Open a file for interactive reading, allowing scrolling and search.
More information: <https://manned.org/more>.

- Open a file:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a file displaying from a specific line:

`more +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Go to the next page:

`<Space>`

- Search for a string (press `n` to go to the next match):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">something</span>

- Exit:

`q`

- Display help about interactive commands:

`h`

- Display help:

`more --help`
