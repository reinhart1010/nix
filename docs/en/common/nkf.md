---
layout: page
title: common/nkf (English)
description: "Network kanji filter: convert kanji code from one encoding to another."
content_hash: 0a2d2d619416a06cee25c149f73fb266fb3cce50
last_modified_at: 2024-04-26
tldri18n_status: 2
---
# nkf

Network kanji filter: convert kanji code from one encoding to another.
More information: <https://manned.org/nkf>.

- Convert to UTF-8 encoding:

`nkf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Convert to SHIFT_JIS encoding:

`nkf -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Convert to UTF-8 encoding and overwrite the file:

`nkf -w --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Use LF as the new line code and overwrite (UNIX type):

`nkf -d --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Use CRLF as the new line code and overwrite (windows type):

`nkf -c --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Decrypt mime file and overwrite:

`nkf -m --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>
