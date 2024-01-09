---
layout: page
title: common/gcloud-auth (English)
description: "Grant and revoke authorization to `gcloud` and manage credentials."
content_hash: 253810a97922547642723215f77752f39dd3125b
last_modified_at: 2024-01-09
tldri18n_status: 2
---
# gcloud auth

Grant and revoke authorization to `gcloud` and manage credentials.
See also: `gcloud`.
More information: <https://cloud.google.com/sdk/gcloud/reference/auth>.

- Authorize Google Cloud access for the `gcloud` CLI with Google Cloud user credentials and set the current account as active:

`gcloud auth login`

- Authorize Google Cloud access similar to `gcloud auth login` but with service account credentials:

`gcloud auth activate-service-account`

- Manage Application Default Credentials (ADC) for Cloud Client Libraries:

`gcloud auth application-default`

- Display a list of Google Cloud accounts currently authenticated on your system:

`gcloud auth list`

- Display the current account's access token:

`gcloud auth print-access-token`

- Remove access credentials for an account:

`gcloud auth revoke`
