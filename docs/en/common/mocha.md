---
layout: page
title: common/mocha (English)
description: "Execute Mocha JavaScript test runner."
content_hash: 406c5e035fdc91d15beed9586a6b1094a4731ea5
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# mocha

Execute Mocha JavaScript test runner.
More information: <https://mochajs.org>.

- Run tests with default configuration or as configured in `mocha.opts`:

`mocha`

- Run tests contained at a specific location:

`mocha `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory/with/tests</span>

- Run tests that match a specific `grep` pattern:

`mocha --grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Run tests on changes to JavaScript files in the current directory and once initially:

`mocha --watch`

- Run tests with a specific reporter:

`mocha --reporter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reporter</span>
