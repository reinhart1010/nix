---
layout: page
title: common/aws-lightsail (English)
description: "Manage Amazon Lightsail resources."
content_hash: 338a72a79f2efe587e6349b2eae00b1e9296b482
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# aws lightsail

Manage Amazon Lightsail resources.
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
