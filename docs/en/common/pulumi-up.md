---
layout: page
title: common/pulumi-up (English)
description: "Create or update the resources in a stack."
content_hash: 9924d64ed8cc7f86a050f921a5792130b469dd14
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/pulumi-up.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pulumi up

Create or update the resources in a stack.
More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_up/>.

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
