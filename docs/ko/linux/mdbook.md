---
layout: page
title: linux/mdbook (한국어)
description: "Markdown 파일을 작성하여 온라인 책을 만듭니다."
content_hash: 06b129f9ee89d18f4cde80f7c99b3983429885ca
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mdbook.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mdbook.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mdbook

Markdown 파일을 작성하여 온라인 책을 만듭니다.
더 많은 정보: <https://rust-lang.github.io/mdBook/>.

- 현재 디렉토리에 mdbook 프로젝트 생성:

`mdbook init`

- 특정 디렉토리에 mdbook 프로젝트 생성:

`mdbook init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 생성된 책이 있는 디렉토리 정리:

`mdbook clean`

- <http://localhost:3000>에서 책 제공, 파일 변경 시 자동 빌드:

`mdbook serve`

- Markdown 파일 세트를 감시하고 파일이 변경될 때 자동으로 빌드:

`mdbook watch`
