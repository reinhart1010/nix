---
layout: page
title: common/yadm-gitconfig (English)
description: "Pass options to `git config`. Change the `.gitconfig` of the repository managed by `yadm`."
content_hash: 13235c368c7d22bff2513707bf62f4352d274105
last_modified_at: 2024-10-02
tldri18n_status: 2
---
# yadm-gitconfig

Pass options to `git config`. Change the `.gitconfig` of the repository managed by `yadm`.
See also: `git config`.
More information: <https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#commands>.

- Update or set a Git configuration value:

`yadm gitconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key.inner-key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Get a value from `yadm`'s Git configuration:

`yadm gitconfig --get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Unset a value in `yadm`'s Git configuration:

`yadm gitconfig --unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- List all values in `yadm`'s Git configuration:

`yadm gitconfig --list`
