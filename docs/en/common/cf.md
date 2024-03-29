---
layout: page
title: common/cf (English)
description: "Manage apps and services on Cloud Foundry."
content_hash: a05de7095dd61ab6ca72294db1673d84ed1ab88c
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# cf

Manage apps and services on Cloud Foundry.
More information: <https://docs.cloudfoundry.org>.

- Log in to the Cloud Foundry API:

`cf login -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_url</span>

- Push an app using the default settings:

`cf push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- View the services available from your organization:

`cf marketplace`

- Create a service instance:

`cf create-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plan</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Connect an application to a service:

`cf bind-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>

- Run a script whose code is included in the app, but runs independently:

`cf run-task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script_command</span>`" --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>

- Start an interactive SSH session with a VM hosting an app:

`cf ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- View a dump of recent app logs:

`cf logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>` --recent`
