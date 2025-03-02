---
layout: page
title: common/pulumi-stack (English)
description: "Manage stacks and view stack state."
content_hash: 54188b023a06db90ef1e1204e9cd2f438b0f5d7b
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/pulumi-stack.html
    icon: bi bi-globe
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

- Delete a stack:

`pulumi stack rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name</span>

- Show stack outputs, including secrets, in plaintext:

`pulumi stack output --show-secrets`

- Export the stack state to a JSON file:

`pulumi stack export --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>
