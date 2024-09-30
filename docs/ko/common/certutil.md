---
layout: page
title: common/certutil (한국어)
description: "NSS 데이터베이스와 기타 NSS 토큰 모두에서 키와 인증서를 관리."
content_hash: 94eb6896b47af76ee2faff64e5fea1cfbda6e2e1
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/certutil.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/certutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/certutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# certutil

NSS 데이터베이스와 기타 NSS 토큰 모두에서 키와 인증서를 관리.
더 많은 정보: <https://manned.org/certutil>.

- 현재 디렉터리([d]irectory)에 새로운([N]ew) 인증서 데이터베이스를 만듬:

`certutil -N -d .`

- 데이터베이스의 모든 인증서를 나열:

`certutil -L -d .`

- 비밀번호 파일([f]ile)을 지정하는 데이터베이스의 모든 개인 키([K]eys)를 나열:

`certutil -K -d . -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패스워드_파일.txt</span>

- 닉네임([n]ickname), 신뢰 속성([t]rust attributes) 및 입력([i]nput) CRT 파일을 지정하여 요청자 데이터베이스에 서명된 인증서를 추가([A]dd):

`certutil -A -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_인증서</span>`" -t ",," -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.crt</span>` -d .`

- Add subject alternative names to a given [c]ertificate with a specific key size ([g]):

`certutil -S -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패스워드_파일.txt</span>` -d . -t ",," -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_인증서</span>`" -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_이름</span>`" -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` -s "CN=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공통_이름</span>`,O=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>`"`
