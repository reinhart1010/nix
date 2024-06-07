---
layout: page
title: windows/test-netconnection (English)
description: "Display diagnostic information for a connection."
content_hash: 82eb821536aac28ba2b0548a84468eb5019da8db
last_modified_at: 2024-06-07
related_topics:
  - title: español version
    url: /es/windows/test-netconnection.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Test-NetConnection

Display diagnostic information for a connection.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection>.

- Test a connection and display detailed results:

`Test-NetConnection -InformationLevel Detailed`

- Test a connection to a remote host using the specified port number:

`Test-NetConnection -ComputerName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_hostname</span>` -Port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>
