---
layout: page
title: common/gcloud-app (English)
description: "Build scalable applications on a managed serverless platform."
content_hash: 0691883d17ec2a0d4b76afed78760f0f5273aaa9
last_modified_at: 2024-01-08
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcloud-app.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcloud app

Build scalable applications on a managed serverless platform.
See also: `gcloud`.
More information: <https://cloud.google.com/sdk/gcloud/reference/app>.

- Deploy an app's code and configuration to the App Engine server:

`gcloud app deploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployables</span>

- List all versions of all services deployed to the App Engine server:

`gcloud app versions list`

- Open the current app in a web browser:

`gcloud app browse`

- Create an App Engine app within the current project:

`gcloud app create`

- Display the latest App Engine app logs:

`gcloud app logs read`
