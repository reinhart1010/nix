---
layout: page
title: common/pest (English)
description: "A PHP testing framework with a focus on simplicity."
content_hash: b1f68461286194bfe67ab27e4f9dfa33737b4ffb
---
# pest

A PHP testing framework with a focus on simplicity.
More information: <https://pestphp.com>.

- Initialize a standard Pest configuration in the current directory:

`pest --init`

- Run tests in the current directory:

`pest`

- Run tests annotated with the given group:

`pest --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Run tests and print the coverage report to stdout:

`pest --coverage`

- Run tests with coverage and fail if the coverage is less than the minimum percentage:

`pest --coverage --min=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>
