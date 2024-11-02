---
layout: page
title: common/wget2 (한국어)
description: "웹에서 파일을 다운로드하기 위한 개선된 `wget` 버전."
content_hash: bff018d554ec5d740722905b689ef4cf79bc7644
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/wget2.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wget2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wget2

웹에서 파일을 다운로드하기 위한 개선된 `wget` 버전.
HTTP, HTTPS 및 HTTP/2 프로토콜을 지원하며 성능이 향상되었습니다.
기본적으로 `wget2`는 더 빠른 다운로드를 위해 여러 스레드를 사용합니다.
더 많은 정보: <https://gitlab.com/gnuwget/wget2>.

- 여러 스레드를 사용하여 URL의 내용을 파일로 다운로드 (기본 동작이 `wget`과 다릅니다):

`wget2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- 다운로드에 사용할 스레드 수 제한 (기본값은 5 스레드):

`wget2 --max-threads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- 단일 웹 페이지와 모든 리소스(스크립트, 스타일시트, 이미지 등) 다운로드:

`wget2 --page-requisites --convert-links `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepage.html</span>

- 웹사이트를 미러링하되 상위 디렉토리로 올라가지 않음 (내장 페이지 요소는 다운로드하지 않음):

`wget2 --mirror --no-parent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepath/</span>

- 다운로드 속도와 연결 재시도 횟수 제한:

`wget2 --limit-rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300k</span>` --tries=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepath/</span>

- 불완전한 다운로드 계속 (동작이 `wget`과 일치):

`wget2 --continue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 텍스트 파일에 저장된 모든 URL을 특정 디렉토리에 다운로드:

`wget2 --directory-prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --input-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URLs.txt</span>

- HTTP 서버에서 Basic Auth를 사용하여 파일 다운로드 (HTTPS에도 작동):

`wget2 --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>
