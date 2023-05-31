---
layout: page
title: windows/diskpart (English)
description: "Disk, volume and partition manager."
content_hash: dc89a17a1caced97dbd7d3ff2c3ab59370bd93ee
last_modified_at: 2023-05-31
related_topics:
  - title: italiano version
    url: /it/windows/diskpart.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/diskpart.html
    icon: bi bi-globe
---
# diskpart

Disk, volume and partition manager.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- Run diskpart by itself in an administrative command prompt to enter its command-line:

`diskpart`

- List all disks:

`list disk`

- Select a volume:

`select volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume</span>

- Assign a drive letter to the selected volume:

`assign letter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">letter</span>

- Create a new partition:

`create partition primary`

- Activate the selected volume:

`active`

- Exit diskpart:

`exit`
