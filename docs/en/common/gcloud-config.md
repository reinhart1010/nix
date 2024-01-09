---
layout: page
title: common/gcloud-config (English)
description: "Manage different configurations of `gcloud`."
content_hash: d7e07dfcd8a26dd5bc5563d3b2f3643cc6673873
last_modified_at: 2024-01-09
tldri18n_status: 2
---
# gcloud config

Manage different configurations of `gcloud`.
See also: `gcloud`.
More information: <https://cloud.google.com/sdk/gcloud/reference/config>.

- Define a property (like compute/zone) for the current configuration:

`gcloud config set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">property</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Fetch the value of a `gcloud` property:

`gcloud config get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">property</span>

- Display all the properties for the current configuration:

`gcloud config list`

- Create a new configuration with a given name:

`gcloud config configurations create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_name</span>

- Display a list of all available configurations:

`gcloud config configurations list`

- Switch to an existing configuration with a given name:

`gcloud config configurations activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_name</span>
