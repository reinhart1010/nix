---
layout: page
title: common/pest (English)
description: "A PHP testing framework with a focus on simplicity."
content_hash: 38a1eee76065e787241a75e9df756f93ad4f96a2
---
# pest

A PHP testing framework with a focus on simplicity.
More information: <https://pestphp.com>.

- Initialise a standard Pest configuration in the current directory:

`pest --init`

- Run tests in the current directory:

`pest`

- Run tests annotated with the given group:

`pest --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Run tests and print the coverage report to stdout:

`pest --coverage`

- Run tests with coverage and fail if the coverage is less than the minimum percentage:

`pest --coverage --min=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>
