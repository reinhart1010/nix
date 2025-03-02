---
layout: page
title: common/pulumi-env (English)
description: "Manage Pulumi environments."
content_hash: cbe1a55d2dc488181b139d5373b8dbe2ff516af8
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/pulumi-env.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pulumi env

Manage Pulumi environments.
More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_env/>.

- List all environments:

`pulumi env ls`

- Create an environment:

`pulumi env init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>

- Set a value in an environment:

`pulumi env set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Edit an environment definition:

`pulumi env edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>

- Delete a value from an environment:

`pulumi env rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Delete an environment entirely:

`pulumi env rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>

- Display help:

`pulumi env --help`
