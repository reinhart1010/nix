---
layout: page
title: common/pio-system (English)
description: "Miscellaneous system commands for PlatformIO."
content_hash: c3fca4873a3437d9de2c53aa06e09350d903a7b0
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pio system

Miscellaneous system commands for PlatformIO.
More information: <https://docs.platformio.org/en/latest/core/userguide/system/>.

- Install shell completion for the current shell (supports Bash, Fish, Zsh and PowerShell):

`pio system completion install`

- Uninstall shell completion for the current shell:

`pio system completion uninstall`

- Display system-wide PlatformIO information:

`pio system info`

- Remove unused PlatformIO data:

`pio system prune`

- Remove only cached data:

`pio system prune --cache`

- List unused PlatformIO data that would be removed but do not actually remove it:

`pio system prune --dry-run`
