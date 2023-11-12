---
layout: page
title: linux/readpe (English)
description: "Displays information about PE files."
content_hash: 5cb57dc2160f716626d2c20dadec8a8fad3e1db4
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# readpe

Displays information about PE files.
More information: <https://manned.org/readpe>.

- Display all information about a PE file:

`readpe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>

- Display all the headers present in a PE file:

`readpe --all-headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>

- Display all the sections present in a PE file:

`readpe --all-sections `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>

- Display a specific header from a PE file:

`readpe --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dos|coff|optional</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>

- List all imported functions:

`readpe --imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>

- List all exported functions:

`readpe --exports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>
