---
layout: page
title: linux/eww (English)
description: "Implement your own custom widgets in any window manager."
content_hash: b95d72a82a6d717c6039dba46216a967a6c25327
last_modified_at: 2024-11-19
tldri18n_status: 2
---
# eww

Implement your own custom widgets in any window manager.
More information: <https://elkowar.github.io/eww>.

- Start the daemon:

`eww daemon`

- Open a widget:

`eww -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_code_directory</span>` open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">window_name</span>

- Close a widget:

`eww -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_code_directory</span>` close `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">window_name</span>

- Reload the configuration:

`eww reload`

- Kill the daemon:

`eww kill`

- Print and watch logs:

`eww logs`
