---
layout: page
title: common/xml-elements (한국어)
description: "XML 문서의 요소를 추출하고 구조를 표시합니다."
content_hash: a64c30b9a571ec7fef4dc3c3c2568aec9efd1a9a
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/xml-elements.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xml elements

XML 문서의 요소를 추출하고 구조를 표시합니다.
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- XML 문서에서 요소 추출 (XPATH 표현 생성):

`xml elements `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/요소.xpath</span>

- XML 문서에서 요소와 그 속성 추출:

`xml elements -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/요소.xpath</span>

- XML 문서에서 요소, 속성 및 값 추출:

`xml elements -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/요소.xpath</span>

- XML 문서의 정렬된 고유 요소를 출력하여 구조 확인:

`xml elements -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>

- 깊이 3까지의 XML 문서의 정렬된 고유 요소 출력:

`xml elements -d`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>

- 도움말 표시:

`xml elements --help`
