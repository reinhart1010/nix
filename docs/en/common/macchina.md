---
layout: page
title: common/macchina (English)
description: "Display information about your computer."
content_hash: 663f88af505005e21d4508525f2376e84807ab2a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# macchina

Display information about your computer.
More information: <https://github.com/Macchina-CLI/macchina>.

- List out system information, with either default settings or those specified in your configuration file:

`macchina`

- Specify a custom configuration file path:

`macchina --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/configuration_file</span>

- List system information, but lengthen uptime, shell and kernel output:

`macchina --long-uptime --long-shell --long-kernel`

- Check for any errors/system failures encountered when trying to fetch system information:

`macchina --doctor`

- List original artists of all the ASCII art:

`macchina --ascii-artists`
