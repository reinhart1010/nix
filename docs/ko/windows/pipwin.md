---
layout: page
title: windows/pipwin (한국어)
description: "Windows에서 비공식 Python 패키지 이진 파일을 설치하는 도구입니다."
content_hash: c0e7cd36b0a44bf78f11b199477b2719aa905a1a
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/windows/pipwin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pipwin

Windows에서 비공식 Python 패키지 이진 파일을 설치하는 도구입니다.
더 많은 정보: <https://github.com/lepisma/pipwin>.

- 다운로드할 수 있는 모든 패키지 목록 표시:

`pipwin list`

- 패키지 검색:

`pipwin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">일부_이름|이름</span>

- 패키지 설치:

`pipwin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거:

`pipwin uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 디렉토리에 패키지 다운로드:

`pipwin download --dest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- `requirements.txt`에 따라 패키지 설치:

`pipwin install --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\requirements.txt</span>
