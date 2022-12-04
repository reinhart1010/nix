---
layout: page
title: common/pest (English)
description: "A PHP testing framework with a focus on simplicity."
content_hash: 9b913412ff4a3e41e6e64baa2b307903fd7e2c08
last_modified_at: 2022-12-04
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

- Run tests and print the coverage report to `stdout`:

`pest --coverage`

- Run tests with coverage and fail if the coverage is less than the minimum percentage:

`pest --coverage --min=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>
