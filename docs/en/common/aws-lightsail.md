---
layout: page
title: common/aws-lightsail (English)
description: "Manage Amazon Lightsail resources using the CLI."
content_hash: 4eff3e76e2d91371bee54177358c7b8420c39e4b
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws lightsail

Manage Amazon Lightsail resources using the CLI.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html>.

- List all virtual private servers, or instances:

`aws lightsail get-instances`

- List all bundles (instance plans):

`aws lightsail list-bundles`

- List all available instance images, or blueprints:

`aws lightsail list-blueprints`

- Create an instance:

`aws lightsail create-instances --instance-names `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --availability-zone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>` --bundle-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nano_2_0</span>` --blueprint-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blueprint_id</span>

- Print the state of a specific instance:

`aws lightsail get-instance-state --instance-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Stop a specific instance:

`aws lightsail stop-instance --instance-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Delete a specific instance:

`aws lightsail delete-instance --instance-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
