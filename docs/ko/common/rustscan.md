---
layout: page
title: common/rustscan (한국어)
description: "Rust로 작성된 빠른 포트 스캐너로 `nmap`이 내장되어 있습니다."
content_hash: abacf1e0917d7cdfc3252215b10649cc246c78a3
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/rustscan.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/rustscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustscan

Rust로 작성된 빠른 포트 스캐너로 `nmap`이 내장되어 있습니다.
더 많은 정보: <https://github.com/RustScan/RustScan>.

- 기본값을 사용하여 쉼표로 구분된 하나 이상의 [a]드레스를 대상으로 모든 포트를 스캔:

`rustscan --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_또는_호스트명</span>

- [t]op 1000 포트를 서비스 및 버전 감지와 함께 스캔:

`rustscan --top --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소_또는_주소들</span>

- 특정 [p]ort 목록을 스캔:

`rustscan --ports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트1,포트2,...,포트N</span>` --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소_또는_주소들</span>

- 특정 범위의 포트를 스캔:

`rustscan --range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작-끝</span>` --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소_또는_주소들</span>

- `nmap`에 스크립트 인수 추가:

`rustscan --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소_또는_주소들</span>` -- -A -sC`

- 사용자 정의 [b]atch 크기(기본: 4500) 및 [t]imeout(기본: 1500ms)으로 스캔:

`rustscan --batch-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배치_크기</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타임아웃</span>` --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소_또는_주소들</span>

- 특정 포트 순서로 스캔:

`rustscan --scan-order `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">serial|random</span>` --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소_또는_주소들</span>

- greppable 모드로 스캔(`nmap` 없이 포트 출력만):

`rustscan --greppable --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소_또는_주소들</span>
