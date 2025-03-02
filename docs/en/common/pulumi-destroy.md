---
layout: page
title: common/pulumi-destroy (English)
description: "Destroy all existing resources in a stack."
content_hash: 50e8f19f814c222d04ed2d9e068fabd5e2f45400
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/pulumi-destroy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pulumi destroy

Destroy all existing resources in a stack.
More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_destroy/>.

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
