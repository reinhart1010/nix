---
layout: page
title: common/fmt (한국어)
description: "단락을 결합하고 줄 너비를 문자 수 (기본적으로 75자)로 제한하여 텍스트 파일의 서식을 다시 지정."
content_hash: 1842b6a954282f44e5ff7a464b1196156370485d
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/fmt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/fmt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fmt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fmt

단락을 결합하고 줄 너비를 문자 수 (기본적으로 75자)로 제한하여 텍스트 파일의 서식을 다시 지정.
더 많은 정보: <https://www.gnu.org/software/coreutils/fmt>.

- 파일 재포맷:

`fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- (최대) `n` 문자의 출력 줄을 생성하는 파일 형식을 다시 지정:

`fmt -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 주어진 너비보다 짧은 줄을 결합하지 않고, 파일 형식을 다시 지정:

`fmt -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 균일한 간격 (단어 사이에 1칸, 단락 사이에 2칸)으로 파일 형식을 다시 지정:

`fmt -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
