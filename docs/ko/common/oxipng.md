---
layout: page
title: common/oxipng (한국어)
description: "PNG 파일의 압축을 무손실로 개선합니다."
content_hash: 733f1801bf0b932d81e0405a098a4aecf58b84f1
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/oxipng.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/oxipng.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># oxipng

PNG 파일의 압축을 무손실로 개선합니다.
더 많은 정보: <https://github.com/shssoichiro/oxipng>.

- PNG 파일 압축 (기본적으로 파일을 덮어씀):

`oxipng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- PNG 파일을 압축하고 출력 파일을 새 파일로 저장:

`oxipng --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 현재 디렉토리의 모든 PNG 파일을 다중 스레드를 사용하여 압축:

`oxipng "*.png"`

- 설정된 최적화 레벨로 파일 압축 (기본값은 2):

`oxipng --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2|3|4|5|6|max</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- PNG 인터레이싱 유형 설정 (`0`은 인터레이싱 제거, `1`은 Adam7 인터레이싱 적용, `keep`은 기존 인터레이싱 유지; 기본값은 `0`):

`oxipng --interlace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|keep</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 알파 채널이 있는 이미지에 추가 최적화 수행:

`oxipng --alpha `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 더 느리지만 강력한 Zopfli 압축기를 최대 최적화로 사용:

`oxipng --zopfli --opt max `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 모든 비중요 메타데이터 청크 제거:

`oxipng --strip all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>
