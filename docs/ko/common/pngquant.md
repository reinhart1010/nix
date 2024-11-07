---
layout: page
title: common/pngquant (한국어)
description: "PNG 변환기 및 손실 이미지 압축기."
content_hash: de81d78513d2c0ec2d1f7fea1802aca1a3357211
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pngquant.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pngquant.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pngquant

PNG 변환기 및 손실 이미지 압축기.
더 많은 정보: <https://pngquant.org/>.

- 특정 PNG를 최대한 압축하고 결과를 새 파일로 저장:

`pngquant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 특정 PNG를 압축하고 원본을 덮어쓰기:

`pngquant --ext .png --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 사용자 지정 품질로 특정 PNG를 압축 시도 (최소 값보다 낮으면 건너뜀):

`pngquant --quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0-100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 색상이 64개로 줄어진 특정 PNG를 압축:

`pngquant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">64</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 특정 PNG를 압축하고 파일이 원본보다 큰 경우 건너뜀:

`pngquant --skip-if-larger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 특정 PNG를 압축하고 메타데이터 제거:

`pngquant --strip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 특정 PNG를 압축하고 지정된 경로에 저장:

`pngquant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 특정 PNG를 압축하고 진행 상황 표시:

`pngquant --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>
