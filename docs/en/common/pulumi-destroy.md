---
layout: page
title: common/pulumi-destroy (English)
description: "Destroy all existing resources in a stack."
content_hash: a25cc3fb16b02b0f3d30430efc8744e13c6e66d9
last_modified_at: 2024-09-15
tldri18n_status: 2
---
# pulumi destroy

Destroy all existing resources in a stack.
More information: <https://www.pulumi.com/docs/cli/commands/pulumi_destroy/>.

- Destroy all resources in the current stack:

`pulumi destroy`

- Destroy all resources in a specific stack:

`pulumi destroy --stack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack</span>

- Automatically approve and destroy resources after previewing:

`pulumi destroy --yes`

- Exclude protected resources from being destroyed:

`pulumi destroy --exclude-protected`

- Remove the stack and its configuration file after all resources in the stack are deleted:

`pulumi destroy --remove`

- Continue destroying the resources, even if an error is encountered:

`pulumi destroy --continue-on-error`
