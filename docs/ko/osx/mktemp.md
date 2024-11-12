---
layout: page
title: osx/mktemp (한국어)
description: "임시 파일 또는 디렉터리 생성."
content_hash: 0223c44ed0acae37b25bb4b1d737ce30abb34210
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/mktemp.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/mktemp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/mktemp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mktemp

임시 파일 또는 디렉터리 생성.
더 많은 정보: <https://keith.github.io/xcode-man-pages/mktemp.1.html>.

- 빈 임시 파일을 생성하고 절대 경로 출력:

`mktemp`

- 사용자 정의 디렉터리 사용 (`getconf DARWIN_USER_TEMP_DIR`의 출력 또는 `/tmp`가 기본값):

`mktemp --tmpdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/임시_폴더</span>

- 사용자 정의 경로 템플릿 사용 (`X`는 무작위 영숫자 문자로 대체됨):

`mktemp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/example.XXXXXXXX</span>

- 사용자 정의 파일 이름 접두사 사용:

`mktemp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제</span>

- 빈 임시 디렉터리를 생성하고 절대 경로 출력:

`mktemp --directory`
