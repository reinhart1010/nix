---
layout: page
title: common/nkf (English)
description: "Network kanji filter."
content_hash: 429da0a35d953c65d73c07cda27787674bea4ada
---
# nkf

Network kanji filter.
Converts kanji code from one encoding to another.
More information: <https://manned.org/nkf>.

- Convert to UTF-8 encoding:

`nkf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Convert to SHIFT_JIS encoding:

`nkf -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Convert to UTF-8 encoding and overwrite the file:

`nkf -w --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Set new line code to LF and overwrite (UNIX type):

`nkf -d --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Set new line code to CRLF and overwrite (windows type):

`nkf -c --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Decrypt mime file and overwrite:

`nkf -m --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>
