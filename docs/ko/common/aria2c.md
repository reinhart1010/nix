---
layout: page
title: common/aria2c (한국어)
description: "빠른 다운로드 유틸리티."
content_hash: db27832114b3ada992a5a482b4dd418b20c2ee71
last_modified_at: 2024-10-09
related_topics:
  - title: English version
    url: /en/common/aria2c.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aria2c.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/aria2c.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aria2c.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aria2c.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aria2c.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aria2c.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aria2c

빠른 다운로드 유틸리티.
HTTP(S), FTP, SFTP, BitTorrent 및 Metalink를 지원합니다.
더 많은 정보: <https://aria2.github.io>.

- 특정 URI를 파일로 다운로드:

`aria2c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`

- 특정 출력 이름을 가진 URI에서 파일을 다운로드:

`aria2c --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`

- 여러 개의 서로 다른 파일을 병렬로 다운로드:

`aria2c --force-sequential `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">false</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url1 url2 ...</span>`"`

- 다른 미러 사이트에서 동일한 파일을 다운로드:

`aria2c --checksum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha-256</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url1</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url2</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">urlN</span>`"`

- 특정 개수의 병렬 다운로드가 되고 있는 파일에 나열된 URI을 다운로드:

`aria2c --input-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --max-concurrent-downloads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">다운로드_횟수</span>

- 다중 연결로 다운로드:

`aria2c --split `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연결_개수</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`

- 사용자 이름과 비밀번호를 사용하여 FTP 다운로드:

`aria2c --ftp-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --ftp-passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패스워드</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`

- 다운로드 속도를 바이트/초로 제한:

`aria2c --max-download-limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속도</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`
