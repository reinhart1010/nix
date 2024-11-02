---
layout: page
title: common/xml-unescape (한국어)
description: "특수 XML 문자를 원래대로 변환, 예: `&lt;a1&gt;` → `<a1>`."
content_hash: 73bf5f5288d4d0af9b10f467dedd624793497fc3
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/xml-unescape.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xml unescape

특수 XML 문자를 원래대로 변환, 예: `&lt;a1&gt;` → `<a1>`.
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- 문자열에서 특수 XML 문자를 원래대로 변환:

`xml unescape "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">&lt;a1&gt;</span>`"`

- `stdin`에서 특수 XML 문자를 원래대로 변환:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">&lt;a1&gt;</span>`" | xml unescape`

- 도움말 표시:

`xml escape --help`
