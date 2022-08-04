---
layout: page
title: common/dvc-dag (English)
description: "Visualize the pipeline(s) defined in `dvc.yaml`."
content_hash: 2ea9a0f9cf560f81d7929de7e6642f5d1dd2ca82
---
# dvc dag

Visualize the pipeline(s) defined in `dvc.yaml`.
More information: <https://dvc.org/doc/command-reference/dag>.

- Visualize the entire pipeline:

`dvc dag`

- Visualize the pipeline stages up to a specified target stage:

`dvc dag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Export the pipeline in the dot format:

`dvc dag --dot > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pipeline.dot</span>
