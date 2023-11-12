---
layout: page
title: common/oc (English)
description: "The OpenShift Container Platform CLI."
content_hash: 6e435679a0662190bc1deadf4e8ab6564bd26b85
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# oc

The OpenShift Container Platform CLI.
Allows for application and container management.
More information: <https://docs.openshift.com/container-platform/3.11/cli_reference/get_started_cli.html>.

- Log in to the OpenShift Container Platform server:

`oc login`

- Create a new project:

`oc new-project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Switch to an existing project:

`oc project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Add a new application to a project:

`oc new-app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_url</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application</span>

- Open a remote shell session to a container:

`oc rsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- List pods in a project:

`oc get pods`

- Log out from the current session:

`oc logout`
