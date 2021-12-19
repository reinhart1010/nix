---
layout: page
title: common/fly (English)
description: "Command-line tool for concourse-ci."
content_hash: fb8e3bf52dd1b62d545a5387acd84c43d6faa387
---
# fly

Command-line tool for concourse-ci.
More information: <https://concourse-ci.org/fly.html>.

- Authenticate with and save concourse target:

`fly --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>` login --team-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">team_name</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://ci.example.com</span>

- List targets:

`fly targets`

- List pipelines:

`fly -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>` pipelines`

- Upload or update a pipeline:

`fly -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>` set-pipeline --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipeline.yml</span>` --pipeline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipeline_name</span>

- Unpause pipeline:

`fly -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>` unpause-pipeline --pipeline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipeline_name</span>

- Show pipeline configuration:

`fly -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>` get-pipeline --pipeline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipeline_name</span>

- Update local copy of fly:

`fly -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>` sync`

- Destroy pipeline:

`fly -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>` destroy-pipeline --pipeline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipeline_name</span>
