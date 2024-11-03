---
layout: page
title: common/weasyprint (한국어)
description: "HTML을 PDF 또는 PNG로 렌더링."
content_hash: 3afda5cb37e6c5661a199eabc49bd7ce838d01d9
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/weasyprint.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/weasyprint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# weasyprint

HTML을 PDF 또는 PNG로 렌더링.
더 많은 정보: <https://weasyprint.org/>.

- HTML 파일을 PDF로 렌더링:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>

- 추가 사용자 스타일시트를 포함하여 HTML 파일을 PNG로 렌더링:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>` --stylesheet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스타일시트.css</span>

- 렌더링 시 추가 디버깅 정보 출력:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>` --verbose`

- PNG로 출력할 때 사용자 지정 해상도 지정:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>` --resolution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>

- 입력 HTML 파일의 상대 URL에 대한 기본 URL 지정:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>` --base-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_또는_파일_이름</span>
