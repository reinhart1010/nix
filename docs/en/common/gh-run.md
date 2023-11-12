---
layout: page
title: common/gh-run (English)
description: "View, run and watch recent GitHub Actions workflow runs."
content_hash: a43ddccdb7c56c5ac65b26ab0b07e539859c99b2
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gh run

View, run and watch recent GitHub Actions workflow runs.
More information: <https://cli.github.com/manual/gh_run>.

- Interactively select a run to see information about the jobs:

`gh run view`

- Display information about a specific run:

`gh run view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workflow_run_number</span>

- Display information about the steps of a job:

`gh run view --job=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_number</span>

- Display the log of a job:

`gh run view --job=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_number</span>` --log`

- Check a specific workflow and exit with a non-zero status if the run failed:

`gh run view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workflow_run_number</span>` --exit-status && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "run pending or passed"</span>

- Interactively select an active run and wait until it's done:

`gh run watch`

- Display the jobs for a run and wait until it's done:

`gh run watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workflow_run_number</span>

- Re-run a specific workflow:

`gh run rerun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workflow_run_number</span>
