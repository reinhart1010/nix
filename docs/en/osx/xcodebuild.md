---
layout: page
title: osx/xcodebuild (English)
description: "Build Xcode projects."
content_hash: 9d8dbc8d867f9bcc763622e35cf02ec9eefb1a4f
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/xcodebuild.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/xcodebuild.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcodebuild

Build Xcode projects.
More information: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Build workspace:

`xcodebuild -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workspace_name.workspace</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scheme_name</span>` -configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_name</span>` clean build SYMROOT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SYMROOT_path</span>

- Build project:

`xcodebuild -target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>` -configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_name</span>` clean build SYMROOT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SYMROOT_path</span>

- Show SDKs:

`xcodebuild -showsdks`
