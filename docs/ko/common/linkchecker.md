---
layout: page
title: common/linkchecker (한국어)
description: "HTML 문서 및 웹사이트의 깨진 링크를 확인하는 명령줄 클라이언트."
content_hash: 83d03b65b61b107990264d5044004fcee839d3c6
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/linkchecker.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linkchecker

HTML 문서 및 웹사이트의 깨진 링크를 확인하는 명령줄 클라이언트.
더 많은 정보: <https://linkchecker.github.io/linkchecker/>.

- <https://example.com/>에서 깨진 링크 찾기:

`linkchecker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>

- 외부 도메인을 가리키는 URL도 확인:

`linkchecker --check-extern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>

- 특정 정규 표현식과 일치하는 URL 무시:

`linkchecker --ignore-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>

- 결과를 CSV 파일로 출력:

`linkchecker --file-output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">csv</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>
