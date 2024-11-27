---
layout: page
title: common/chromium (한국어)
description: "구글에서 주도하는 오픈소스 웹 브라우저."
content_hash: 654d853dd4b4e74461a6c5a4dcf912e2bd2bd121
last_modified_at: 2024-11-27
related_topics:
  - title: Deutsch version
    url: /de/common/chromium.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chromium.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chromium.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chromium.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/chromium.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chromium.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chromium.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chromium.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chromium

구글에서 주도하는 오픈소스 웹 브라우저.
참고: 원하는 웹 브라우저로 `chromium` 명령어를 대체할 수 있습니다. 예를 들어 `brave`, `google-chrome`, `opera`, `vivaldi` 등을 사용할 수 있습니다.
더 많은 정보: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- 특정 URL 또는 파일 열기:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|경로/대상/파일.html</span>

- 익명으로 열기:

`chromium --incognito `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 새 창으로 열기:

`chromium --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 앱 모드로 열기 (툴바, URL 바, 버튼 등 제외):

`chromium --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 프록시 서버 사용:

`chromium --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://호스트명:포트</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 사용자 데이터 디렉토리 지정:

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>

- CORS 검증 없이 열기 (API 테스트 유용):

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` --disable-web-security`

- 각 탭에 대해 DevTools 창 열기:

`chromium --auto-open-devtools-for-tabs`
