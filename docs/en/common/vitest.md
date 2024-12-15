---
layout: page
title: common/vitest (English)
description: "Fast, modern testing framework built for Vite, offering seamless integration, TypeScript support, and a Jest-compatible API for unit, integration, and snapshot testing."
content_hash: 4467af09fadd904b921c2a84d40ea2a25f1a2e3c
last_modified_at: 2024-12-15
tldri18n_status: 2
---
# vitest

Fast, modern testing framework built for Vite, offering seamless integration, TypeScript support, and a Jest-compatible API for unit, integration, and snapshot testing.
More information: <https://vitest.dev/guide>.

- Run all available tests:

`vitest run`

- Run the test suites from the given files:

`vitest run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Run the test suites from files within the current and subdirectories, whose paths match the given regular expression:

`vitest run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression2</span>

- Run the tests whose names match the given regular expression:

`vitest run --testNamePattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Watch files for changes and automatically re-run related tests:

`vitest`

- Run tests with coverage:

`vitest run --coverage`

- Run all tests but stops immediately after the first test failure:

`vitest run --bail=1`

- Display help:

`vitest --help`
