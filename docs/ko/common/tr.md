---
layout: page
title: common/tr (한국어)
description: "문자를 변환합니다: 단일 문자 및 문자 집합을 기반으로 대체를 수행합니다."
content_hash: 3eb66e1edd7ec54889d415e1f491369cc98eed83
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/common/tr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tr

문자를 변환합니다: 단일 문자 및 문자 집합을 기반으로 대체를 수행합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- 파일에서 특정 문자의 모든 발생을 대체하고 결과를 출력:

`tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">찾을_문자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체할_문자</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 다른 명령의 출력에서 특정 문자의 모든 발생을 대체:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>` | tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">찾을_문자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체할_문자</span>

- 첫 번째 집합의 각 문자를 두 번째 집합의 해당 문자로 매핑:

`tr '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abcd</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jkmn</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 입력에서 지정된 문자 집합의 모든 발생 삭제:

`tr -d '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_문자들</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 연속된 같은 문자를 하나의 문자로 압축:

`tr -s '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_문자들</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 내용을 대문자로 변환:

`tr "[:lower:]" "[:upper:]" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에서 출력 가능한 문자가 아닌 문자 제거:

`tr -cd "[:print:]" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
