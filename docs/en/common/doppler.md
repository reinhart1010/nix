---
layout: page
title: common/doppler (English)
description: "Manage environment variables across different environments using Doppler."
content_hash: b396bd41527b1e664d53e2b39d8587c18558aee6
last_modified_at: 2024-10-05
related_topics:
  - title: español version
    url: /es/common/doppler.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doppler

Manage environment variables across different environments using Doppler.
Some subcommands such as `run` and `secrets` have their own usage documentation.
More information: <https://docs.doppler.com/docs/cli>.

- Setup Doppler CLI in the current directory:

`doppler setup`

- Setup Doppler project and config in current directory:

`doppler setup`

- Run a command with secrets injected into the environment:

`doppler run --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- View your project list:

`doppler projects`

- View your secrets for current project:

`doppler secrets`

- Open Doppler dashboard in browser:

`doppler open`
