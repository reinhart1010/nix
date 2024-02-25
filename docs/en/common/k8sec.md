---
layout: page
title: common/k8sec (English)
description: "Manage Kubernetes secrets."
content_hash: 15a0849db67fe8153b386bf89ea21543ae1dbd56
last_modified_at: 2024-02-25
tldri18n_status: 2
---
# k8sec

Manage Kubernetes secrets.
More information: <https://github.com/dtan4/k8sec>.

- List all secrets:

`k8sec list`

- List a specific secret as a base64-encoded string:

`k8sec list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name</span>` --base64`

- Set a secret's value:

`k8sec set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key=value</span>

- Set a base64-encoded value:

`k8sec set --base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key=encoded_value</span>

- Unset a secret:

`k8sec unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name</span>

- Load secrets from a file:

`k8sec load -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name</span>

- Dump secrets to a file:

`k8sec dump -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_name</span>
