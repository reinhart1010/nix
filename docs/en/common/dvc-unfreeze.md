---
layout: page
title: common/dvc-unfreeze (English)
description: "Unfreeze stages in the DVC pipeline."
content_hash: a6ad33caf5809f148d3c23506d7592fe4beb1cad
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dvc unfreeze

Unfreeze stages in the DVC pipeline.
This allows DVC to start tracking changes in stage dependencies again after they were frozen.
See also `dvc freeze`.
More information: <https://dvc.org/doc/command-reference/unfreeze>.

- Unfreeze 1 or more specified stages:

`dvc unfreeze `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stage_name_a</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stage_name_b</span>` ...]`
