---
layout: page
title: common/minisign (한국어)
description: "파일 서명 및 서명 검증을 위한 간단한 도구."
content_hash: 3dbd1eef0fb75988203fa843ffb667924dc75686
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/common/minisign.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/minisign.html
    icon: bi bi-globe
tldri18n_status: 2
---
# minisign

파일 서명 및 서명 검증을 위한 간단한 도구.
더 많은 정보: <https://jedisct1.github.io/minisign/>.

- 기본 위치에 새 키 쌍 생성:

`minisign -G`

- 파일 서명:

`minisign -Sm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 서명 시, 서명에 신뢰할 수 있는(서명된) 주석과 신뢰할 수 없는(서명되지 않은) 주석 추가:

`minisign -Sm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">신뢰할 수 없는 주석</span>`" -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">신뢰할 수 있는 주석</span>`"`

- 지정된 공개 키 파일을 사용하여 파일 및 서명 내 신뢰할 수 있는 주석 검증:

`minisign -Vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/공개키.pub</span>

- Base64로 인코딩된 리터럴로 공개 키를 지정하여 파일 및 서명 내 신뢰할 수 있는 주석 검증:

`minisign -Vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -P "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공개_키_base64</span>`"`
