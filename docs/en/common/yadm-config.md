---
layout: page
title: common/yadm-config (English)
description: "Pass options to `yadm`'s config file. Change the `.config` of the repository managed by `yadm`."
content_hash: 1b99e812300cdaee3c494c080ea34a64d018d095
last_modified_at: 2024-10-02
tldri18n_status: 2
---
# yadm-config

Pass options to `yadm`'s config file. Change the `.config` of the repository managed by `yadm`.
See also: <https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#configuration>.

- Set or update a `yadm`'s Git configuration:

`yadm config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key.inner-key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Get a value from `yadm`'s Git configuration:

`yadm config --get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Unset a value in `yadm`'s Git configuration:

`yadm config --unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- List all values in `yadm`'s Git configuration:

`yadm config --list`
