---
layout: page
title: common/pulumi-state (English)
description: "Edit the current stack's state."
content_hash: 4c303dab7006a18b4132aa3583d9f88b966d3406
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/pulumi-state.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pulumi state

Edit the current stack's state.
More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_state/>.

- Delete a resource from the current stack's state:

`pulumi state delete`

- Move a resource from the current stack to another:

`pulumi state move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_urn</span>` --dest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name</span>

- Rename a resource in the current stack's state:

`pulumi state rename`

- Repair an invalid state:

`pulumi state repair`

- Edit a stack's state in the editor specified by the `EDITOR` environment variable:

`pulumi state edit --stack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name</span>

- Display help:

`pulumi state --help`
