---
layout: page
title: common/od (한국어)
description: "파일 내용을 8진수, 10진수 또는 16진수 형식으로 표시."
content_hash: f2dee21f7dc533c85df6875a2c44d091e930a982
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/od.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/od.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/od.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># od

파일 내용을 8진수, 10진수 또는 16진수 형식으로 표시.
선택적으로 각 줄에 대한 바이트 오프셋 및/또는 인쇄 가능한 표현을 표시.
더 많은 정보: <https://www.gnu.org/software/coreutils/od>.

- 기본 설정으로 파일 표시: 8진수 형식, 8바이트 단위로 줄바꿈, 8진수 바이트 오프셋, 중복 줄은 `*`로 대체:

`od `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 자세한 모드로 파일 표시, 즉 중복 줄을 `*`로 대체하지 않음:

`od -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 16진수 형식(2바이트 단위)으로 파일 표시, 10진수 형식의 바이트 오프셋:

`od --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>` --address-radix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 16진수 형식(1바이트 단위)으로 파일 표시, 4바이트 단위로 줄바꿈:

`od --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x1</span>` --width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 16진수 형식과 문자 표현으로 파일 표시, 바이트 오프셋은 출력하지 않음:

`od --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xz</span>` --address-radix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 500번째 바이트부터 시작하여 파일의 100바이트만 읽기:

`od --read-bytes 100 --skip-bytes=500 -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
