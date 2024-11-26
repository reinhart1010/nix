---
layout: page
title: linux/tmt-run (English)
description: "Execute tmt test steps. By default, all steps are run."
content_hash: 610ab124c8ce761d4cbb669aa927337073511e02
last_modified_at: 2024-11-26
tldri18n_status: 2
---
# tmt run

Execute tmt test steps. By default, all steps are run.
More information: <https://tmt.readthedocs.io/en/stable/overview.html#run>.

- Run all test steps for each plan:

`tmt run`

- Run only the discover step to show what tests would be run:

`tmt run discover -v`

- Run all steps and adjust the provision step options:

`tmt run --all provision --how `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora:rawhide</span>

- Run only selected plans and tests:

`tmt run plan --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/plan/name</span>` test --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/test/name</span>

- Show results from the last run in a web browser:

`tmt run --last report --how `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` --open`

- Run tests with the provided context:

`tmt run --context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key=value</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distro=fedora</span>

- Run tests interactively (debug test code in the middle of a test):

`tmt run --all execute --how `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmt</span>` --interactive`

- Use dry mode to see what actions would happen and use the highest verbosity:

`tmt run --dry -vvv`
