---
layout: page
title: common/php-coveralls (English)
description: "A PHP client for Coveralls."
content_hash: 2c5ba15f221ff145f4d31defa721633932644080
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# php-coveralls

A PHP client for Coveralls.
More information: <https://php-coveralls.github.io/php-coveralls>.

- Send coverage information to Coveralls:

`php-coveralls`

- Send coverage information to Coveralls for a specific directory:

`php-coveralls --root_dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Send coverage information to Coveralls with a specific config:

`php-coveralls --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/.coveralls.yml</span>

- Send coverage information to Coveralls with verbose output:

`php-coveralls --verbose`

- Send coverage information to Coveralls excluding source files with no executable statements:

`php-coveralls --exclude-no-stmt`

- Send coverage information to Coveralls with a specific environment name:

`php-coveralls --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test|dev|prod</span>

- Specify multiple Coverage Clover XML files to upload:

`php-coveralls --coverage_clover `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/first_clover.xml</span>` --coverage_clover `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/second_clover.xml</span>

- Output the JSON that will be sent to Coveralls to a specific file:

`php-coveralls --json_path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/coveralls-upload.json</span>
