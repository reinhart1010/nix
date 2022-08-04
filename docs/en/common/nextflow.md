---
layout: page
title: common/nextflow (English)
description: "Tool for running computational pipelines. Mostly used for bioinformatics workflows."
content_hash: b3ae5824070d002bd668936c1a82b02d9b18b41a
---
# nextflow

Tool for running computational pipelines. Mostly used for bioinformatics workflows.
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
