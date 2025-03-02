---
layout: page
title: common/pulumi (English)
description: "Define infrastructure on any cloud using familiar programming languages."
content_hash: f79c5b08b698300b048e418350ce6265b4208c3a
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/pulumi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pulumi

Define infrastructure on any cloud using familiar programming languages.
Some subcommands such as `up` have their own usage documentation.
More information: <https://www.pulumi.com/docs/iac/cli/>.

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
