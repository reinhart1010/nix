---
layout: page
title: common/bats (English)
description: "Bash Automated Testing System: a TAP (<https://testanything.org/>) compliant testing framework for Bash."
content_hash: 369209520c26e902bd24342b8e65bf554ecbdd46
last_modified_at: 2024-02-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bats.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bats

Bash Automated Testing System: a TAP (<https://testanything.org/>) compliant testing framework for Bash.
More information: <https://bats-core.readthedocs.io/en/stable/usage.html>.

- Run a BATS test script and output results in the TAP (Test Anything Protocol) format:

`bats --tap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test.bats</span>

- Count test cases of a test script without running any tests:

`bats --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test.bats</span>

- Run BATS test cases contained in a directory and its subdirectories (files with a `.bats` extension):

`bats --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Output results in a specific format:

`bats --formatter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pretty|tap|junit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test.bats</span>
