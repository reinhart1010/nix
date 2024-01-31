---
layout: page
title: common/hashid (English)
description: "Python3 program that identifies data and password hashes."
content_hash: 7890763074f416db472b87a40dbbc988e483e6fe
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# hashid

Python3 program that identifies data and password hashes.
More information: <https://github.com/psypanda/hashID>.

- Identify hashes from `stdin` (through typing, copying and pasting, or piping the hash into the program):

`hashid`

- Identify one or more hashes:

`hashid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash1 hash2 ...</span>

- Identify hashes on a file (one hash per line):

`hashid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hashes.txt</span>

- Show all possible hash types (including salted hashes):

`hashid --extended `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>

- Show `hashcat`'s mode number and `john`'s format string of the hash types:

`hashid --mode --john `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>

- Save output to a file instead of printing to `stdout`:

`hashid --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>
