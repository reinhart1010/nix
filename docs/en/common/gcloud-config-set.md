---
layout: page
title: common/gcloud-config-set (English)
description: "Set a property in the Google Cloud CLI configuration."
content_hash: 5cea5bb6dcdbc94114f5bd3392eb0b2e06aee3d4
last_modified_at: 2023-12-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcloud-config-set.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcloud config set

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
