---
layout: page
title: common/glab-pipeline (English)
description: "List, view, and run GitLab CI/CD pipelines."
content_hash: d7e663a715f6a1255a151f72c7c790193fdfb472
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># glab pipeline

List, view, and run GitLab CI/CD pipelines.
More information: <https://glab.readthedocs.io/en/latest/pipeline>.

- View a running pipeline on the current branch:

`glab pipeline status`

- View a running pipeline on a specific branch:

`glab pipeline status --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Get the list of pipelines:

`glab pipeline list`

- Run a manual pipeline on the current branch:

`glab pipeline run`

- Run a manual pipeline on a specific branch:

`glab pipeline run --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>
