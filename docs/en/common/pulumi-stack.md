---
layout: page
title: common/pulumi-stack (English)
description: "Manage stacks and view stack state."
content_hash: 728ba3267a02143dcc4a5651f22913a29f60b7dc
last_modified_at: 2024-10-08
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pulumi-stack.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pulumi stack

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
