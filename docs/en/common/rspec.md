---
layout: page
title: common/rspec (English)
description: "Behavior-driven development testing framework written in Ruby to test Ruby code."
content_hash: cb34cccc5e198a2044f4cc8345333f2bf24756df
last_modified_at: 2024-01-31
related_topics:
  - title: Indonesia version
    url: /id/common/rspec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rspec

Behavior-driven development testing framework written in Ruby to test Ruby code.
More information: <https://rspec.info>.

- Initialize an .rspec configuration and a spec helper file:

`rspec --init`

- Run all tests:

`rspec`

- Run a specific directory of tests:

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Run one or more test files:

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Run a specific test in a file (e.g. the test starts on line 83):

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">83</span>

- Run specs with a specific seed:

`rspec --seed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seed_number</span>
