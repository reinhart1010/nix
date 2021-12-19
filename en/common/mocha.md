---
layout: page
title: common/mocha (English)
description: "Execute Mocha JavaScript test runner."
content_hash: 574d1405730876562c3fd1a0410f8380fb27b151
---
# mocha

Execute Mocha JavaScript test runner.
More information: <https://mochajs.org>.

- Run tests with default configuration or as configured in `mocha.opts`:

`mocha`

- Run tests contained at a specific location:

`mocha `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory/with/tests</span>

- Run tests that match a specific grep pattern:

`mocha --grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Run tests on changes to JavaScript files in the current directory and once initially:

`mocha --watch`

- Run tests with a specific reporter:

`mocha --reporter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reporter</span>
