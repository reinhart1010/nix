---
layout: page
title: common/cargo-package (한국어)
description: "로컬 패키지를 배포 가능한 tarball (`.crate` 파일)로 어셈블."
content_hash: e8057b431f0fc0ae834d8f20cdfd737b10ed09f3
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-package.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-package.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-package.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo package

로컬 패키지를 배포 가능한 tarball (`.crate` 파일)로 어셈블.
`cargo publish --dry-run`과 유사하지만, 더 많은 옵션이 있음.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-package.html>.

- 검사를 수행하고 `.crate` 파일을 생성 (`cargo publish --dry-run`과 동일):

`cargo package`

- 실제로 tarball을 생성하지 않고 tarball에 포함될 파일을 표시:

`cargo package --list`
