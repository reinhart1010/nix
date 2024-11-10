---
layout: page
title: linux/fcrackzip (한국어)
description: "ZIP 압축 파일 비밀번호 크랙 도구."
content_hash: f58a50033a80109ac78ad3b4b8989821e61aea97
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/fcrackzip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fcrackzip

ZIP 압축 파일 비밀번호 크랙 도구.
더 많은 정보: <https://manned.org/fcrackzip>.

- 4에서 8자리의 길이를 가지며, 영숫자만 포함된 비밀번호를 무차별 대입으로 찾기 (순서 중요):

`fcrackzip --brute-force --length 4-8 --charset aA1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축_파일</span>

- 자세히 보기 모드에서 3자리의 길이를 가지며, 소문자, `$` 및 `%`만 포함된 비밀번호를 무차별 대입으로 찾기:

`fcrackzip -v --brute-force --length 3 --charset a:$% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축_파일</span>

- 소문자와 특수 문자만 포함된 비밀번호를 무차별 대입으로 찾기:

`fcrackzip --brute-force --length 4 --charset a! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축_파일</span>

- 숫자만 포함된 비밀번호를 `12345`부터 시작하여 무차별 대입으로 찾기:

`fcrackzip --brute-force --length 5 --charset 1 --init-password 12345 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축_파일</span>

- 사전 목록을 사용하여 비밀번호 크랙:

`fcrackzip --use-unzip --dictionary --init-password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단어목록</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축_파일</span>

- 크랙 성능 벤치마크:

`fcrackzip --benchmark`
