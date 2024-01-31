---
layout: page
title: common/unison (English)
description: "Bidirectional file synchronisation tool."
content_hash: db51095565abda4b60fda303d1f77dc664a67833
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# unison

Bidirectional file synchronisation tool.
More information: <https://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-manual.html>.

- Sync two directories (creates log first time these two directories are synchronized):

`unison `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_2</span>

- Automatically accept the (non-conflicting) defaults:

`unison `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_2</span>` -auto`

- Ignore some files using a pattern:

`unison `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_2</span>` -ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- View documentation:

`unison -doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topics</span>
