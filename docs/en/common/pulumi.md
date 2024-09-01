---
layout: page
title: common/pulumi (English)
description: "Define infrastructure on any cloud using familiar programming languages."
content_hash: 650b9218e40a5a3ce19518dc2676c36dc6c19ad8
last_modified_at: 2024-09-01
tldri18n_status: 2
---
# pulumi

Define infrastructure on any cloud using familiar programming languages.
Some subcommands such as `pulumi up` have their own usage documentation.
More information: <https://www.pulumi.com/docs/cli>.

- Create a new project using a template:

`pulumi new`

- Create a new stack using an isolated deployment target:

`pulumi stack init`

- Configure variables (e.g. keys, regions, etc.) interactively:

`pulumi config`

- Preview and deploy changes to a program and/or infrastructure:

`pulumi up`

- Preview deployment changes without performing them (dry-run):

`pulumi preview`

- Destroy a program and its infrastructure:

`pulumi destroy`

- Use Pulumi locally, independent of a Pulumi Cloud:

`pulumi login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--local</span>
