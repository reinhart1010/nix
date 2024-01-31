---
layout: page
title: common/dvc-unfreeze (English)
description: "Unfreeze stages in the DVC pipeline."
content_hash: 36d1b624cdeeef192d842481323106c4ca32f913
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# dvc unfreeze

Unfreeze stages in the DVC pipeline.
This allows DVC to start tracking changes in stage dependencies again after they were frozen.
See also `dvc freeze`.
More information: <https://dvc.org/doc/command-reference/unfreeze>.

- Unfreeze one or more specified stages:

`dvc unfreeze `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stage_name1 stage_name2 ...</span>
