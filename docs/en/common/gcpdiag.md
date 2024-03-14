---
layout: page
title: common/gcpdiag (English)
description: "Google Cloud Platform troubleshooting and diagnostics tool."
content_hash: 057dc96a5775e8360f2ce05faf784790268e9004
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# gcpdiag

Google Cloud Platform troubleshooting and diagnostics tool.
Run in a Docker container or in GCP Cloudshell.
More information: <https://github.com/GoogleCloudPlatform/gcpdiag>.

- Run `gcpdiag` on your project, returning all rules:

`gcpdiag lint --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcp_project_id</span>

- Hide rules that are ok:

`gcpdiag lint --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcp_project_id</span>` --hide-ok`

- Authenticate using a service account private key file:

`gcpdiag lint --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcp_project_id</span>` --auth-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/private_key</span>

- Search logs and metrics from a number of days back (default: 3 days):

`gcpdiag lint --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcp_project_id</span>` --within-days `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Display help:

`gcpdiag lint --help`
