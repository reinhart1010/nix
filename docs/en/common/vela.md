---
layout: page
title: common/vela (English)
description: "Command-line tools for the Vela pipeline."
content_hash: b40435bb7ff0d072336ad298c298740f0d91d7d7
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# vela

Command-line tools for the Vela pipeline.
More information: <https://go-vela.github.io/docs/reference/cli/>.

- Trigger a pipeline to run from a Git branch, commit or tag:

`vela add deployment --org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>` --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment</span>` --ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch|commit|refs/tags/git_tag</span>` --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deploy_description</span>`"`

- List deployments for a repository:

`vela get deployment --org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>` --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>

- Inspect a specific deployment:

`vela view deployment --org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization</span>` --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>` --deployment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment_number</span>
