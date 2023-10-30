---
layout: page
title: common/cargo-locate-project (English)
description: "Print the full path to the `Cargo.toml` manifest of the current project."
content_hash: 907f7941315954d40ad1029f5be56a0f88f77e19
last_modified_at: 2023-10-30
---
# cargo locate-project

Print the full path to the `Cargo.toml` manifest of the current project.
If the project is part of a workspace, the manifest of the project is shown, rather than that of the workspace.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-locate-project.html>.

- Print the JSON object to `stdout` with full path to the `Cargo.toml` manifest:

`cargo locate-project`

- Print the project path in the specified format:

`cargo locate-project --message-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain|json</span>

- Print the `Cargo.toml` manifest located at the root of the workspace as opposed to the current workspace member:

`cargo locate-project --workspace`
