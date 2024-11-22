---
layout: page
title: common/pulumi-new (English)
description: "Create a new Pulumi project."
content_hash: 2e2186c15ad964c42c16283cdbd6b8f0c582a25b
last_modified_at: 2024-11-22
tldri18n_status: 2
---
# pulumi new

Create a new Pulumi project.
More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_new/>.

- Choose a template interactively:

`pulumi new`

- Create a project from a specific template (e.g `azure-python`):

`pulumi new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">provided-template</span>

- Create a project from a local file:

`pulumi new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/templates/aws-typescript</span>

- Create a project from a Git repository:

`pulumi new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Use the specified secrets provider with the <pulumi.com> backend:

`pulumi new --secrets-provider=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passphrase</span>
