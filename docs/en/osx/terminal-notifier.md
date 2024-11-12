---
layout: page
title: osx/terminal-notifier (English)
description: "Send macOS User Notifications."
content_hash: 667ae801627faaf1b7592c19ff0c67a3a9f22bf9
last_modified_at: 2024-11-12
related_topics:
  - title: español version
    url: /es/osx/terminal-notifier.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/osx/terminal-notifier.html
    icon: bi bi-globe
tldri18n_status: 2
---
# terminal-notifier

Send macOS User Notifications.
More information: <https://github.com/julienXX/terminal-notifier>.

- Send a notification (only the message is required):

`terminal-notifier -group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tldr-info</span>` -title `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TLDR</span>` -message '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TLDR rocks</span>`'`

- Display piped data with a sound:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Piped Message Data!</span>`' | terminal-notifier -sound `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default</span>

- Open a URL when the notification is clicked:

`terminal-notifier -message '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Check your Apple stock!</span>`' -open '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://finance.yahoo.com/q?s=AAPL</span>`'`

- Open an app when the notification is clicked:

`terminal-notifier -message '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Imported 42 contacts.</span>`' -activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.AddressBook</span>
