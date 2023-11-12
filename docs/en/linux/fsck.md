---
layout: page
title: linux/fsck (English)
description: "Check the integrity of a filesystem or repair it. The filesystem should be unmounted at the time the command is run."
content_hash: 7c8da085585609da40e62e66cf6eb4aa8d18a224
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/linux/fsck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fsck

Check the integrity of a filesystem or repair it. The filesystem should be unmounted at the time the command is run.
More information: <https://manned.org/fsck>.

- Check filesystem `/dev/sdXN`, reporting any damaged blocks:

`sudo fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Check filesystem `/dev/sdXN`, reporting any damaged blocks and interactively letting the user choose to repair each one:

`sudo fsck -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Check filesystem `/dev/sdXN`, reporting any damaged blocks and automatically repairing them:

`sudo fsck -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
