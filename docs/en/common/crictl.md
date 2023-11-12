---
layout: page
title: common/crictl (English)
description: "Command-line for CRI-compatible container runtimes."
content_hash: 5a528ac7509dd3f050666bab071aca24233d155b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# crictl

Command-line for CRI-compatible container runtimes.
More information: <https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md>.

- List all kubernetes pods (Ready and NotReady):

`crictl pods`

- List all containers (Running and Exited):

`crictl ps --all`

- List all images:

`crictl images`

- Print information about specific containers:

`crictl inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_id1 container_id2 ...</span>

- Open a specific shell inside a running container:

`crictl exec -it `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- Pull a specific image from a registry:

`crictl pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image:tag</span>

- Print and [f]ollow logs of a specific container:

`crictl logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_id</span>

- Remove one or more images:

`crictl rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_id1 image_id2 ...</span>
