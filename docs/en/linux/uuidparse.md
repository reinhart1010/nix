---
layout: page
title: linux/uuidparse (English)
description: "Parse universally unique identifiers."
content_hash: 54f5c2f355321e6fd91d752507e4cf3469b2d44c
last_modified_at: 2024-01-23
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/uuidparse.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uuidparse

Parse universally unique identifiers.
See also: `uuidgen`.
More information: <https://manned.org/uuidparse.1>.

- Parse the specified UUIDs, use a tabular output format:

`uuidparse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid1 uuid2 ...</span>

- Parse UUIDs from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | uuidparse`

- Use the JSON output format:

`uuidparse --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid1 uuid2 ...</span>

- Do not print a header line:

`uuidparse --noheadings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid1 uuid2 ...</span>

- Use the raw output format:

`uuidparse --raw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid1 uuid2 ...</span>

- Specify which of the four output columns to print:

`uuidparse --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UUID,VARIANT,TYPE,TIME</span>

- Display help:

`uuidparse -h`
