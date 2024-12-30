---
layout: page
title: common/apkeep (English)
description: "Download APK files from various sources."
content_hash: 2ee9c5529cf1992a80c29f337d7c554611b40b05
last_modified_at: 2024-12-30
tldri18n_status: 2
---
# apkeep

Download APK files from various sources.
More information: <https://github.com/EFForg/apkeep>.

- Download an APK file to the specified directory:

`apkeep --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.application</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- List all available versions for download:

`apkeep --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.application</span>` --list-versions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Specify a store to download from:

`apkeep --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.application</span>` --download-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apk-pure|google-play|f-droid|huawei-app-gallery</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
