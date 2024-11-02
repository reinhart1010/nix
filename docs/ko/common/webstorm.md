---
layout: page
title: common/webstorm (한국어)
description: "JetBrains JavaScript IDE."
content_hash: 1cf0c0cc96db3028733321efe640625316c5a382
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/webstorm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/webstorm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># webstorm

JetBrains JavaScript IDE.
더 많은 정보: <https://www.jetbrains.com/help/webstorm/working-with-the-ide-features-from-command-line.html>.

- 현재 디렉토리를 WebStorm에서 열기:

`webstorm`

- 특정 디렉토리를 WebStorm에서 열기:

`webstorm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 파일들을 LightEdit 모드에서 열기:

`webstorm -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 파일을 LightEdit 모드에서 열고 편집이 완료될 때까지 대기:

`webstorm --wait -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 줄에 커서를 두고 파일 열기:

`webstorm --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">줄_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 열고 비교 (최대 3개 파일 지원):

`webstorm diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 경로/대상/선택_파일3</span>

- 3방향 병합 수행하기:

`webstorm merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/왼쪽_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오른쪽_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_파일</span>
