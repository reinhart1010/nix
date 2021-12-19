---
layout: page
title: linux/xtrlock (English)
description: "Lock the X display until the user supplies their password."
content_hash: 689148845c38712d708514117660dc74de402925
---
# xtrlock

Lock the X display until the user supplies their password.

- Lock the display and show a padlock instead of the cursor:

`xtrlock`

- Display a blank screen as well as the padlock cursor:

`xtrlock -b`

- Fork the xtrlock process and return immediately:

`xtrlock -f`
