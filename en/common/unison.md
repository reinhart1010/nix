---
layout: page
title: common/unison (English)
description: "Bidirectional file synchronisation tool."
content_hash: ca467e969509709cc815cac636900831a359fedb
---
# unison

Bidirectional file synchronisation tool.
More information: <https://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-manual.html>.

- Sync two directories (creates log first time these two directories are synchronised):

`unison `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_2</span>

- Automatically accept the (non-conflicting) defaults:

`unison `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_2</span>` -auto`

- Ignore some files using a pattern:

`unison `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_2</span>` -ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Show documentation:

`unison -doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topics</span>
