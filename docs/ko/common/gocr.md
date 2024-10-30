---
layout: page
title: common/gocr (한국어)
description: "광학 문자 인식 도구."
content_hash: b141bcd7b0071051e452e4c9f8a6f8f50fdcbd44
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/gocr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/gocr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gocr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gocr

광학 문자 인식 도구.
엔진을 사용하여 문자를 인식하고, 사용자에게 알 수 없는 패턴을 묻는 메시지를 표시하여 데이터베이스에 저장.
더 많은 정보: <https://manned.org/gocr.1>.

- 입력([i]nput) 이미지의 문자를 인식하여 주어진 파일에 출력([o]utput)합니다. 데이터베이스([p])를 `경로/대상/데이터베이스_디렉토리` 안에 넣음. (폴더가 있는지 확인하고, 그렇지 않으면 DB 사용량이 자동으로 넘어가짐). 모드([m]ode) 130은 데이터베이스 생성 + 사용 + 확장을 의미:

`gocr -m 130 -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터베이스_디렉토리</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_이미지.png</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.txt</span>

- 문자를 인식하고 모든 문자([C]haracters)가 숫자라고 가정:

`gocr -m 130 -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터베이스_디렉토리</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_이미지.png</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.txt</span>` -C "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>`"`

- 100% 확실성(cert[a]inty)으로 문자를 인식 (문자는 알 수 없는 것을 간주될 확률이 더 높음):

`gocr -m 130 -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터베이스_디렉토리</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_이미지.png</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.txt</span>` -a 100`
