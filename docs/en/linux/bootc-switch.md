---
layout: page
title: linux/bootc-switch (English)
description: "Target a new container image reference to boot."
content_hash: 0f3a225347758a7bd820cfaf48e9791bed19a09c
last_modified_at: 2024-12-27
tldri18n_status: 2
---
# bootc switch

Target a new container image reference to boot.
More information: <https://containers.github.io/bootc/man/bootc-switch.html>.

- Change the base OS to a new container image from a registry:

`sudo bootc switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Change the base OS to a new container image from the local image storage of the root user:

`sudo bootc switch --transport containers-storage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Change the base OS to a new container image stored in a tarball:

`sudo bootc switch --transport oci-archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.tar.gz</span>
