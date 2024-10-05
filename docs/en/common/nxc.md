---
layout: page
title: common/nxc (English)
description: "Network service enumeration and exploitation tool."
content_hash: dc6359a889bd342fdfb1f2ad3141ac0d266540fe
last_modified_at: 2024-10-05
related_topics:
  - title: español version
    url: /es/common/nxc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nxc

Network service enumeration and exploitation tool.
Some subcommands such as `smb` have their own usage documentation.
More information: <https://www.netexec.wiki/>.

- [L]ist available modules for the specified protocol:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` -L`

- List the options available for the specified module:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>` --options`

- Specify an option for a module:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">OPTION_NAME</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option_value</span>

- View the options available for the specified protocol:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` --help`
