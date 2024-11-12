---
layout: page
title: osx/log (한국어)
description: "로그 시스템을 보기, 내보내기 및 구성."
content_hash: eb8fa76f211f25b4150483fc162960f4a12730b7
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/log.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/log.html
    icon: bi bi-globe
tldri18n_status: 2
---
# log

로그 시스템을 보기, 내보내기 및 구성.
더 많은 정보: <https://keith.github.io/xcode-man-pages/log.1.html>.

- 실시간 시스템 로그 스트리밍:

`log stream`

- 특정 PID를 가진 프로세스에서 `syslog`로 전송된 로그 스트리밍:

`log stream --process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_ID</span>

- 특정 이름을 가진 프로세스에서 syslog로 전송된 로그 표시:

`log show --predicate "process == '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>`'"`

- 지난 한 시간 동안 모든 로그를 디스크에 내보내기:

`sudo log collect --last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1h</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.logarchive</span>
