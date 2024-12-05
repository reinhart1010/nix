---
layout: page
title: common/wfuzz (한국어)
description: "웹 애플리케이션 브루트포스 도구."
content_hash: 5719cca525dcf2665d660f397f478529857f217b
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/wfuzz.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wfuzz

웹 애플리케이션 브루트포스 도구.
더 많은 정보: <https://wfuzz.readthedocs.io/en/latest/user/basicusage.html>.

- 지정된 [w]ordlist 및 [p]roxy를 사용하여 디렉토리 및 파일 브루트포스:

`wfuzz -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1:8080:HTTP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/FUZZ</span>

- 결과를 [f]ile에 저장:

`wfuzz -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/FUZZ</span>

- 색상 출력 및 지정한 응답 코드만 표시:

`wfuzz -c -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --sc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200,301,302</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/FUZZ</span>

- 사용자 정의 [H]eader를 사용하여 서브도메인 퍼징, 특정 응답 [c]odes 및 단어 수 숨김. [t]hreads를 100으로 증가시키고 대상 ip/도메인 포함:

`wfuzz -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -H "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Host: FUZZ.example.com</span>`" --hc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">301</span>` --hw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">222</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 파일에서 각 FUZ[z] 키워드에 대한 사용자 명과 비밀번호 목록을 사용하여 기본 인증 브루트포스, 실패한 시도에 대한 응답 [c]odes 숨김:

`wfuzz -c --hc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">401</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">요청 간 지연 시간(초)</span>` -z file,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사용자명</span>` -z file,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀번호</span>` --basic 'FUZZ:FUZ2Z' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 커맨드라인에서 직접 워드리스트 제공 및 POST 요청을 사용하여 퍼징:

`wfuzz -z list,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">word1-word2-...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://api.example.com</span>` -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id=FUZZ&showwallet=true</span>`"`

- 파일에서 워드리스트를 제공하며 base64 및 md5 인코딩 적용 (`wfuzz -e encoders`로 사용 가능한 모든 인코더 나열):

`wfuzz -z file,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`,none-base64-md5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/FUZZ</span>

- 사용 가능한 인코더/페이로드/이터레이터/프린터/스크립트 나열:

`wfuzz -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoders|payloads|iterators|printers|scripts</span>
