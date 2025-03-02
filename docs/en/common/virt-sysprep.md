---
layout: page
title: common/virt-sysprep (English)
description: "Reset, unconfigure, or customize a virtual machine image."
content_hash: cf9ef70ae2545077156aab495a9437308829fb36
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/virt-sysprep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virt-sysprep

Reset, unconfigure, or customize a virtual machine image.
More information: <https://manned.org/virt-sysprep>.

- List all supported operations (enabled operations are indicated with asterisks):

`virt-sysprep --list-operations`

- Remove sensitive system data from a virtual machine image:

`sudo virt-sysprep --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.qcow2</span>

- Specify a virtual machine by its name and run all enabled operations but don't actually apply the changes:

`sudo virt-sysprep --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --dry-run`

- Run only the specified operations:

`sudo virt-sysprep --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --operations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">operation1,operation2,...</span>

- Generate a new `/etc/machine-id` file and enable customizations to be able to change the host name to avoid network conflicts:

`sudo virt-sysprep --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_name</span>` --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">customizations</span>` --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_name</span>` --operation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">machine-id</span>
