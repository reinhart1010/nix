---
layout: page
title: common/qutebrowser (English)
description: "A keyboard-driven, vim-like browser based on PyQt5."
content_hash: ace802246a75dec584e6d25131643428df25bba3
---
# qutebrowser

A keyboard-driven, vim-like browser based on PyQt5.
More information: <https://qutebrowser.org/>.

- Open qutebrowser with a specified storage directory:

`qutebrowser --basedir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Open a qutebrowser instance with temporary settings:

`qutebrowser --set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">content.geolocation</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true|false</span>

- Restore a named session of a qutebrowser instance:

`qutebrowser --restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name</span>

- Launch qutebrowser, opening all URLs using the specified method:

`qutebrowser --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto|tab|tab-bg|tab-silent|tab-bg-silent|window|private-window</span>

- Open qutebrowser with a temporary base directory and print logs to stdout as JSON:

`qutebrowser --temp-basedir --json-logging`
