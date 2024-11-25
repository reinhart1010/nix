---
layout: page
title: linux/tmt (English)
description: "Test Management Tool for creating, running, and debugging tests."
content_hash: d1aa200e444a07160dd456f58c0ab03845b18981
last_modified_at: 2024-11-25
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tmt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tmt

Test Management Tool for creating, running, and debugging tests.
Some subcommands such as `run`, `try`, etc. have their own usage documentation.
More information: <https://tmt.readthedocs.io>.

- List available tests, plans, and stories:

`tmt`

- Initialize tmt files/project structure:

`tmt init`

- Create a new test with a template and a link:

`tmt test create --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beakerlib</span>` --link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verifies:issue#1234</span>

- List available tests, plans, or stories:

`tmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test|plan|story</span>` ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Show detailed test metadata in the given context:

`tmt --context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arch=aarch64</span>` test show`

- Validate tmt files against the specification:

`tmt lint`

- Use filter:

`tmt tests ls --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag:foo</span>` --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tier:0</span>

- Display help:

`tmt --help`
