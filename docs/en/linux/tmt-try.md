---
layout: page
title: linux/tmt-try (English)
description: "Quickly experiment with tests and environments."
content_hash: 170f2bd8c8fa3f726fe9a58e0814eb1eb08a1d84
last_modified_at: 2024-11-26
tldri18n_status: 2
---
# tmt try

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
