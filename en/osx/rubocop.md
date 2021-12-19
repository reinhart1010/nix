---
layout: page
title: osx/rubocop (English)
description: "Lint Ruby files."
content_hash: 2118d85f785a7a241f5964117504ea6356585f9d
related_topics:
  - title: español version
    url: /es/osx/rubocop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/rubocop.html
    icon: bi bi-globe
---
# rubocop

Lint Ruby files.

- Check all files in the current directory (including subdirectories):

`rubocop`

- Check one or more specific files or directories:

`rubocop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Write output to file:

`rubocop --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- View list of cops (linter rules):

`rubocop --show-cops`

- Exclude a cop:

`rubocop --except `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_2</span>

- Run only specified cops:

`rubocop --only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop_2</span>

- Auto-correct files (experimental):

`rubocop --auto-correct`
