---
layout: page
title: common/krunvm (English)
description: "Create MicroVMs from OCI images."
content_hash: f4f116d53a3800e825ccba8b0ec3411ac5ce2383
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/krunvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# krunvm

Create MicroVMs from OCI images.
More information: <https://github.com/containers/krunvm>.

- Create MicroVM based on Fedora:

`krunvm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker.io/fedora</span>` --cpus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_vcpus</span>` --mem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">memory_in_megabytes</span>` --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`"`

- Start a specific image:

`krunvm start "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>`"`

- List images:

`krunvm list`

- Change a specific image:

`krunvm changevm --cpus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_vcpus</span>` --mem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">memory_in_megabytes</span>` --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_vm_name</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">current_vm_name</span>`"`

- Delete a specific image:

`krunvm delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_name</span>`"`
