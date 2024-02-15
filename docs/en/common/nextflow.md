---
layout: page
title: common/nextflow (English)
description: "Run computational pipelines. Mostly used for bioinformatics workflows."
content_hash: 12451f79acddf39da5335adba6b7d6246e6bd388
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# nextflow

Run computational pipelines. Mostly used for bioinformatics workflows.
More information: <https://www.nextflow.io>.

- Run a pipeline, use cached results from previous runs:

`nextflow run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main.nf</span>` -resume`

- Run a specific release of a remote workflow from GitHub:

`nextflow run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/repo</span>` -revision `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release_tag</span>

- Run with a given work directory for intermediate files, save execution report:

`nextflow run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workflow</span>` -work-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -with-report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">report.html</span>

- Show details of previous runs in current directory:

`nextflow log`

- Remove cache and intermediate files for a specific run:

`nextflow clean -force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">run_name</span>

- List all downloaded projects:

`nextflow list`

- Pull the latest version of a remote workflow from Bitbucket:

`nextflow pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/repo</span>` -hub bitbucket`

- Update Nextflow:

`nextflow self-update`
