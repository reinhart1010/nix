---
layout: page
title: common/rspec (English)
description: "Behavior-driven development testing framework written in Ruby to test Ruby code."
content_hash: 22d4e128f4b4bd9d70d659fd2cee8765bd60ee82
---
# rspec

Behavior-driven development testing framework written in Ruby to test Ruby code.
More information: <https://rspec.info>.

- Initialise an .rspec config and a spec helper file:

`rspec --init`

- Run all tests:

`rspec`

- Run a specific directory of tests:

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Run a specific test file:

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Run multiple test files:

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Run a specific test in a file (e.g. the test starts on line 83):

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">83</span>

- Run specs with a specific seed:

`rspec --seed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seed_number</span>
