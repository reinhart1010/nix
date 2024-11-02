---
layout: page
title: windows/msedge (한국어)
description: "마이크로소프트에서 개발한 최신 웹 브라우저로, 구글에서 개발한 크로미움 웹 브라우저를 기반으로 합니다."
content_hash: 3f0ede9509a6266b6ea530d13e1c64938b24bf19
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/windows/msedge.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/msedge.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/msedge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># msedge

마이크로소프트에서 개발한 최신 웹 브라우저로, 구글에서 개발한 크로미움 웹 브라우저를 기반으로 합니다.
이 명령어는 다른 플랫폼에서는 `microsoft-edge`로 사용할 수 있습니다.
참고: `chromium`에서 추가 명령어 인수로 Microsoft Edge를 제어할 수 있습니다.
더 많은 정보: <https://microsoft.com/edge>.

- 특정 URL 또는 파일 열기:

`msedge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|경로\대상\파일.html</span>

- InPrivate 모드로 열기:

`msedge --inprivate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 새 창으로 열기:

`msedge --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 애플리케이션 모드로 열기 (도구 모음, URL 표시줄, 버튼 등 없음):

`msedge --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 프록시 서버 사용:

`msedge --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 사용자 데이터 디렉토리 사용:

`msedge --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>

- CORS 유효성 검사 없이 열기 (API 테스트에 유용):

`msedge --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>` --disable-web-security`

- 각 탭 열릴 때마다 DevTools 창 열기:

`msedge --auto-open-devtools-for-tabs`
