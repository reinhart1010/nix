---
layout: page
title: common/az-repos (English)
description: "Manage Azure DevOps repos."
content_hash: 34e6794f245e6acc4d302cc0e999bc8bd3fb36c9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# az repos

Manage Azure DevOps repos.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/repos>.

- List all repos in a specific project:

`az repos list --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Add policy on a specific branch of a specific repository to restrict basic merge:

`az repos policy merge-strategy create --repository-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_id_in_repos_list</span>` --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>` --blocking --enabled --allow-no-fast-forward false --allow-rebase true --allow-rebase-merge true --allow-squash true`

- Add build validation on a specific repository, using an existing build pipeline, to be triggered automatically on source update:

`az repos policy build create --repository-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_id</span>` --build-definition-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">build_pipeline_id</span>` --branch main --blocking --enabled --queue-on-source-update-only true --display-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --valid-duration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutes</span>

- List all active Pull Requests on a specific repository within a specific project:

`az repos pr list --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>` --status active`
