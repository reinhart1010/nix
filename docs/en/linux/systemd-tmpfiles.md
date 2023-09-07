---
layout: page
title: linux/systemd-tmpfiles (English)
description: "Create, delete and clean up volatile and temporary files and directories."
content_hash: 6bc9cdeb05d1ab48a35a0a8a8207129292a20446
last_modified_at: 2023-09-07
---
# systemd-tmpfiles

Create, delete and clean up volatile and temporary files and directories.
This command is automatically invoked on boot by systemd services, and running it manually is usually not needed.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-tmpfiles.html>.

- Create files and directories as specified in the configuration:

`systemd-tmpfiles --create`

- Clean up files and directories with age parameters configured:

`systemd-tmpfiles --clean`

- Remove files and directories as specified in the configuration:

`systemd-tmpfiles --remove`

- Apply operations for user-specific configurations:

`systemd-tmpfiles --create --user`

- Execute lines marked for early boot:

`systemd-tmpfiles --create --boot`
