---
layout: page
title: common/gcloud-config-set (English)
description: "Set a property in the Google Cloud CLI configuration."
content_hash: 5cea5bb6dcdbc94114f5bd3392eb0b2e06aee3d4
last_modified_at: 2023-12-08
tldri18n_status: 2
---
# gcloud config set

Set a property in the Google Cloud CLI configuration.
Properties control various aspects of Google Cloud CLI behavior.
More information: <https://cloud.google.com/sdk/gcloud/reference/config/set>.

- Set the project property in the core section:

`gcloud config set project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_id</span>

- Set the compute zone for future operations:

`gcloud config set compute/zone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone_name</span>

- Disable prompting to make gcloud suitable for scripting:

`gcloud config set disable_prompts true`

- View the list of properties currently in use:

`gcloud config list`

- Unset a previously set property:

`gcloud config unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">property_name</span>

- Create a new configuration profile:

`gcloud config configurations create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_name</span>

- Switch between different configuration profiles:

`gcloud config configurations activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_name</span>
