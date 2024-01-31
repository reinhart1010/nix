---
layout: page
title: common/gcloud-components-install (English)
description: "Install specific components of the Google Cloud CLI, along with their dependencies."
content_hash: 0b8665d9fb88bca6141fad2f21f89a26e6844138
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# gcloud components install

Install specific components of the Google Cloud CLI, along with their dependencies.
Installs components at the current version of the Google Cloud CLI without upgrading the existing installation.
More information: <https://cloud.google.com/sdk/gcloud/reference/components/install>.

- View available components for installation:

`gcloud components list`

- Install one or more components (installs any dependencies as well):

`gcloud components install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_id1 component_id2 ...</span>

- Check the current version of Google Cloud CLI:

`gcloud version`

- Update Google Cloud CLI to the latest version:

`gcloud components update`
