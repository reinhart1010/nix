---
layout: page
title: common/airshare (한국어)
description: "로컬 네트워크의 두 컴퓨터 사이의 데이터 전송."
content_hash: 353ac3ff34bb577371e2f3e01039a46683830a3c
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/common/airshare.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/airshare.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airshare.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airshare

로컬 네트워크의 두 컴퓨터 사이의 데이터 전송.
더 많은 정보: <https://airshare.rtfd.io/en/latest/cli.html>.

- 파일 또는 디렉터리 공유:

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리1 경로/대상/파일_또는_디렉토리2 ...</span>

- 파일 받기:

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드</span>

- 수신 서버 호스팅 (웹 인터페이스를 사용하여 파일을 업로드할 때 사용):

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드</span>

- 파일이나 디렉터리를 수신 서버로 전송:

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리1 경로/대상/파일_또는_디렉토리2 ...</span>

- 경로가 클립보드에 복사된 파일 전송:

`airshare --file-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드</span>

- 파일을 받아 클립보드에 복사:

`airshare --clip-receive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드</span>
