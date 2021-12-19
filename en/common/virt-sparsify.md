---
layout: page
title: common/virt-sparsify (English)
description: "Make virtual machine drive images thin-provisioned."
content_hash: d6564a1ae8f24af6feccc0a0451a2133b71d59b8
---
# virt-sparsify

Make virtual machine drive images thin-provisioned.
NOTE: Use only for offline machines to avoid data corruption.
Home page: <https://libguestfs.org/>.

- Create a sparsified compressed image without snapshots from an unsparsified one:

`virt-sparsify --compress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.qcow2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_new.qcow2</span>

- Sparsify an image in-place:

`virt-sparsify --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.img</span>
