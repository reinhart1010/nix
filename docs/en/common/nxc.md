---
layout: page
title: common/nxc (English)
description: "Network service enumeration and exploitation tool."
content_hash: 2fcedced8ea5ced426349fdaaa35dbb863ffc61e
last_modified_at: 2024-08-10
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nxc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nxc

Network service enumeration and exploitation tool.
Some subcommands such as `nxc smb` have their own usage documentation.
More information: <https://www.netexec.wiki/>.

- [L]ist available modules for the specified protocol:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` -L`

- List the options available for the specified module:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>` --options`

- Specify an option for a module:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">OPTION_NAME</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option_value</span>

- View the options available for the specified protocol:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` --help`
