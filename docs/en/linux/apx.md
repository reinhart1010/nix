---
layout: page
title: linux/apx (English)
description: "Package management utility."
content_hash: 45b81e231172065a1f874536a2ccee148e3d4498
last_modified_at: 2023-03-11
related_topics:
  - title: தமிழ் version
    url: /ta/linux/apx.html
    icon: bi bi-globe
---
# apx

Package management utility.
Install packages inside managed containers from multiple sources (`apx` supports --aur,--dnf, --apk flags in all commands).
More information: <https://github.com/Vanilla-OS/apx>.

- Initialize or reinitialize a specific container:

`apx init`

- Install specific packages in the container:

`apx install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Install a DEB/RPM package inside the container (Use `--dnf` flag for installing RPMs):

`apx install --sideload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package</span>

- Remove specific packages from the container:

`apx remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Search for specific packages:

`apx search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Enter the managed container shell to execute commands (type `exit` to exit the container):

`apx enter`

- Update the list of available packages in the container:

`apx update`

- Upgrade all installed packages in the container to their newest available version:

`apx upgrade`
