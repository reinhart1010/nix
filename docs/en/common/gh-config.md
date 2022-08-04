---
layout: page
title: common/gh-config (English)
description: "Change configuration for GitHub cli."
content_hash: 048febc7f0c57cd1350e59cc15bdf0a43c68d2ad
---
# gh config

Change configuration for GitHub cli.
More information: <https://cli.github.com/manual/gh_config>.

- Display what Git protocol is being used:

`gh config get git_protocol`

- Set protocol to SSH:

`gh config set git_protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh</span>

- Use `delta` in side-by-side mode as the default pager for all `gh` commands:

`gh config set pager '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delta --side-by-side</span>`'`

- Set text editor to Vim:

`gh config set editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vim</span>

- Reset to default text editor:

`gh config set editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">""</span>

- Disable interactive prompts:

`gh config set prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disabled</span>

- Set a specific configuration value:

`gh config set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
