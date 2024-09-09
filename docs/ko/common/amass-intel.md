---
layout: page
title: common/amass-intel (한국어)
description: "루트 도메인 및 ASN과 같은 조직에 대한 오픈 소스 정보 수집."
content_hash: f305d5639f76f05f62478fa30bb16ce33893f245
last_modified_at: 2024-09-09
related_topics:
  - title: English version
    url: /en/common/amass-intel.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/amass-intel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-intel.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/amass-intel.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/amass-intel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# amass intel

루트 도메인 및 ASN과 같은 조직에 대한 오픈 소스 정보 수집.
더 많은 정보: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- IP 주소([addr]ess) 범위에서 루트 도메인 찾기:

`amass intel -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- 활성 정찰 방법을 사용:

`amass intel -active -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- 도메인([d]omain)과 관련된 루트 도메인 찾기:

`amass intel -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>

- 조직([org]anisation)에 속하는 ASN 찾기:

`amass intel -org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_이름</span>

- 주어진 자율 시스템 번호에 속하는 루트 도메인 찾기:

`amass intel -asn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asn</span>

- 결과를 텍스트 파일에 저장:

`amass intel -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>` -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>

- 사용 가능한 모든 데이터 소스 나열:

`amass intel -list`
