---
layout: page
title: common/flutter (English)
description: "Google's free, open source, and cross-platform mobile app SDK."
content_hash: 538fe7ff62207bba53cb11d98937a1ceb3da4626
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/flutter.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/flutter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flutter

Google's free, open source, and cross-platform mobile app SDK.
Some subcommands such as `flutter pub` have their own usage documentation.
More information: <https://github.com/flutter/flutter/wiki/The-flutter-tool>.

- Initialize a new Flutter project in a directory of the same name:

`flutter create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Check if all external tools are correctly installed:

`flutter doctor`

- List or change Flutter channel:

`flutter channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|beta|dev|master</span>

- Run Flutter on all started emulators and connected devices:

`flutter run -d all`

- Run tests in a terminal from the root of the project:

`flutter test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test/example_test.dart</span>

- Build a release APK targeting most modern smartphones:

`flutter build apk --target-platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android-arm</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android-arm64</span>

- Display help about a specific command:

`flutter help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
