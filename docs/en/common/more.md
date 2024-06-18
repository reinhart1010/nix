---
layout: page
title: common/more (English)
description: "Interactively display a file, allowing scrolling and searching."
content_hash: 73e51adb73686d64e009ac32a355e577777c499b
last_modified_at: 2024-06-18
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

Interactively display a file, allowing scrolling and searching.
See also: `less`.
More information: <https://manned.org/more.1p>.

- Open a file:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display a specific line:

`more +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Go to the next page:

`<Space>`

- Search for a string (press `n` to go to the next match):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">something</span>

- Exit:

`q`

- Display help about interactive commands:

`h`
