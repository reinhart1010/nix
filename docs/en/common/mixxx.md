---
layout: page
title: common/mixxx (English)
description: "Free and open source cross-platform DJ software."
content_hash: 80302e19434b9bb853425fa55497f6228c91a118
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# mixxx

Free and open source cross-platform DJ software.
More information: <https://mixxx.org/manual/latest/chapters/appendix.html#command-line-options>.

- Start the Mixxx GUI in fullscreen:

`mixxx --fullScreen`

- Start in safe developer mode to debug a crash:

`mixxx --developer --safeMode`

- Debug a malfunction:

`mixxx --debugAssertBreak --developer --loglevel trace`

- Start Mixxx using the specified settings file:

`mixxx --resourcePath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mixxx/res/controllers</span>` --settingsPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/settings-file</span>

- Debug a custom controller mapping:

`mixxx --controllerDebug --resourcePath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mapping-directory</span>

- Display help:

`mixxx --help`
