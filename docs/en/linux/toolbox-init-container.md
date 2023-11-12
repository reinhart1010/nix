---
layout: page
title: linux/toolbox-init-container (English)
description: "Initialize a running `toolbox` container."
content_hash: 1033eb06fd52069ac07cb3a4ecc85e545dc408f6
last_modified_at: 2023-11-12
related_topics:
  - title: தமிழ் version
    url: /ta/linux/toolbox-init-container.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox init-container

Initialize a running `toolbox` container.
This command should not be executed by the user, and cannot be run on the host.
More information: <https://manned.org/toolbox-init-container.1>.

- Initialize a running toolbox:

`toolbox init-container --gid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gid</span>` --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">home</span>` --home-link --media-link --mnt-link --monitor-host --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell</span>` --uid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>
