---
layout: page
title: linux/update-alternatives (English)
description: "Convenientily maintain symbolic links to determine default commands."
content_hash: 78b05f71938561e91765b5bd76e119d11869985b
last_modified_at: 2024-02-25
related_topics:
  - title: Nederlands version
    url: /nl/linux/update-alternatives.html
    icon: bi bi-globe
tldri18n_status: 2
---
# update-alternatives

Convenientily maintain symbolic links to determine default commands.
More information: <https://manned.org/update-alternatives>.

- Add a symbolic link:

`sudo update-alternatives --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/symlink</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/command_binary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>

- Configure a symbolic link for `java`:

`sudo update-alternatives --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>

- Remove a symbolic link:

`sudo update-alternatives --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/opt/java/jdk1.8.0_102/bin/java</span>

- Display information about a specified command:

`update-alternatives --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>

- Display all commands and their current selection:

`update-alternatives --get-selections`
