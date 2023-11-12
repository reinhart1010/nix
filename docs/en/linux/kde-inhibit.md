---
layout: page
title: linux/kde-inhibit (English)
description: "Inhibit various desktop functions while a command runs."
content_hash: 6426616be46eb5306475382d26f5c0afe260c6df
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kde-inhibit

Inhibit various desktop functions while a command runs.
More information: <https://invent.kde.org/plasma/kde-cli-tools/-/blob/master/kdeinhibit/main.cpp>.

- Inhibit power management:

`kde-inhibit --power `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Inhibit screen saver:

`kde-inhibit --screenSaver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Launch VLC, and inhibit color correction (night mode) while it's running:

`kde-inhibit --colorCorrect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vlc</span>
