---
layout: page
title: osx/xsltproc (한국어)
description: "XSLT를 사용하여 XML을 변환하여 출력(주로 HTML 또는 XML)을 생성합니다."
content_hash: 0e846d71f15cdeea9644c2ab22dac19b3e0f50c6
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/xsltproc.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xsltproc.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/xsltproc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/xsltproc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xsltproc

XSLT를 사용하여 XML을 변환하여 출력(주로 HTML 또는 XML)을 생성합니다.
더 많은 정보: <http://www.xmlsoft.org/xslt/xsltproc.html>.

- 특정 XSLT 스타일시트를 사용하여 XML 파일 변환:

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스타일시트_파일.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.xml</span>

- 스타일시트의 매개변수에 값을 전달:

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.html</span>` --stringparam "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스타일시트_파일.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/xml_파일.xml</span>
