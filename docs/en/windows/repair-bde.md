---
layout: page
title: windows/repair-bde (English)
description: "Attempt to repair or decrypt a damaged BitLocker-encrypted volume."
content_hash: a96b07d6a107b349b1f514e601f3141559d19f5e
last_modified_at: 2024-01-30
related_topics:
  - title: 中文 version
    url: /zh/windows/repair-bde.html
    icon: bi bi-globe
tldri18n_status: 2
---
# repair-bde

Attempt to repair or decrypt a damaged BitLocker-encrypted volume.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/repair-bde>.

- Attempt to repair a specified volume:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>

- Attempt to repair a specified volume and output to another volume:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">D:</span>

- Attempt to repair a specified volume using the provided recovery key file:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -RecoveryKey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.bek</span>

- Attempt to repair a specified volume using the provided numerical recovery password:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -RecoveryPassword `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Attempt to repair a specified volume using the provided password:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -Password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Attempt to repair a specified volume using the provided key package:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -KeyPackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- Log all output to a specific file:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -LogFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>

- Display help:

`repair-bde /?`
