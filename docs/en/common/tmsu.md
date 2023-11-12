---
layout: page
title: common/tmsu (English)
description: "Simple command-line tool for tagging files."
content_hash: 26198bfcab63cd81fd1d0153821f18bc02d0020a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tmsu

Simple command-line tool for tagging files.
More information: <https://tmsu.org>.

- Tag a specific file with multiple tags:

`tmsu tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mp3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">music</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">big-jazz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>

- Tag multiple files:

`tmsu tag --tags "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">music mp3</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.mp3</span>

- List tags of specified file(s):

`tmsu tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.mp3</span>

- List files with specified tag(s):

`tmsu files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">big-jazz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">music</span>

- List files with tags matching boolean expression:

`tmsu files "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(year >= 1990 and year <= 2000)</span>` and `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grunge</span>`"`

- Mount tmsu virtual filesystem to an existing directory:

`tmsu mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
