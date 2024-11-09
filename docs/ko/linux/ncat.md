---
layout: page
title: linux/ncat (한국어)
description: "네트워크를 통해 데이터를 읽고, 쓰고, 리디렉션하고, 암호화."
content_hash: 7624c3b7c0ad1fcb2f1ceae1ec2504f52d077468
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ncat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ncat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ncat

네트워크를 통해 데이터를 읽고, 쓰고, 리디렉션하고, 암호화.
유사한 유틸리티 `netcat`/`nc`의 대체 구현.
더 많은 정보: <https://nmap.org/ncat/guide/index.html>.

- 지정된 포트에서 입력을 대기하고 지정된 파일에 기록:

`ncat -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 여러 연결을 수락하고 닫힌 후에도 ncat을 열어 두기:

`ncat -lk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 지정된 파일의 출력을 지정된 호스트의 지정된 포트로 전송:

`ncat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 암호화된 채널에서 여러 수신 연결을 수락하여 트래픽 내용을 탐지하지 않도록 회피:

`ncat --ssl -k -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- SSL을 통해 열린 `ncat` 연결에 접속:

`ncat --ssl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 특정 포트로 원격 호스트에 연결 가능 여부를 타임아웃과 함께 확인:

`ncat -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>` -vz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>
