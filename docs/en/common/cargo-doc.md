---
layout: page
title: common/cargo-doc (English)
description: "Build the documentation of Rust packages."
content_hash: 8188707bff514815a1dbdc6623be17d6590a040b
last_modified_at: 2023-10-30
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-doc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-doc.html
    icon: bi bi-globe
---
# cargo doc

Build the documentation of Rust packages.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Build the documentation for the current project and all dependencies:

`cargo doc`

- Do not build documentation for dependencies:

`cargo doc --no-deps`

- Build and open the documentation in a browser:

`cargo doc --open`

- Build and view the documentation of a particular package:

`cargo doc --open --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
