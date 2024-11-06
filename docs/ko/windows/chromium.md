---
layout: page
title: windows/chromium (한국어)
description: "주로 Google에서 개발 및 유지 관리하는 오픈 소스 웹 브라우저."
content_hash: 3cf8872d01a1ccfabf075bdd63ad52ced28d9021
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/chromium.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/chromium.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/chromium.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chromium

주로 Google에서 개발 및 유지 관리하는 오픈 소스 웹 브라우저.
참고: 원하는 웹 브라우저에 따라 `chromium` 명령을 `brave`, `google-chrome`, `microsoft-edge`/`msedge`, `opera`, 또는 `vivaldi`로 대체해야 할 수 있습니다.
더 많은 정보: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- 특정 URL 또는 파일 열기:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|경로/대상/파일.html</span>

- 시크릿 모드로 열기 (Microsoft Edge의 경우 `--inprivate` 사용):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chromium --incognito|msedge --inprivate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 새 창으로 열기:

`chromium --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 애플리케이션 모드로 열기 (툴바, URL 바, 버튼 등 없이):

`chromium --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 프록시 서버 사용:

`chromium --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 사용자 정의 프로필 디렉토리로 열기:

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- CORS 검증 없이 열기 (API 테스트에 유용):

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --disable-web-security`

- 열리는 각 탭에 대해 개발자 도구 창과 함께 열기:

`chromium --auto-open-devtools-for-tabs`
