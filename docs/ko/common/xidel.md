---
layout: page
title: common/xidel (한국어)
description: "HTML/XML 페이지 및 JSON API에서 데이터를 다운로드하고 추출."
content_hash: 14a050fa7efa316e8214f6dad81292fb938bf337
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xidel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xidel

HTML/XML 페이지 및 JSON API에서 데이터를 다운로드하고 추출.
더 많은 정보: <https://www.videlibri.de/xidel.html>.

- Google 검색으로 찾은 모든 URL 출력:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/search?q=test</span>` --extract "//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']"`

- Google 검색으로 찾은 모든 페이지의 제목을 출력하고 다운로드:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/search?q=test</span>` --follow "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']</span>`" --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//title</span>` --download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{$host}/'</span>

- 페이지의 모든 링크를 따라가서 제목을 XPath로 출력:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>` --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//a</span>` --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//title</span>

- 페이지의 모든 링크를 따라가서 제목을 CSS 선택자로 출력:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>` --follow "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">css('a')</span>`" --css `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>

- 페이지의 모든 링크를 따라가서 제목을 패턴 매칭으로 출력:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>` --follow "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><a>{.}</a>*</span>`" --extract "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><title>{.}</title></span>`"`

- example.xml에서 패턴을 읽고 "ood"를 포함한 요소가 있는지 확인(없으면 실패):

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/example.xml</span>` --extract "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><x><foo>ood</foo><bar>{.}</bar></x></span>`"`

- 패턴 매칭을 사용하여 제목과 URL을 포함한 최신 Stack Overflow 질문 출력:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://stackoverflow.com/feeds</span>` --extract "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><entry><title>{title:=.}</title><link>{uri:=@href}</link></entry>+</span>`"`

- 읽지 않은 Reddit 메일 확인, 웹 스크래핑, CSS, XPath, JSONiq 및 자동 양식 평가 조합:

`xidel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://reddit.com</span>` --follow "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">form(css('form.login-form')[1], {'user': '$your_username', 'passwd': '$your_password'})</span>`" --extract "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">css('#mail')/@title</span>`"`
