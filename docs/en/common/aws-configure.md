---
layout: page
title: common/aws-configure (English)
description: "Manage configuration for the AWS CLI."
content_hash: 85f7d6724d51343670f0d4c131497a570d3909f9
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/aws-configure.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/aws-configure.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-configure.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws configure

Manage configuration for the AWS CLI.
More information: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- Configure AWS CLI interactively (creates a new configuration or updates the default):

`aws configure`

- Configure a named profile for AWS CLI interactively (creates a new profile or updates an existing one):

`aws configure --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Display the value from a specific configuration variable:

`aws configure get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Display the value for a configuration variable in a specific profile:

`aws configure get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Set the value of a specific configuration variable:

`aws configure set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Set the value of a configuration variable in a specific profile:

`aws configure set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- List the configuration entries:

`aws configure list`

- List the configuration entries for a specific profile:

`aws configure list --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>
