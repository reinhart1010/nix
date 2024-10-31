---
layout: page
title: common/pulumi-stack (English)
description: "Manage stacks and view stack state."
content_hash: f09c1dc0beac5932fbd365f9254d8d9341d48647
last_modified_at: 2024-10-31
tldri18n_status: 2
---
# pulumi stack

Manage stacks and view stack state.
More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_stack/>.

- Create a new stack:

`pulumi stack init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name</span>

- View the stack state:

`pulumi stack`

- List stacks in the current project:

`pulumi stack ls`

- List stacks across all projects:

`pulumi stack ls --all`

- Select an active stack:

`pulumi stack select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name</span>

- Show stack outputs, including secrets, in plaintext:

`pulumi stack output --show-secrets`

- Export the stack state to a JSON file:

`pulumi stack export --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>

- Display help:

`pulumi stack --help`
