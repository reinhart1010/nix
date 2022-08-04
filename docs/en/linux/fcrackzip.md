---
layout: page
title: linux/fcrackzip (English)
description: "ZIP archive password cracking utility."
content_hash: a9d592d6721897b09dbc3f30896791d3314a6bf0
---
# fcrackzip

ZIP archive password cracking utility.
More information: <https://manned.org/fcrackzip>.

- Brute-force a password with a length of 4 to 8 characters, and contains only alphanumeric characters (order matters):

`fcrackzip --brute-force --length 4-8 --charset aA1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>

- Brute-force a password in verbose mode with a length of 3 characters that only contains lowercase characters, `$` and `%`:

`fcrackzip -v --brute-force --length 3 --charset a:$% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>

- Brute-force a password that contains only lowercase and special characters:

`fcrackzip --brute-force --length 4 --charset a! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>

- Brute-force a password containing only digits, starting from the password `12345`:

`fcrackzip --brute-force --length 5 --charset 1 --init-password 12345 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>

- Crack a password using a wordlist:

`fcrackzip --use-unzip --dictionary --init-password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wordlist</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>

- Benchmark cracking performance:

`fcrackzip --benchmark`
