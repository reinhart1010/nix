---
layout: page
title: osx/pmset (English)
description: "Configure macOS power management settings, as one might do in System Preferences > Energy Saver."
content_hash: 476c803502af9a8fee4f5fb905836a51e66a6400
last_modified_at: 2024-01-31
related_topics:
  - title: 中文 version
    url: /zh/osx/pmset.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pmset

Configure macOS power management settings, as one might do in System Preferences > Energy Saver.
Commands that modify settings must begin with `sudo`.
More information: <https://keith.github.io/xcode-man-pages/pmset.1.html>.

- Display the current power management settings:

`pmset -g`

- Display the current power source and battery levels:

`pmset -g batt`

- Put display to sleep immediately:

`pmset displaysleepnow`

- Set display to never sleep when on charger power:

`sudo pmset -c displaysleep 0`

- Set display to sleep after 15 minutes when on battery power:

`sudo pmset -b displaysleep 15`

- Schedule computer to automatically wake up every weekday at 9 AM:

`sudo pmset repeat wake MTWRF 09:00:00`

- Restore to system defaults:

`sudo pmset -a displaysleep 10 disksleep 10 sleep 30 womp 1`
