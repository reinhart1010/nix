---
layout: page
title: common/phpunit (English)
description: "PHPUnit command-line test runner."
content_hash: b23138c01f75c69803472046121bc304c2b14783
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

`phpunit --coverage-html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>
