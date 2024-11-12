---
layout: page
title: osx/security (한국어)
description: "키체인, 키, 인증서 및 보안 프레임워크를 관리합니다."
content_hash: cb82aba5f013ed40bd9c9f223c16ae535b8149ea
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/security.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/security.html
    icon: bi bi-globe
tldri18n_status: 2
---
# security

키체인, 키, 인증서 및 보안 프레임워크를 관리합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/security.1.html>.

- 사용 가능한 모든 키체인 나열:

`security list-keychains`

- 특정 키체인 삭제:

`security delete-keychain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.keychain</span>

- 키체인 생성:

`security create-keychain -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.keychain</span>

- 인증서를 웹사이트 또는 [s]서비스에서 사용하도록 [c]일반 이름으로 설정 (동일한 일반 이름을 가진 인증서가 여러 개 있는 경우 실패):

`security set-identity-preference -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL|호스트명|서비스</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">일반_이름</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.keychain</span>

- 파일에서 [k]키체인으로 인증서 추가 (-k가 지정되지 않으면 기본 키체인이 사용됨):

`security add-certificates -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.keychain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인증서_파일.pem</span>

- 사용자별 신뢰 설정에 CA 인증서 추가:

`security add-trusted-cert -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사용자-키체인.keychain-db</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/ca-인증서_파일.pem</span>

- 사용자별 신뢰 설정에서 CA 인증서 제거:

`security remove-trusted-cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/ca-인증서_파일.pem</span>
