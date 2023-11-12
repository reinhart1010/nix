---
layout: page
title: osx/dot_clean (English)
description: "Merge ._* files with corresponding native files."
content_hash: 6ac1dc811e3bd1f515d5b8ca8b0455fdbd1e21e4
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/dot_clean.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/dot_clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dot_clean

Merge ._* files with corresponding native files.
More information: <https://ss64.com/osx/dot_clean.html>.

- Merge all `._*` files recursively:

`dot_clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Don't recursively merge all `._*` in a directory (flat merge):

`dot_clean -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Merge and delete all `._*` files:

`dot_clean -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Only delete `._*` files if there's a matching native file:

`dot_clean -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Follow symlinks:

`dot_clean -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Print verbose output:

`dot_clean -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
