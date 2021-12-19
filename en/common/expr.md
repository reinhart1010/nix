---
layout: page
title: common/expr (English)
description: "Evaluate expressions and manipulate strings."
content_hash: 8df8d3f4d182cf7e99cf74d211fc20982181b9e2
---
# expr

Evaluate expressions and manipulate strings.
More information: <https://www.gnu.org/software/coreutils/expr>.

- Get string length:

`expr length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- Evaluate logical or math expression with an operator ('+', '-', '*', '&', '|', etc.). Special symbols should be escaped:

`expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_argument</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">operator</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_argument</span>

- Get position of the first character in 'string' that matches 'substring':

`echo $(expr index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">substring</span>`)`

- Extract part of the string:

`echo $(expr substr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">position_to_start</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_characters</span>

- Extract part of the string which matches a regular expression:

`echo $(expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` : '\(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`\)')`
