---
layout: page
title: common/pulumi-config (English)
description: "Manage configuration of a Pulumi stack."
content_hash: 5b5e72b160434f32a459cef48669898dd0a4124b
last_modified_at: 2024-11-28
tldri18n_status: 2
---
# pulumi config

Manage configuration of a Pulumi stack.
More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_config/>.

- View current configuration in JSON format:

`pulumi config --json`

- Get the value of a configuration key:

`pulumi config get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Remove a configuration value:

`pulumi config rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Set a value for a configuration key from a file:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | pulumi config set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Set a secret value (e.g. API key) for a configuration key and store/display as ciphertext:

`pulumi config set --secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">S3cr37_value</span>

- Remove multiple configuration values from a specified configuration file:

`pulumi config --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` rm-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key1 key2 ...</span>
