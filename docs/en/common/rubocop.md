---
layout: page
title: common/rubocop (English)
description: "Lint Ruby files."
content_hash: b88992433d587fb4257d37557883a82eebaa5cb9
last_modified_at: 2024-09-08
related_topics:
  - title: español version
    url: /es/common/rubocop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/rubocop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rubocop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rubocop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rubocop

Lint Ruby files.
More information: <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- Check all files in the current directory (including subdirectories):

`rubocop`

- Check one or more specific files or directories:

`rubocop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Write output to file:

`rubocop --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- View list of cops (linter rules):

`rubocop --show-cops`

- Exclude a cop:

`rubocop --except `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop1 cop2 ...</span>

- Run only specified cops:

`rubocop --only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cop1 cop2 ...</span>

- Auto-correct files (experimental):

`rubocop --auto-correct`
