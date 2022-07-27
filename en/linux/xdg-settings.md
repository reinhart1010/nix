---
layout: page
title: linux/xdg-settings (English)
description: "Manage settings of XDG-compatible desktop environments."
content_hash: f4b6cee7d6b310136b2efa82bbfefa1c14ed5149
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xdg-settings

Manage settings of XDG-compatible desktop environments.
More information: <https://portland.freedesktop.org/doc/xdg-settings.html>.

- Print the default web browser:

`xdg-settings get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default-web-browser</span>

- Set the default web browser to Firefox:

`xdg-settings set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default-web-browser</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox.desktop</span>

- Set the default mail URL scheme handler to Evolution:

`xdg-settings set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default-url-scheme-handler</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mailto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">evolution.desktop</span>

- Set the default PDF document viewer:

`xdg-settings set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf-viewer.desktop</span>

- Display help:

`xdg-settings --help`
