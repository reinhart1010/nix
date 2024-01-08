---
layout: page
title: common/gcloud (English)
description: "The official CLI tool for Google Cloud Platform."
content_hash: 01a584fce9d97f0a031fe99ae693b66230792e65
last_modified_at: 2024-01-08
related_topics:
  - title: dansk version
    url: /da/common/gcloud.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/gcloud.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/gcloud.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcloud

The official CLI tool for Google Cloud Platform.
Note: `gcloud` subcommands have their own usage documentation.
More information: <https://cloud.google.com/sdk/gcloud>.

- List all properties in one's active configuration:

`gcloud config list`

- Login to a Google account:

`gcloud auth login`

- Set the active project:

`gcloud config set project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- SSH into a virtual machine instance:

`gcloud compute ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance</span>

- Display all Google Compute Engine instances in a project (by default instances from all zones are listed):

`gcloud compute instances list`

- Update a kubeconfig file with the appropriate credentials to point `kubectl` to a specific cluster in Google Kubernetes Engine (GKE):

`gcloud container clusters get-credentials `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Update all `gcloud` components:

`gcloud components update`

- Display help for a given command:

`gcloud help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
