---
layout: page
title: linux/systemd-sysusers (English)
description: "Create system users and groups."
content_hash: e79d5f1cb5ef1dd60c67217cd618a68ea120f22e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# systemd-sysusers

Create system users and groups.
If the config file is not specified, files in the `sysusers.d` directories are used.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-sysusers.html>.

- Create users and groups from a specific configuration file:

`systemd-sysusers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Process configuration files and print what would be done without actually doing anything:

`systemd-sysusers --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print the contents of all config files (before each file, its name is printed as a comment):

`systemd-sysusers --cat-config`
