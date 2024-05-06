---
layout: page
title: common/dart (English)
description: "Manage Dart projects."
content_hash: 038d010437df8366f0b7319d98424520202ac64b
last_modified_at: 2024-05-06
related_topics:
  - title: Deutsch version
    url: /de/common/dart.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/dart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dart

Manage Dart projects.
More information: <https://dart.dev/tools/dart-tool>.

- Initialize a new Dart project in a directory of the same name:

`dart create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Run a Dart file:

`dart run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.dart</span>

- Download dependencies for the current project:

`dart pub get`

- Run unit tests for the current project:

`dart test`

- Update an outdated project's dependencies to support null-safety:

`dart pub upgrade --null-safety`

- Compile a Dart file to a native binary:

`dart compile exe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.dart</span>

- Apply automated fixes to the current project:

`dart fix --apply`
