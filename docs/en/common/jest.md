---
layout: page
title: common/jest (English)
description: "A zero-configuration JavaScript testing platform."
content_hash: ae93d44afb38ddcdc4dd4b62b4c08282a94a1f21
last_modified_at: 2024-01-31
related_topics:
  - title: français version
    url: /fr/common/jest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jest

A zero-configuration JavaScript testing platform.
More information: <https://jestjs.io>.

- Run all available tests:

`jest`

- Run the test suites from the given files:

`jest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Run the test suites from files within the current and subdirectories, whose paths match the given regular expression:

`jest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression2</span>

- Run the tests whose names match the given regular expression:

`jest --testNamePattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Run test suites related to a given source file:

`jest --findRelatedTests `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.js</span>

- Run test suites related to all uncommitted files:

`jest --onlyChanged`

- Watch files for changes and automatically re-run related tests:

`jest --watch`

- Display help:

`jest --help`
