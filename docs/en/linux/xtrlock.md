---
layout: page
title: linux/xtrlock (English)
description: "Lock the X display until the user supplies their password."
content_hash: 4243bba4be048dcc2878d8bf0e771bc134a853d3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xtrlock

Lock the X display until the user supplies their password.
More information: <https://manned.org/xtrlock>.

- Lock the display and show a padlock instead of the cursor:

`xtrlock`

- Display a blank screen as well as the padlock cursor:

`xtrlock -b`

- Fork the xtrlock process and return immediately:

`xtrlock -f`
