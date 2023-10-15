---
layout: page
title: common/az-devops (English)
description: "Manage Azure DevOps organizations."
content_hash: 26f45452d3d77addfcc81143b97d2f6d76cc3b23
last_modified_at: 2023-10-15
related_topics:
  - title: español version
    url: /es/common/az-devops.html
    icon: bi bi-globe
---
# az devops

Manage Azure DevOps organizations.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/devops>.

- Set the Personal Access Token (PAT) to login to a particular organization:

`az devops login --organization `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_url</span>

- Open a project in the browser:

`az devops project show --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` --open`

- List members of a specific team working on a particular project:

`az devops team list-member --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` --team `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">team_name</span>

- Check the Azure DevOps CLI current configuration:

`az devops configure --list`

- Configure the Azure DevOps CLI behavior by setting a default project and a default organization:

`az devops configure --defaults project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` organization=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization_url</span>
