---
layout: page
title: common/gh-config (English)
description: "Change configuration for GitHub cli."
content_hash: 131a4b5b65da7bda51160bcf491ab18a7f44082f
last_modified_at: 2024-12-05
related_topics:
  - title: 한국어 version
    url: /ko/common/gh-config.html
    icon: bi bi-globe
tldri18n_status: 2
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

`gh config set editor ""`

- Disable interactive prompts:

`gh config set prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disabled</span>

- Set a specific configuration value:

`gh config set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
