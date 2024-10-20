---
layout: page
title: common/ffe (한국어)
description: "플랫 데이터베이스 파일에서 필드를 추출하고 다른 형식으로 씀."
content_hash: 859304edc9a56d80c08ddab3590ed51b5e244d02
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/ffe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ffe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ffe

플랫 데이터베이스 파일에서 필드를 추출하고 다른 형식으로 씀.
입력을 해석하고 출력 형식을 지정하려면 구성 파일이 필요.
더 많은 정보: <https://ff-extractor.sourceforge.net/ffe.html>.

- 지정된 데이터 구성을 사용하여 모든 입력 데이터를 표시:

`ffe --configuration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성.ffe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력</span>

- 입력 파일을 새로운 형식의 출력 파일로 변환:

`ffe --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성.ffe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력</span>

- `~/.fferc` 구성 파일의 정의에서 입력 구조 및 출력 형식을 선택:

`ffe --structure=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">structure</span>` --print=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력</span>

- 선택한 필드만 작성하기:

`ffe --field-list="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FirstName,LastName,Age</span>`" -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성.ffe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력</span>

- 표현식과 일치하는 레코드만 작성:

`ffe -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LastName=Smith</span>`" -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성.ffe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력</span>

- 도움말 표시:

`ffe --help`
