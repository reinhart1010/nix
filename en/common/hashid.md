---
layout: page
title: common/hashid (English)
description: "Python3 program that identifies data and password hashes."
content_hash: 4d96c2c5dc6280ad92b5fc9e301ad7e771e5bb84
---
# hashid

Python3 program that identifies data and password hashes.
More information: <https://github.com/psypanda/hashID>.

- Identify hashes from standard input (through typing, copying and pasting, or piping the hash into the program):

`hashid`

- Identify hashes passed as arguments (multiple hashes can be passed):

`hashid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>

- Identify hashes on a file (one hash per line):

`hashid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hashes.txt</span>

- Show all possible hash types (including salted hashes):

`hashid --extended `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>

- Show `hashcat`'s mode number and `john`'s format string of the hash types:

`hashid --mode --john `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>

- Save output to a file instead of printing to standard output:

`hashid --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>
