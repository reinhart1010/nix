---
layout: page
title: linux/grub-mkconfig (English)
description: "Generate a GRUB configuration file."
content_hash: daea240831383e0f52063e4fb0012066e6b694e9
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/linux/grub-mkconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/grub-mkconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grub-mkconfig

Generate a GRUB configuration file.
More information: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dmkconfig.html>.

- Do a dry run and print the configuration to `stdout`:

`sudo grub-mkconfig`

- Generate the configuration file:

`sudo grub-mkconfig --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/boot/grub/grub.cfg</span>

- Print the help page:

`grub-mkconfig --help`
