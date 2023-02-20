---
layout: page
title: windows/sfc (English)
description: "Scans the integrity of Windows system files."
content_hash: d482e70711a17f7db8c5497606fc92381cae859f
last_modified_at: 2023-02-20
related_topics:
  - title: 中文 version
    url: /zh/windows/sfc.html
    icon: bi bi-globe
---
# sfc

Scans the integrity of Windows system files.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/sfc>.

- Display information about the usage of the command:

`sfc`

- Scan all system files and, if possible, repair any problems:

`sfc /scannow`

- Scan all system files without attempting to repair any:

`sfc /verifyonly`

- Scan a specific file and, if possible, repair any problems:

`sfc /scanfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>

- Scan a specific file without attempting to repair it:

`sfc /verifyfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>

- When repairing offline, specify the boot directory:

`sfc /offbootdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- When repairing offline, specify the Windows directory:

`sfc /offwindir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>
