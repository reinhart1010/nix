---
layout: page
title: common/spicetify (English)
description: "A CLI utility to customize the Spotify client UI and functionality."
content_hash: 13858f67eee3da2a2f861a7ab326d9db0121b9ac
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># spicetify

A CLI utility to customize the Spotify client UI and functionality.
More information: <https://spicetify.app>.

- Generate a configuration file on very first run and display help:

`spicetify`

- Backup and preprocess Spotify application files:

`spicetify backup`

- Print all configuration fields and values:

`spicetify config`

- Change the value of a configuration field:

`spicetify config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Apply the customization changes to Spotify:

`spicetify apply`

- Restore Spotify to its original state:

`spicetify restore`
