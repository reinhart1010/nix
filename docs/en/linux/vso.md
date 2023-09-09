---
layout: page
title: linux/vso (English)
description: "Package manager, system updater and a task automator for Vanilla OS."
content_hash: 67a664f98c2e89266f4322307fa93c0f829ccc49
last_modified_at: 2023-09-09
---
# vso

Package manager, system updater and a task automator for Vanilla OS.
More information: <https://github.com/Vanilla-OS/vanilla-system-operator>.

- Check for system updates to the host system:

`vso sys-upgrade check`

- Upgrade the host system now:

`vso sys-upgrade upgrade --now`

- Initialize the Pico subsystem (used for package management):

`vso pico-init`

- Install applications inside the subsystem:

`vso install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Remove applications from the subsystem:

`vso remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Enter the subsystem's shell:

`vso shell`

- Run an application from the subsystem:

`vso run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display VSO configuration:

`vso config show`
