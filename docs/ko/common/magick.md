---
layout: page
title: common/magick (한국어)
description: "이미지 형식 간 변환, 편집, 합성 또는 변환."
content_hash: ceca22c5e7434cf9a57b194d8cc1f1f9069d6f56
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/magick.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/magick.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># magick

이미지 형식 간 변환, 편집, 합성 또는 변환.
이 도구는 ImageMagick 7+에서 `convert`를 대체합니다. 7+ 버전에서 이전 도구를 사용하려면 `magick convert`를 참조하세요.
`mogrify`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://imagemagick.org>.

- 이미지 형식 간 변환:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_이미지.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_이미지.jpg</span>

- 이미지를 크기 조정하여 새 복사본 만들기:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_이미지.jpg</span>` -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100x100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_이미지.jpg</span>

- 현재 디렉토리의 모든 JPEG 이미지로 GIF 생성:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.gif</span>

- 체커보드 패턴 생성:

`magick -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480</span>` pattern:checkerboard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/체커보드.png</span>

- 현재 디렉토리의 모든 JPEG 이미지로 PDF 파일 생성:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` -adjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>
