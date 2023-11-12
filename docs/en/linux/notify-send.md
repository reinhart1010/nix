---
layout: page
title: linux/notify-send (English)
description: "Uses the current desktop environment's notification system to create a notification."
content_hash: 3d0d0607496a97f9aa72d4311f0bafea53cd44be
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# notify-send

Uses the current desktop environment's notification system to create a notification.
More information: <https://manned.org/notify-send>.

- Show a notification with the title "Test" and the content "This is a test":

`notify-send "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Test</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">This is a test</span>`"`

- Show a notification with a custom icon:

`notify-send -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">icon.png</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Test</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">This is a test</span>`"`

- Show a notification for 5 seconds:

`notify-send -t 5000 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Test</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">This is a test</span>`"`

- Show a notification with an app's icon and name:

`notify-send "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Test</span>`" --icon=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">google-chrome</span>` --app-name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Google Chrome</span>`"`
