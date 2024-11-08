---
layout: page
title: common/minifab (한국어)
description: "Hyperledger Fabric 네트워크의 설정 및 배포를 자동화."
content_hash: 39caaeae88a104246a17123bd8ba15627fd76626
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/minifab.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/minifab.html
    icon: bi bi-globe
tldri18n_status: 2
---
# minifab

Hyperledger Fabric 네트워크의 설정 및 배포를 자동화.
더 많은 정보: <https://github.com/hyperledger-labs/minifabric>.

- 기본 Hyperledger Fabric 네트워크 시작:

`minifab up -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minifab_버전</span>

- Hyperledger Fabric 네트워크 중지:

`minifab down`

- 지정된 채널에 체인코드 설치:

`minifab install -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">체인코드_이름</span>

- 특정 버전의 체인코드를 채널에 설치:

`minifab install -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">체인코드_이름</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">체인코드_버전</span>

- 설치/업그레이드 후 체인코드 초기화:

`minifab approve,commit,initialize,discover`

- 지정된 인수로 체인코드 메서드 호출:

`minifab invoke -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">체인코드_이름</span>` -p '"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메서드_이름</span>`", "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1</span>`", "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수2</span>`", ...'`

- 원장에 쿼리 실행:

`minifab blockquery `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">블록_번호</span>

- 애플리케이션을 빠르게 실행:

`minifab apprun -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_프로그래밍_언어</span>
