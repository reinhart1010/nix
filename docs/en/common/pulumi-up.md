---
layout: page
title: common/pulumi-up (English)
description: "Create or update the resources in a stack."
content_hash: e01feb15556a29ff4e6e839a104db37515818da4
last_modified_at: 2024-09-12
tldri18n_status: 2
---
# pulumi up

Create or update the resources in a stack.
More information: <https://www.pulumi.com/docs/cli/commands/pulumi_up/>.

- Preview and deploy changes to a program and/or infrastructure:

`pulumi up`

- Automatically approve and perform the update after previewing it:

`pulumi up --yes`

- Preview and deploy changes in a specific stack:

`pulumi up --stack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack</span>

- Don't display stack outputs:

`pulumi up --suppress-outputs`

- Continue updating the resources, even if an error is encountered:

`pulumi up --continue-on-error`
