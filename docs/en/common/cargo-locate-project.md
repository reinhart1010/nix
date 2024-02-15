---
layout: page
title: common/cargo-locate-project (English)
description: "Print the full path to the `Cargo.toml` manifest of a project."
content_hash: 2095d45cfff64eac42ec5a4adfd964d4fee8eebf
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# cargo locate-project

Print the full path to the `Cargo.toml` manifest of a project.
If the project is part of a workspace, the manifest of the project is shown, rather than that of the workspace.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-locate-project.html>.

- Display the JSON object with full path to the `Cargo.toml` manifest:

`cargo locate-project`

- Display the project path in the specified format:

`cargo locate-project --message-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain|json</span>

- Display the `Cargo.toml` manifest located at the root of the workspace as opposed to the current workspace member:

`cargo locate-project --workspace`

- Display the `Cargo.toml` manifest of a specific directory:

`cargo locate-project --manifest-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Cargo.toml</span>
