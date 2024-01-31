---
layout: page
title: osx/chflags (English)
description: "Change file or directory flags."
content_hash: 189e5f1b0b7b7718c615267f3b34b63bd3515830
last_modified_at: 2024-01-31
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/osx/chflags.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/chflags.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chflags

Change file or directory flags.
More information: <https://keith.github.io/xcode-man-pages/chflags.1.html>.

- Set the `hidden` flag for a file:

`chflags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hidden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Unset the `hidden` flag for a file:

`chflags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nohidden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Recursively set the `uchg` flag for a directory:

`chflags -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uchg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Recursively unset the `uchg` flag for a directory:

`chflags -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouchg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
