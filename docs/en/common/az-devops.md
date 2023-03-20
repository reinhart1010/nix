---
layout: page
title: common/az-devops (English)
description: "Manage Azure DevOps organizations."
content_hash: e91b4fc0d5d79e37137a45fbd0ce5b7f287d9814
last_modified_at: 2023-03-20
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># az devops

Manage Azure DevOps organizations.
Part of `azure-cli`.
More information: <https://learn.microsoft.com/en-us/cli/azure/devops?view=azure-cli-latest>.

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
