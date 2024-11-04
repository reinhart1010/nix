---
layout: page
title: common/httpx (한국어)
description: "여러 프로브를 한 번에 실행하기 위해 Go로 작성된 빠르고 다목적 HTTP 도구 키트."
content_hash: a91255bc7a01d45098e8d9ade1b18e78e6ff8666
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/httpx.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/httpx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># httpx

여러 프로브를 한 번에 실행하기 위해 Go로 작성된 빠르고 다목적 HTTP 도구 키트.
참고: 동일한 명령 이름을 가진 관련 없는 Python's HTTPX와 혼동하지 말것.
더 많은 정보: <https://github.com/projectdiscovery/httpx>.

- 프로브 상태를 표시하는 [u]RL, 호스트, IP 주소 또는 서브넷 (CIDR 표기법)에 대해 프로브를 실행:

`httpx -probe -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|host|ipaddress|subnet_with_cidr</span>

- `subfinder`의 입력으로 상태 코드([s]tatus [c]ode)를 표시하는 여러 호스트에 대해 프로브를 실행:

`subfinder -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` | httpx -sc`

- 감지된([d]etected) 기술([t]echnology) 및 응답시간([r]esponse [t]ime)을 보여주는 파일에서 호스트 목록([l]ist)에 대해 제한된 속도로 실행:

`httpx -rl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">150</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/개행으로_구분된_호스트_목록</span>` -td -rt`

- 웹페이지 제목, 사용 중인 CDN/WAF 및 페이지 콘텐츠 해시를 표시하는 [u]RL에 대해 프로브를 실행:

`httpx -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>` -title -cdn -hash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha256</span>

- 사용자 정의된 포트([p]orts)와 특정 초 후 시간 초과가 있는 호스트 목록에 대해 프로블를 실행:

`httpx -probe -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트1,호스트2,...</span>` -p http:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,8000-8080</span>`,https:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443,8443</span>` -timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 특정 응답 코드([c]odes)를 필터링하여([f]iltering), 호스트 목록에 대해 프로브를 실행:

`httpx -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트1,호스트2,...</span>` -fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">400,401,404</span>

- 특정 응답 코드([c]odes)와 일치하는([m]atching) 호스트 목록에 대해 프로브를 실행:

`httpx -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트1,호스트2,...</span>` -mc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200,301,304</span>

- 특정 경로의 스크린샷([s]creenshots)을 저장하고([s]aving) 스크린샷 타임아웃([s]creenshot [t]imeouts)을 사용하여 URL에 대해 프로브를 실행 (리소스는 `./output`에 저장됨):

`httpx -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.github.com</span>` -path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tldr-pages/tldr,/projectdiscovery/httpx</span>` -ss -st `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
