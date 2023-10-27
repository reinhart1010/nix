---
layout: page
title: windows/uwfmgr (English)
description: "Unified Write Filter (UWF)."
content_hash: 77975890934a57e4a6eb9d1b36d3ff6fd8372bed
last_modified_at: 2023-10-27
---
# uwfmgr

Unified Write Filter (UWF).
Protect drives by redirecting any writes to the drive to a virtual overlay. Writes are discarded upon reboot unless committed by default.
More information: <https://learn.microsoft.com/windows/iot/iot-enterprise/customize/unified-write-filter>.

- Get the current status:

`uwfmgr get-config`

- Set a drive as protected:

`uwfmgr volume protect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">drive_letter</span>`:`

- Remove a drive from protection list:

`uwfmgr volume unprotect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">drive_letter</span>`:`

- Enable or disable protection (Applies after reboot):

`uwfmgr filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>

- Commit changes of a file on protected drive:

`uwfmgr file commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">drive_letter:\path\to\file</span>

- Commit deletion of a file on protected drive:

`uwfmgr file commit-delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">drive_letter:\path\to\file</span>
