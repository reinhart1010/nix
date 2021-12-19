---
layout: page
title: common/grex (English)
description: "Simple command-line tool to generate regular expressions."
content_hash: 07345649284fce8fb24500691745a50e882ef000
---
# grex

Simple command-line tool to generate regular expressions.
More information: <https://github.com/pemistahl/grex>.

- Generate a simple regular expression:

` grex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">space_separated_strings</span>

- Generate a case-insensitive regular expression:

`grex -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">space_separated_strings</span>

- Replace digits with '\d':

`grex -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">space_separated_strings</span>

- Replace Unicode word character with '\w':

`grex -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">space_separated_strings</span>

- Replace spaces with '\s':

`grex -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">space_separated_strings</span>

- Add {min, max} quantifier representation for repeating sub-strings:

`grex -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">space_separated_strings</span>
