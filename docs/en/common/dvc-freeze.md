---
layout: page
title: common/dvc-freeze (English)
description: "Freeze stages in the DVC pipeline."
content_hash: 1be71ce9a520a913480f0040fe2ec182f8d3278c
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# dvc freeze

Freeze stages in the DVC pipeline.
This prevents DVC from tracking changes in stage dependencies and re-execution until unfreeze.
See also `dvs unfreeze`.
More information: <https://dvc.org/doc/command-reference/freeze>.

- Freeze one or more specified stages:

`dvc freeze `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stage_name1 stage_name2 ...</span>
