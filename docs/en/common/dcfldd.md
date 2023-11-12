---
layout: page
title: common/dcfldd (English)
description: "Enhanced version of dd for forensics and security."
content_hash: e0ba8b242d55f80990b0a8f4b56454287778756b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dcfldd

Enhanced version of dd for forensics and security.
More information: <http://dcfldd.sourceforge.net/>.

- Copy a disk to a raw image file and hash the image using SHA256:

`dcfldd if=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disk_device</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.img</span>` hash=sha256 hashlog=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hash</span>

- Copy a disk to a raw image file, hashing each 1 GB chunk:

`dcfldd if=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disk_device</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.img</span>` hash=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha512|sha384|sha256|sha1|md5</span>` hashlog=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hash</span>` hashwindow=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1G</span>
