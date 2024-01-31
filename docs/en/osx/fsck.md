---
layout: page
title: osx/fsck (English)
description: "Check the integrity of a filesystem or repair it. The filesystem should be unmounted at the time the command is run."
content_hash: 17a43c9b7805e0726f3db4bd18b93efd64ddceb1
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/fsck.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/fsck.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/fsck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fsck

Check the integrity of a filesystem or repair it. The filesystem should be unmounted at the time the command is run.
It is a wrapper that calls `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat`, and `fsck_udf` as needed.
More information: <https://keith.github.io/xcode-man-pages/fsck.8.html>.

- Check filesystem `/dev/sdX`, reporting any damaged blocks:

`fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Check filesystem `/dev/sdX` only if it is clean, reporting any damaged blocks and interactively letting the user choose to repair each one:

`fsck -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Check filesystem `/dev/sdX` only if it is clean, reporting any damaged blocks and automatically repairing them:

`fsck -fy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Check filesystem `/dev/sdX`, reporting whether it has been cleanly unmounted:

`fsck -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
