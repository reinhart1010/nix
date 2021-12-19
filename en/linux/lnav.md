---
layout: page
title: linux/lnav (English)
description: "Advanced log file viewer to analyze logs with little to no setup."
content_hash: 485b977693564762338debbaa17ee23cedb5d5ae
---
# lnav

Advanced log file viewer to analyze logs with little to no setup.
More information: <https://docs.lnav.org/en/latest/cli.html>.

- View logs of a program, specifying log files, directories or URLs:

`lnav `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/log_or_directory|url</span>

- View logs of a specific remote host (SSH passwordless login required):

`lnav `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host1.example.com</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/syslog.log</span>

- Validate the format of log files against the configuration and report any errors:

`lnav -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/log_directory</span>
