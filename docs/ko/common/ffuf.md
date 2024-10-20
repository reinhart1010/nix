---
layout: page
title: common/ffuf (한국어)
description: "Go로 작성된 빠른 웹 퍼저."
content_hash: 7bf3c97624b76ad23a888a9b77457ca03e90c83d
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/ffuf.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ffuf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ffuf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ffuf

Go로 작성된 빠른 웹 퍼저.
`FUZZ` 키워드가 자리 표시자로 사용됨. `ffuf`는 `FUZZ`라는 단어를 단어 목록의 모든 단어로 변경해 URL에 접속하려 시도.
더 많은 정보: <https://github.com/ffuf/ffuf#usage>.

- 색상 출력([c]olored output)과 대상 URL([u]RL)을 지정하는 단어 리스트([w]ordlist)를 사용하여 디렉토리를 열거:

`ffuf -c -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://target/FUZZ</span>

- 키워드 위치를 변경하여 하위 도메인의 웹서버를 열거:

`ffuf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서브도메인.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://FUZZ.target.com</span>

- 지정된 스레드([t]hreads) (기본값: 40)를 퍼징하고 트래픽을 프로파일링(pro[x]ying)하고 출력([o]utput)을 파일에 저장:

`ffuf -o -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://target/FUZZ</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>

- 특정 헤더([H]eader) ("이름: 값")를 퍼징하고 HTTP 상태 코드와 일치시킴([m]atch):

`ffuf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://target.com</span>` -H "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Host: FUZZ</span>`" -mc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>

- 지정된 HTTP 메소드와 데이터([d]ata)를 퍼즈하고, 쉼표로 구분된 상태 코드([c]odes)를 필터링([f]iltering):

`ffuf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/포스트데이터.txt</span>` -X `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POST</span>` -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username=admin\&password=FUZZ</span>`" -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://target/login.php</span>` -fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">401,403</span>

- 다양한 모드를 사용하여 여러 단어 목록으로 여러 위치를 퍼즈:

`ffuf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/keys:KEY</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/values:VALUE</span>` -mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pitchfork|clusterbomb</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://target.com/id?KEY=VALUE</span>

- HTTP MITM 프록시(pro[x]y) (Burp Suite 또는 `mitmproxy`)를 통한 프록시 요청:

`ffuf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://target.com/FUZZ</span>
