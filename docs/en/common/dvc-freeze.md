---
layout: page
title: common/dvc-freeze (English)
description: "Freeze stages in the DVC pipeline."
content_hash: 24c36e58b16b04e82c1e673e9c26760df5e45733
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dvc freeze

Freeze stages in the DVC pipeline.
This prevents DVC from tracking changes in stage dependencies and re-execution until unfreeze.
See also `dvs unfreeze`.
More information: <https://dvc.org/doc/command-reference/freeze>.

- Freeze 1 or more specified stages:

`dvc freeze `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stage_name_a</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stage_name_b</span>` ...]`
