---
layout: page
title: common/exrex (English)
description: "Generate all/random matching strings for a regular expression."
content_hash: f66da4e8125902c91358b188a3929677ad87e580
---
# exrex

Generate all/random matching strings for a regular expression.
It can also simplify regular expressions.
More information: <https://github.com/asciimoo/exrex>.

- Generate all possible strings that match a regular expression:

`exrex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`'`

- Generate a random string that matches a regular expression:

`exrex --random '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`'`

- Generate at most 100 strings that match a regular expression:

`exrex --max-number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`'`

- Generate all possible strings that match a regular expression, joined by a custom delimiter string:

`exrex --delimiter "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">, </span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`'`

- Print count of all possible strings that match a regular expression:

`exrex --count '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`'`

- Simplify a regular expression:

`exrex --simplify '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ab|ac</span>`'`

- Print eyes:

`exrex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[oO0](_)[oO0]</span>`'`

- Print a boat:

`exrex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">( {20}(\| *\\|-{22}|\|)|\.={50}| ( ){0,5}\\\.| {12}~{39})</span>`'`
