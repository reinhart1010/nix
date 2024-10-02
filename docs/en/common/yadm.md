---
layout: page
title: common/yadm (English)
description: "A dotfiles manager that works by using `git`."
content_hash: e4b899ac6a71afb3b2b8df70a7c4f4d1a3179af9
last_modified_at: 2024-10-02
tldri18n_status: 2
---
# yadm

A dotfiles manager that works by using `git`.
Some subcommands such as `init`, `clone`, `push`, and `pull` have their own usage documentation.
More information: <https://yadm.io/docs/overview>.

- Override the `yadm` directory. `yadm` stores its configurations relative to this directory:

`yadm --yadm-dir`

- Override the `yadm` data directory: `yadm` stores its data relative to this directory:

`yadm --yadm-data`

- Override the location of the `yadm` repository:

`yadm --yadm-repo`

- Override the location of the `yadm` configuration file:

`yadm --yadm-config`

- Override the location of the `yadm` encryption configuration:

`yadm --yadm-encrypt`

- Override the location of the `yadm` encrypted files archive:

`yadm --yadm-archive`

- Override the location of the `yadm` bootstrap program:

`yadm --yadm-bootstrap`
