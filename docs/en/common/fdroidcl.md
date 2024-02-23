---
layout: page
title: common/fdroidcl (English)
description: "Manage F-Droid apps of devices connected via ADB."
content_hash: c5f7b96178a8444ead41321c9e4c39dbc3705649
last_modified_at: 2024-02-23
related_topics:
  - title: Deutsch version
    url: /de/common/fdroidcl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fdroidcl

Manage F-Droid apps of devices connected via ADB.
More information: <https://github.com/mvdan/fdroidcl>.

- Fetch the F-Droid index:

`fdroidcl update`

- Display information about an app:

`fdroidcl show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Download the APK file of an app:

`fdroidcl download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Search for an app in the index:

`fdroidcl search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>

- Install an app on a connected device:

`fdroidcl install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Add a repository:

`fdroidcl repo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Remove, enable or disable a repository:

`fdroidcl repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remove|enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_name</span>
