---
layout: page
title: linux/notify-send (English)
description: "Uses the current desktop environment's notification system to create a notification."
content_hash: f19588697013a36be87e3ae74af5a2498e0e4098
---
# notify-send

Uses the current desktop environment's notification system to create a notification.

- Show a notification with the title "Test" and the content "This is a test":

`notify-send "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Test</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">This is a test</span>`"`

- Show a notification with a custom icon:

`notify-send -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">icon.png</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Test</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">This is a test</span>`"`

- Show a notification for 5 seconds:

`notify-send -t 5000 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Test</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">This is a test</span>`"`

- Show a notification with an app's icon and name:

`notify-send "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Test</span>`" --icon=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">google-chrome</span>` --app-name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Google Chrome</span>`"`
