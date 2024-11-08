---
layout: page
title: common/mktemp (한국어)
description: "임시 파일이나 디렉토리를 생성."
content_hash: ae7036876d75ee475acfdb627c4b6e09cd794c15
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mktemp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/mktemp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/mktemp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mktemp

임시 파일이나 디렉토리를 생성.
더 많은 정보: <https://man.openbsd.org/mktemp.1>.

- 빈 임시 파일을 생성하고 절대 경로 출력:

`mktemp`

- `$TMPDIR`이 설정되지 않은 경우 사용자 지정 디렉토리 사용 (기본값은 플랫폼에 따라 다르지만 보통 `/tmp`):

`mktemp -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/임시디렉토리</span>

- 사용자 지정 경로 템플릿 사용 (`X`는 무작위 영숫자로 대체됨):

`mktemp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/example.XXXXXXXX</span>

- 사용자 지정 파일 이름 템플릿 사용:

`mktemp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.XXXXXXXX</span>

- 빈 임시 디렉토리를 생성하고 절대 경로 출력:

`mktemp -d`
