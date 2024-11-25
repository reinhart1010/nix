---
layout: page
title: linux/tmt-try (English)
description: "Quickly experiment with tests and environments."
content_hash: 170f2bd8c8fa3f726fe9a58e0814eb1eb08a1d84
last_modified_at: 2024-11-25
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tmt-try.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tmt try

Quickly experiment with tests and environments.
More information: <https://tmt.readthedocs.io/en/stable/stories/cli.html#try>.

- Quickly experiment with the default provision method (no tests in the CWD):

`tmt try`

- Run a test in the current working directory:

`cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test</span>` && tmt try`

- Use a specific operating system:

`tmt try `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora-41</span>

- Select both custom image and provision method:

`tmt try `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora@container</span>

- Select tests with custom filter:

`tmt try --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>

- Provision guest and wait for instructions:

`tmt try --ask`

- Directly log into the guest without asking:

`tmt try --login`

- Display help:

`tmt try --help`
