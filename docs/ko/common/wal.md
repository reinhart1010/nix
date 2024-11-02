---
layout: page
title: common/wal (한국어)
description: "배경화면의 주요 색상을 기반으로 색상 테마 생성."
content_hash: b1c84d56691fdfc8cbb91a5065a87171137b7c4e
last_modified_at: 2024-11-02
related_topics:
  - title: català version
    url: /ca/common/wal.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/wal.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wal.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wal

배경화면의 주요 색상을 기반으로 색상 테마 생성.
더 많은 정보: <https://github.com/dylanaraps/pywal>.

- 색상 테마 미리보기:

`wal --preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.png</span>

- 색상 테마 생성:

`wal -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.png</span>

- 밝은 색상 테마 생성:

`wal -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.png</span>` -l`

- 데스크탑 배경화면 설정 건너뛰기:

`wal -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.png</span>` -n`

- 터미널 색상 설정 건너뛰기:

`wal -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.png</span>` -s`

- 이전에 생성된 색상 테마와 배경화면 복원:

`wal -R`
