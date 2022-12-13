---
layout: page
title: linux/apx (English)
description: "Package management utility for Vanilla OS."
content_hash: 7b22baa50417106a01c28bf413c26ef7b0795cf3
last_modified_at: 2022-12-13
related_topics:
  - title: தமிழ் version
    url: /ta/linux/apx.html
    icon: bi bi-globe
---
# apx

Package management utility for Vanilla OS.
Install packages inside managed containers from multiple sources (`apx` supports --aur,--dnf flags in all commands).
More information: <https://github.com/Vanilla-OS/apx>.

- Initialize the container:

`apx init`

- Install specific packages in the container:

`apx install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

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
