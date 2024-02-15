---
layout: page
title: common/doctl-apps (English)
description: "Manage DigitalOcean apps."
content_hash: 1afefa870d9bd78b6c188bbde47fece34e3b1804
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# doctl apps

Manage DigitalOcean apps.
More information: <https://docs.digitalocean.com/reference/doctl/reference/apps>.

- Create an app:

`doctl apps create`

- Create a deployment for a specific app:

`doctl apps create-deployment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Delete an app interactively:

`doctl apps delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Get an app:

`doctl apps get`

- List all apps:

`doctl apps list`

- List all deployments from a specific app:

`doctl apps list-deployments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Get logs from a specific app:

`doctl apps logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Update a specific app with a given app spec:

`doctl apps update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>` --spec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/spec.yml</span>
