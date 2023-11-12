---
layout: page
title: common/virt-sparsify (English)
description: "Make virtual machine drive images thin-provisioned."
content_hash: 0e7255742082888d032f0acfd66776f890545a37
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# virt-sparsify

Make virtual machine drive images thin-provisioned.
NOTE: Use only for offline machines to avoid data corruption.
More information: <https://libguestfs.org>.

- Create a sparsified compressed image without snapshots from an unsparsified one:

`virt-sparsify --compress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.qcow2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_new.qcow2</span>

- Sparsify an image in-place:

`virt-sparsify --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.img</span>
