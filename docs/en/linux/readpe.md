---
layout: page
title: linux/readpe (English)
description: "Display information about PE files."
content_hash: bb4ad84797d7be2d8a12849ea7e12774f0ed3c4b
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# readpe

Display information about PE files.
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
