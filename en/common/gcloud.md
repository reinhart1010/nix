---
layout: page
title: common/gcloud (English)
description: "The official CLI tool for Google Cloud Platform."
content_hash: 84cf69bea3e6f1f1e3a42693bbce30a40d294762
---
# gcloud

The official CLI tool for Google Cloud Platform.
More information: <https://cloud.google.com/sdk/gcloud>.

- List all properties in one's active configuration:

`gcloud config list`

- Log in to Google account:

`gcloud auth login`

- Set the active project:

`gcloud config set project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- SSH into a virtual machine instance:

`gcloud compute ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance</span>` `

- Display all Google Compute Engine instances in a project. Instances from all zones are listed by default:

`gcloud compute instances list`

- Update a kubeconfig file with the appropriate credentials to point kubectl to a specific cluster in Google Kubernetes Engine:

`gcloud container clusters get-credentials `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Update all gcloud CLI components:

`gcloud components update`

- Show help for a given command:

`gcloud help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
