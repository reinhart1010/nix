---
layout: page
title: windows/test-netconnection (English)
description: "Display diagnostic information for a connection."
content_hash: 557486458d9de0e4547c11bcbab9cb4f16edb90b
last_modified_at: 2024-04-21
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/test-netconnection.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Test-NetConnection

Display diagnostic information for a connection.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection>.

- Test a connection and display detailed results:

`Test-NetConnection -InformationLevel Detailed`

- Test a connection to a remote host using the specified port number:

`Test-NetConnection -ComputerName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_hostname</span>` -Port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>
