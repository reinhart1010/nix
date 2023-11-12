---
layout: page
title: linux/mmdebstrap (English)
description: "Create a Debian chroot."
content_hash: b655220316ff3b15212045829f1c98cdbaae17fc
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mmdebstrap

Create a Debian chroot.
Alternative to `debootstrap`.
More information: <https://gitlab.mister-muffin.de/josch/mmdebstrap/>.

- Create a Debian Stable directory chroot:

`sudo mmdebstrap stable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/debian-root/</span>

- Create a Debian Bookworm tarball chroot using a mirror:

`mmdebstrap bookworm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/debian-bookworm.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://mirror.example.org/debian</span>

- Create a Debian Sid tarball chroot with additional packages:

`mmdebstrap sid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/debian-sid.tar</span>` --include=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkg1,pkg2</span>
