---
layout: page
title: common/pint (English)
description: "An opinionated PHP code style fixer based on PHP-CS-Fixer."
content_hash: 4b0c54447434b8fbae8cfe5fa76d725a2cb03e3e
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Pint

An opinionated PHP code style fixer based on PHP-CS-Fixer.
More information: <https://laravel.com/docs/pint>.

- Execute code style fixing:

`pint`

- Display all files that are changed:

`pint -v`

- Execute code style linting without applying changes:

`pint --test`

- Execute code style fixes using a specific config file:

`pint --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pint.json</span>

- Execute code style fixes using a specific preset:

`pint --preset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">psr12</span>
