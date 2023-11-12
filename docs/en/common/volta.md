---
layout: page
title: common/volta (English)
description: "A JavaScript Tool Manager that installs Node.js runtimes, npm and Yarn package managers, or any binaries from npm."
content_hash: 38601dd194f81c85dc3c2a5d605be32912f64101
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# volta

A JavaScript Tool Manager that installs Node.js runtimes, npm and Yarn package managers, or any binaries from npm.
More information: <https://volta.sh>.

- List all installed tools:

`volta list`

- Install the latest version of a tool:

`volta install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node|npm|yarn|package_name</span>

- Install a specific version of a tool:

`volta install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node|npm|yarn</span>`@version`

- Choose a tool version for a project (will store it in `package.json`):

`volta pin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node|npm|yarn</span>`@version`

- Display help:

`volta help`

- Display help for a subcommand:

`volta help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fetch|install|uninstall|pin|list|completions|which|setup|run|help</span>
