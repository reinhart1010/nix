---
layout: page
title: common/xml-select (한국어)
description: "XPATH를 사용하여 XML 문서에서 선택."
content_hash: 78d1b9fc075966ba0e8d7a8c0aa896ef1844b7cb
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/xml-select.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xml select

XPATH를 사용하여 XML 문서에서 선택.
팁: XML 문서의 XPATH를 표시하려면 `xml elements`를 사용하세요.
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- "XPATH1"과 일치하는 모든 요소를 선택하고 그 하위 요소 "XPATH2"의 값을 출력:

`xml select --template --match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH1</span>`" --value-of "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH2</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>

- "XPATH1"과 일치하는 요소를 선택하고 "XPATH2"의 값을 새 줄과 함께 텍스트로 출력:

`xml select --text --template --match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH1</span>`" --value-of "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH2</span>`" --nl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>

- "XPATH1"의 요소 수를 계산:

`xml select --template --value-of "count(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH1</span>`)" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>

- 하나 이상의 XML 문서에서 모든 노드 수를 계산:

`xml select --text --template --inp-name --output " " --value-of "count(node())" --nl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.xml|URI</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력2.xml|URI</span>

- 도움말 표시:

`xml select --help`
