---
layout: page
title: common/fdroid (English)
description: "F-Droid build tool."
content_hash: 652313250542d945f7758be2623b4227e998911a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/fdroid.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fdroid

F-Droid build tool.
F-Droid is an installable catalog of FOSS (Free and Open Source Software) applications for the Android platform.
More information: <https://f-droid.org/>.

- Build a specific app:

`fdroid build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Build a specific app in a build server VM:

`fdroid build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>` --server`

- Publish the app to the local repository:

`fdroid publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Install the app on every connected device:

`fdroid install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Check if the metadata is formatted correctly:

`fdroid lint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>

- Fix the formatting automatically (if possible):

`fdroid rewritemeta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_id</span>
