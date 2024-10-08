---
layout: page
title: linux/systemd-nspawn (한국어)
description: "경량 컨테이너에서 명령이나 운영 체제를 실행."
content_hash: a3a0a1cd7a58a14ab4ef6ce1c4efa998f7fc7877
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/systemd-nspawn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-nspawn

경량 컨테이너에서 명령이나 운영 체제를 실행.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemd-nspawn.html>.

- 컨테이너에서 명령 실행:

`systemd-nspawn --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/컨테이너_루트</span>

- 컨테이너에서 전체 Linux 기반 운영 체제 실행:

`systemd-nspawn --boot --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/컨테이너_루트</span>

- 지정된 명령을 컨테이너에서 PID 2로 실행 (PID 1 대신)하고, 초기화 프로세스 스텁 사용:

`systemd-nspawn --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/컨테이너_루트</span>` --as-pid2`

- 머신 이름과 호스트 이름 지정:

`systemd-nspawn --machine=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>` --hostname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_호스트</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/컨테이너_루트</span>
