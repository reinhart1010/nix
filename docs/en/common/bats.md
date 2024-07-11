---
layout: page
title: common/bats (English)
description: "Bash Automated Testing System: a TAP (<https://testanything.org/>) compliant testing framework for Bash."
content_hash: 84c139224ee09c6ce4fb1fc6493545237023896e
last_modified_at: 2024-07-11
related_topics:
  - title: español version
    url: /es/common/bats.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bats

Bash Automated Testing System: a TAP (<https://testanything.org/>) compliant testing framework for Bash.
More information: <https://bats-core.readthedocs.io/en/stable/usage.html>.

- Run a BATS test script and output results in the [t]AP (Test Anything Protocol) format:

`bats --tap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test.bats</span>

- [c]ount test cases of a test script without running any tests:

`bats --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test.bats</span>

- Run BATS test cases [r]ecursively (files with a `.bats` extension):

`bats --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Output results in a specific [F]ormat:

`bats --formatter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pretty|tap|tap13|junit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test.bats</span>

- Add [T]iming information to tests:

`bats --timing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test.bats</span>

- Run specific number of [j]obs in parallel (requires GNU `parallel` to be installed):

`bats --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test.bats</span>
