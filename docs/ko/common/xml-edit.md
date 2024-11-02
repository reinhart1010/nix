---
layout: page
title: common/xml-edit (한국어)
description: "XML 문서 편집."
content_hash: af4b551269040fc685c1d6b2e302a2209aa7a59e
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/xml-edit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xml edit

XML 문서 편집.
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- XML 문서에서 XPATH와 일치하는 요소 삭제:

`xml edit --delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH1</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>

- XML 문서의 요소 노드를 XPATH1에서 XPATH2로 이동:

`xml edit --move "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH1</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XPATH2</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>

- 이름이 "id"인 모든 속성을 "ID"로 변경:

`xml edit --rename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//*/@id</span>`" -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>

- "table" 요소의 하위 요소 중 "rec"으로 명명된 요소를 "record"로 이름 변경:

`xml edit --rename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/xml/table/rec</span>`" -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">record</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>

- "id=3"인 XML 테이블 레코드를 "id=5" 값으로 업데이트:

`xml edit --update "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml/table/rec[@id=3]/@id</span>`" -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>

- 도움말 표시:

`xml edit --help`
