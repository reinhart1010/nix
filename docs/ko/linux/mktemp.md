---
layout: page
title: linux/mktemp (한국어)
description: "임시 파일 또는 디렉토리 생성."
content_hash: 52944090bc60a1a0aee0986a60d93f24f9fa1da1
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/mktemp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/mktemp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mktemp

임시 파일 또는 디렉토리 생성.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/mktemp-invocation.html>.

- 빈 임시 파일을 생성하고 절대 경로 출력:

`mktemp`

- 사용자 지정 디렉토리 사용 (기본값: `$TMPDIR`, 또는 `/tmp`):

`mktemp --tmpdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/tempdir</span>

- 사용자 지정 경로 템플릿 사용 (`X`는 무작위 영숫자 문자로 대체됨):

`mktemp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/example.XXXXXXXX</span>

- 사용자 지정 파일명 템플릿 사용:

`mktemp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.XXXXXXXX</span>

- 주어진 접미사를 가진 빈 임시 파일을 생성하고 절대 경로 출력:

`mktemp --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ext</span>

- 빈 임시 디렉토리를 생성하고 절대 경로 출력:

`mktemp --directory`
