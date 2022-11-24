---
layout: page
title: common/k3d (English)
description: "Wrapper CLI to easily create k3s clusters inside Docker."
content_hash: 72f7823f49af02da0259940df4103bb55945d221
last_modified_at: 2022-11-24
---
# k3d

Wrapper CLI to easily create k3s clusters inside Docker.
More information: <https://k3d.io>.

- Create a cluster:

`k3d cluster create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Delete a cluster:

`k3d cluster delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Create a new containerized k3s node:

`k3d node create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>

- Import an image from Docker into a k3d cluster:

`k3d image import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>` --cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Create a new registry:

`k3d registry create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry_name</span>
