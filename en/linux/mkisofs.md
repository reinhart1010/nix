---
layout: page
title: linux/mkisofs (English)
description: "Create ISO files from directories."
content_hash: 78b030cb875c64eb6a1511e888aafeda6efd9caf
---
# mkisofs

Create ISO files from directories.
Also aliased as `genisoimage`.
More information: <https://manned.org/mkisofs>.

- Create an ISO from a directory:

`mkisofs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_directory</span>

- Set the disc label when creating an ISO:

`mkisofs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.iso</span>` -V "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_name</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_directory</span>
