---
layout: page
title: osx/look (English)
description: "Display lines beginning with a prefix in a sorted file."
content_hash: 1e63dac3719d482ace846e40a1addef52b667cfd
last_modified_at: 2024-06-12
related_topics:
  - title: español version
    url: /es/osx/look.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/look.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/look.html
    icon: bi bi-globe
tldri18n_status: 2
---
# look

Display lines beginning with a prefix in a sorted file.
See also: `grep`, `sort`.
More information: <https://keith.github.io/xcode-man-pages/look.1.html>.

- Search for lines beginning with a specific prefix in a specific file:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Case-insensitively search only on alphanumeric characters:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--ignore-case</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--alphanum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Specify a string termination character (space by default):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--terminate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- Search in `/usr/share/dict/words` (`--ignore-case` and `--alphanum` are assumed):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>
