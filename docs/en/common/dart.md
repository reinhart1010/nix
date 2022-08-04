---
layout: page
title: common/dart (English)
description: "The tool for managing Dart projects."
content_hash: d4f64d217f26238d27399c0bd1de5ec808a7f1ca
---
# dart

The tool for managing Dart projects.
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
