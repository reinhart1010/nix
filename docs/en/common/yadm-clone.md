---
layout: page
title: common/yadm-clone (English)
description: "Works just like `git clone`. In addition you can pass extra flags to configure your repository."
content_hash: 77d46946d239cf2e04c46ecf474f73c699745185
last_modified_at: 2024-10-02
tldri18n_status: 2
---
# yadm-clone

Works just like `git clone`. In addition you can pass extra flags to configure your repository.
If there is a bootstrap file in the repository, you will be prompted to execute it.
See also: `git clone`.
More information: <https://yadm.io/docs/common_commands>.

- Clone an existing repository:

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_location</span>

- Clone an existing repository, then execute the bootstrap file:

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_location</span>` --bootstrap`

- Clone an existing repository and after cloning, do not execute the bootstrap file:

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_location</span>` --no-bootstrap`

- Change the worktree that `yadm` will use during cloning:

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_location</span>` --w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">worktree_file</span>

- Change the branch that `yadm` gets files from:

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_location</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>

- Override an existing repository local branch:

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_location</span>` -f`
