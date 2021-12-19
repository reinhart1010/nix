---
layout: page
title: osx/fsck (English)
description: "Check the integrity of a filesystem or repair it. The filesystem should be unmounted at the time the command is run."
content_hash: 45a3cd26a33377e3cbfd4ba96950b1d55839d474
related_topics:
  - title: 中文 version
    url: /zh/osx/fsck.html
    icon: bi bi-globe
---
# fsck

Check the integrity of a filesystem or repair it. The filesystem should be unmounted at the time the command is run.
It is a wrapper that calls `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat`, and `fsck_udf` as needed.
More information: <https://ss64.com/osx/fsck.html>.

- Check filesystem `/dev/sdX`, reporting any damaged blocks:

`fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Check filesystem `/dev/sdX` only if it is clean, reporting any damaged blocks and interactively letting the user choose to repair each one:

`fsck -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Check filesystem `/dev/sdX` only if it is clean, reporting any damaged blocks and automatically repairing them:

`fsck -fy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Check filesystem `/dev/sdX`, reporting whether it has been cleanly unmounted:

`fsck -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
