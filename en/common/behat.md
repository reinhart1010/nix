---
layout: page
title: common/behat (English)
description: "A PHP framework for Behaviour-Driven Development."
content_hash: 1fc0f3247260a5adaf9bf42d9ad7435142e9227e
related_topics:
  - title: italiano version
    url: /it/common/behat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/behat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/behat.html
    icon: bi bi-globe
---
# behat

A PHP framework for Behaviour-Driven Development.
More information: <https://behat.org>.

- Initialize a new Behat project:

`behat --init`

- Run all tests:

`behat`

- Run all tests from the specified suite:

`behat --suite=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suite_name</span>

- Run tests with a specific output formatter:

`behat --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pretty|progress</span>

- Run tests and output results to a file:

`behat --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display a list of definitions in your test suites:

`behat --definitions`
