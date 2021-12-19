---
layout: page
title: linux/kreadconfig5 (English)
description: "Read KConfig entries for KDE Plasma."
content_hash: a86fcd4b3e73fc93a5ef62aa38f24a6a7e4b7476
---
# kreadconfig5

Read KConfig entries for KDE Plasma.
More information: <https://userbase.kde.org/KDE_System_Administration/Configuration_Files>.

- Read a key from the global configuration:

`kreadconfig5 --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>

- Read a key from a specific configuration file:

`kwriteconfig5 --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_name</span>

- Check if systemd is used to start the Plasma session:

`kreadconfig5 --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">startkderc</span>` --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">General</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">systemdBoot</span>
