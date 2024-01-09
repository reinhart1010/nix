---
layout: page
title: common/gcloud-projects (English)
description: "Manage project access policies in Google Cloud."
content_hash: ae188b2310ef76382c10c7f4affcfc8e3510fb43
last_modified_at: 2024-01-09
tldri18n_status: 2
---
# gcloud projects

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
