---
layout: page
title: common/krunvm (English)
description: "CLI-based utility for creating MicroVMs from OCI images."
content_hash: 5b6a2cea756b1ed4a37f2faaeb8b28543ec18623
last_modified_at: 2022-12-09
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># krunvm

CLI-based utility for creating MicroVMs from OCI images.
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
