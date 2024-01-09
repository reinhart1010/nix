---
layout: page
title: common/gcloud-iam (English)
description: "Configure Identity and Access Management (IAM) preferences and service accounts."
content_hash: 6cfc7c89f9f88c3d1e398b2fc99446c06d032677
last_modified_at: 2024-01-09
tldri18n_status: 2
---
# gcloud iam

Configure Identity and Access Management (IAM) preferences and service accounts.
See also: `gcloud`.
More information: <https://cloud.google.com/sdk/gcloud/reference/iam>.

- List IAM grantable roles for a resource:

`gcloud iam list-grantable-roles `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource</span>

- Create a custom role for a organization or project:

`gcloud iam roles create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_name</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization|project</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organization|project_id</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/role.yaml</span>

- Create a service account for a project:

`gcloud iam service-accounts create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Add an IAM policy binding to a service account:

`gcloud iam service-accounts add-iam-policy-binding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_account_email</span>` --member `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">member</span>` --role `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role</span>

- Replace existing IAM policy binding:

`gcloud iam service-accounts set-iam-policy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_account_email</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">policy_file</span>

- List a service account's keys:

`gcloud iam service-accounts keys list --iam-account `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_account_email</span>
