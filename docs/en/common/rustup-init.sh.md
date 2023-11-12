---
layout: page
title: common/rustup-init.sh (English)
description: "Script to install `rustup` and the Rust toolchain."
content_hash: 3126beffe167d524c7b705dc3f46fe045fa247d1
last_modified_at: 2023-11-12
related_topics:
  - title: தமிழ் version
    url: /ta/common/rustup-init.sh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustup-init.sh

Script to install `rustup` and the Rust toolchain.
More information: <https://forge.rust-lang.org/infra/other-installation-methods.html#rustup>.

- Download and run `rustup-init` to install `rustup` and the default Rust toolchain:

`curl https://sh.rustup.rs -sSf | sh -s`

- Download and run `rustup-init` and pass arguments to it:

`curl https://sh.rustup.rs -sSf | sh -s -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Run `rustup-init` and specify additional components or targets to install:

`rustup-init.sh --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` --component `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component</span>

- Run `rustup-init` and specify the default toolchain to install:

`rustup-init.sh --default-toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>

- Run `rustup-init` and do not install any toolchain:

`rustup-init.sh --default-toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none</span>

- Run `rustup-init` and specify an installation profile:

`rustup-init.sh --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minimal|default|complete</span>

- Run `rustup-init` without asking for confirmation:

`rustup-init.sh -y`
