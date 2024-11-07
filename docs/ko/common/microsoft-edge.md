---
layout: page
title: common/microsoft-edge (한국어)
description: "Google에서 개발한 Chromium 웹 브라우저를 기반으로 Microsoft가 개발한 현대적인 웹 브라우저."
content_hash: 0d537d2d8ff0b276fc3b152e4b518662e5bf7fb0
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/microsoft-edge.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/microsoft-edge.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/microsoft-edge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># microsoft-edge

Google에서 개발한 Chromium 웹 브라우저를 기반으로 Microsoft가 개발한 현대적인 웹 브라우저.
이 명령은 Windows에서는 `msedge`로 사용 가능합니다.
참고: `chromium`의 추가 명령 인수도 Microsoft Edge 제어에 사용할 수 있습니다.
더 많은 정보: <https://microsoft.com/edge>.

- 특정 URL 또는 파일 열기:

`microsoft-edge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|경로/대상/파일.html</span>

- InPrivate 모드로 열기:

`microsoft-edge --inprivate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 새 창에서 열기:

`microsoft-edge --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 애플리케이션 모드로 열기 (툴바, URL 바, 버튼 등 없이):

`microsoft-edge --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 프록시 서버 사용:

`microsoft-edge --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 사용자 지정 프로필 디렉토리로 열기:

`microsoft-edge --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- CORS 검증 없이 열기 (API 테스트에 유용):

`microsoft-edge --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --disable-web-security`

- 각 탭이 열릴 때마다 DevTools 창 열기:

`microsoft-edge --auto-open-devtools-for-tabs`
