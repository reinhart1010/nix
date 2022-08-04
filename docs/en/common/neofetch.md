---
layout: page
title: common/neofetch (English)
description: "CLI tool to display information about your operating system, software and hardware."
content_hash: 02a4f9e622313bb6654f162523430bee99a09ff8
related_topics:
  - title: italiano version
    url: /it/common/neofetch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/neofetch.html
    icon: bi bi-globe
---
# neofetch

CLI tool to display information about your operating system, software and hardware.
More information: <https://github.com/dylanaraps/neofetch>.

- Return the default config, and create it if it's the first time the program runs:

`neofetch`

- Trigger an info line from appearing in the output, where 'infoname' is the function name in the config file, e.g. memory:

`neofetch --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">infoname</span>

- Hide/Show OS architecture:

`neofetch --os_arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Enable/Disable CPU brand in output:

`neofetch --cpu_brand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>
