---
layout: page
title: common/dnsx (한국어)
description: "여러 DNS 쿼리를 실행하기 위한 빠르고 목적이 다양한 DNS 도구 키트."
content_hash: 313c727404d1398b628821bc0ae8ebecf8b3c517
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/dnsx.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dnsx.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dnsx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dnsx

여러 DNS 쿼리를 실행하기 위한 빠르고 목적이 다양한 DNS 도구 키트.
참고: 어떤 경우에는 `dnsx`에 대한 입력이 `stdin` (파이프 `|`)를 통해 전달되어야 함.
See also: `dig`, `dog`, `dnstracer`.
더 많은 정보: <https://github.com/projectdiscovery/dnsx>.

- (하위)도메인의 A 레코드를 쿼리하고 수신된 응답([re]sponse)을 표시:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` | dnsx -a -re`

- 모든 DNS 레코드(A, AAAA, CNAME, NS, TXT, SRV, PTR, MX, SOA, AXFR, CAA)를 쿼리:

`dnsx -recon -re <<< `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 특정 유형의 DNS 레코드를 쿼리:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` | dnsx -re -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa</span>

- 응답([r]esponse)만 ([o]nly) 출력 (쿼리된 도메인이나 하위 도메인은 표시하지 않음):

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` | dnsx -ro`

- 쿼리의 원시 응답을 표시하고, 실패에 대한 시도를 라도 재시도할 [r]esolvers를 지정:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` | dnsx -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|raw</span>` -resolver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1,8.8.8.8,...</span>` -retry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- 자리 표시자를 사용한 무차별 대입 DNS 레코드:

`dnsx -domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FUZZ.example.com</span>` -wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>` -re`

- DNS 도메인([d]omains) 및 단어 목록의 무차별 대입 DNS 레코드를 색상 코드가 없는([n]o [c]olor) 파일에 출력([o]utput) 결과를 추가:

`dnsx -domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/도메인.txt</span>` -wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>` -re -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.txt</span>` -no-color`

- 초당 DNS 쿼리 속도를 제한하여([r]ate [l]imiting) 지정된 하위 도메인 목록에 대한 `CNAME` 레코드를 추출:

`subfinder -silent -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` | dnsx -cname -re -rl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>
