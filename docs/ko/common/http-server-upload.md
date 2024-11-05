---
layout: page
title: common/http-server-upload (한국어)
description: "파일 업로드를 위한 경량 인터페이스를 제공하는 구성이 필요없는 커멘트라인 HTTP 서버."
content_hash: 543c13ded748e26a3be5e9355a9913115751350b
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/http-server-upload.html
    icon: bi bi-globe
tldri18n_status: 2
---
# http-server-upload

파일 업로드를 위한 경량 인터페이스를 제공하는 구성이 필요없는 커멘트라인 HTTP 서버.
더 많은 정보: <https://github.com/crycode-de/http-server-upload>.

- 기본 포트에서 HTTP 서버를 시작하여 현재 디렉터리에 파일을 업로드:

`http-server-upload`

- MiB 단위로 지정된 최대 허용 파일 크기로 HTTP 서버를 시작 (기본값 200 MiB):

`MAX_FILE_SIZE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size_in_megabytes</span>` http-server-upload`

- 특정 포트에서 HTTP 서버를 시작해 현재 디렉터리에 파일을 업로드:

`PORT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` http-server-upload`

- HTTP 서버를 시작하고, 업로드된 파일을 특정 디렉터리에 저장:

`UPLOAD_DIR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` http-server-upload`

- 업로드 중에 파일을 임시로 저장하기 위해 특정 디렉터리를 사용하여 HTTP 서버를 시작:

`UPLOAD_TMP_DIR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` http-server-upload`

- HTTP post의 특정 토큰 필드를 사용하여 업로드를 허용하는 HTTP 서버를 시작:

`TOKEN=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>` http-server-upload`
