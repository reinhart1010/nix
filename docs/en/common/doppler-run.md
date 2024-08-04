---
layout: page
title: common/doppler-run (English)
description: "Run a command with Doppler secrets injected into the environment."
content_hash: 430e463efe6a8b39de84672c85855799405e8a19
last_modified_at: 2024-08-04
tldri18n_status: 2
---
# doppler run

Run a command with Doppler secrets injected into the environment.
More information: <https://docs.doppler.com/docs/cli#run-a-command-with-secrets-populated-in-environment>.

- Run a command:

`doppler run --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run multiple commands:

`doppler run --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1 && command2</span>

- Run a script:

`doppler run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/command.sh</span>

- Run command with specified project and config:

`doppler run -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Automatically restart process when secrets change:

`doppler run --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
