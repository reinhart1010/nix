---
layout: page
title: linux/more (English)
description: "Interactively display a file, allowing scrolling and searching."
content_hash: 8197c210902b9dc1e07977cf8366906effe9f573
last_modified_at: 2024-02-13
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/more.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># more

Interactively display a file, allowing scrolling and searching.
See also: `less`.
More information: <https://manned.org/more>.

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
