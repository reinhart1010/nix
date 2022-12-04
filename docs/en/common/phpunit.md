---
layout: page
title: common/phpunit (English)
description: "PHPUnit command-line test runner."
content_hash: b147479151d478e30b39070c7f5b516903d15cf0
last_modified_at: 2022-12-04
---
# phpunit

PHPUnit command-line test runner.
More information: <https://phpunit.de>.

- Run tests in the current directory. Note: Expects you to have a 'phpunit.xml':

`phpunit`

- Run tests in a specific file:

`phpunit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/TestFile.php</span>

- Run tests annotated with the given group:

`phpunit --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Run tests and generate a coverage report in HTML:

`phpunit --coverage-html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
