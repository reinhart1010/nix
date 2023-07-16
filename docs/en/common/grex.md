---
layout: page
title: common/grex (English)
description: "Generate regular expressions."
content_hash: 594bd49ff4be3462e4559ba2c3c35419c2736563
last_modified_at: 2023-07-16
---
# grex

Generate regular expressions.
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
