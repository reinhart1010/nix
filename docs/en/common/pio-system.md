---
layout: page
title: common/pio-system (English)
description: "Miscellaneous system commands for PlatformIO."
content_hash: 8d3de326d866373049403d505ec463ba85bf6809
last_modified_at: 2024-03-10
related_topics:
  - title: Nederlands version
    url: /nl/common/pio-system.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio system

Miscellaneous system commands for PlatformIO.
More information: <https://docs.platformio.org/en/latest/core/userguide/system/>.

- Install shell completion for the current shell (supports Bash, fish, Zsh and PowerShell):

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
