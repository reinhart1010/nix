---
layout: page
title: common/pulumi-stack (English)
description: "Manage stacks and view stack state."
content_hash: 728ba3267a02143dcc4a5651f22913a29f60b7dc
last_modified_at: 2024-10-09
tldri18n_status: 2
---
# pulumi stack

Manage stacks and view stack state.
More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_stack/>.

- Create a new stack:

`pulumi stack init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name</span>

- View the stack state:

`pulumi stack`

- List known stacks:

`pulumi stack ls`

- Select an active stack:

`pulumi stack select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name</span>

- Show stack outputs, including secrets, in plaintext:

`pulumi stack output --show-secrets`

- Export the stack state to a JSON file:

`pulumi stack export --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>

- Display help:

`pulumi stack --help`
