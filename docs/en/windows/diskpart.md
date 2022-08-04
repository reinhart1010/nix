---
layout: page
title: windows/diskpart (English)
description: "Disk, volume and partition manager."
content_hash: c617f46a30c2c4b8aa50c1c27407a8936fc83ce5
---
# diskpart

Disk, volume and partition manager.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- Run diskpart by itself in an administrative command prompt to enter its command line:

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
