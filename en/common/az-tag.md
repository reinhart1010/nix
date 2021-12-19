---
layout: page
title: common/az-tag (English)
description: "Manage tags on a resource."
content_hash: 34a1d313ce5da55e2ed3dbe42d8eee2b6e1b3ca9
---
# az tag

Manage tags on a resource.
Part of `azure-cli`.
More information: <https://docs.microsoft.com/cli/azure/tag>.

- Create a tag value:

`az tag add-value --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>` --value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_value</span>

- Create a tag in the subscription:

`az tag create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>

- Delete a tag from the subscription:

`az tag delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>

- List all tags on a subscription:

`az tag list --resource-id /subscriptions/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subscription_id</span>

- Delete a tag value for a specific tag name:

`az tag remove-value --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>` --value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_value</span>
