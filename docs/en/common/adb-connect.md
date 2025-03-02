---
layout: page
title: common/adb-connect (English)
description: "Connect to an Android device wirelessly."
content_hash: b69deb555376d2e56f3febf9684163b4daad92cf
last_modified_at: 2025-03-02
tldri18n_status: 2
---
# adb connect

Connect to an Android device wirelessly.
More information: <https://developer.android.com/tools/adb>.

- Pair with an Android device (address and pairing code can be found in developer options):

`adb pair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Connect to an Android device (port will be different from pairing):

`adb connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Disconnect a device:

`adb disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>
