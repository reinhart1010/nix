---
layout: page
title: common/jmtpfs (English)
description: "FUSE-based filesystem for accessing MTP devices."
content_hash: 87e39ed2c21249661a6c9141715707d8f08a87cd
---
# jmtpfs

FUSE-based filesystem for accessing MTP devices.
More information: <https://manned.org/jmtpfs>.

- Mount an MTP device to a directory:

`jmtpfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Set mount options:

`jmtpfs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">allow_other,auto_unmount</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- List available MTP devices:

`jmtpfs --listDevices`

- If multiple devices are present, mount a specific device:

`jmtpfs -device=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus_id</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Unmount MTP device:

`fusermount -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
