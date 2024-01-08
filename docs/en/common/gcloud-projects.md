---
layout: page
title: common/gcloud-projects (English)
description: "Manage project access policies in Google Cloud."
content_hash: ae188b2310ef76382c10c7f4affcfc8e3510fb43
last_modified_at: 2024-01-08
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcloud-projects.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcloud projects

Manage project access policies in Google Cloud.
See also: `gcloud`.
More information: <https://cloud.google.com/sdk/gcloud/reference/projects>.

- Create a new project:

`gcloud projects create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_id|project_number</span>

- List all active projects:

`gcloud projects list`

- Display metadata for a project:

`gcloud projects describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_id</span>

- Delete a project:

`gcloud projects delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_id|project_number</span>

- Add an IAM policy binding to a specified project:

`gcloud projects add-iam-policy-binding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_id</span>` --member `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">principal</span>` --role `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role</span>
