---
layout: page
title: common/gcloud-logging-logs-list (English)
description: "List logs in a Google Cloud project."
content_hash: db78b1ef2612276676f9df172b286c2039c80a2d
last_modified_at: 2023-12-08
tldri18n_status: 2
---
# gcloud logging logs list

List logs in a Google Cloud project.
Useful for identifying available logs for monitoring and analysis. See also: `gcloud`.
More information: <https://cloud.google.com/sdk/gcloud/reference/logging/logs/list>.

- List all logs in the current project:

`gcloud logging logs list`

- List all logs for a specific log bucket and location:

`gcloud logging logs list --bucket=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_id</span>` --location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">location</span>

- List all logs for a specific view in a log bucket:

`gcloud logging logs list --bucket=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_id</span>` --location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">location</span>` --view=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">view_id</span>

- List logs with a filter expression:

`gcloud logging logs list --filter="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression</span>`"`

- List a specified number of logs:

`gcloud logging logs list --limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- List logs sorted by a specific field in ascending or descending order (`~` for descending):

`gcloud logging logs list --sort-by="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_name</span>`"`

- List logs sorted by multiple fields:

`gcloud logging logs list --sort-by="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field1</span>`,~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field2</span>`"`

- List logs with verbose output, showing additional details:

`gcloud logging logs list --verbosity=debug`
