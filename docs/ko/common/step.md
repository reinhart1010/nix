---
layout: page
title: common/step (한국어)
description: "사용하기 쉬운 CLI 도구로, 공개 키 기반 구조(PKI) 시스템 및 워크플로를 구축, 운영 및 자동화하는 데 도움을 줍니다."
content_hash: d07e210a7cc09d8aca63be31abb5615651c9ea02
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/step.html
    icon: bi bi-globe
tldri18n_status: 2
---
# step

사용하기 쉬운 CLI 도구로, 공개 키 기반 구조(PKI) 시스템 및 워크플로를 구축, 운영 및 자동화하는 데 도움을 줍니다.
같이 보기: `openssl`.
더 많은 정보: <https://smallstep.com/docs/step-cli/>.

- 인증서의 내용을 검사:

`step certificate inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인증서.crt</span>

- 루트 CA 인증서 및 키 생성 (개인 키 비밀번호 보호를 건너뛰려면 `--no-password --insecure` 추가):

`step certificate create "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예시 루트 CA</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/root-ca.crt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/root-ca.key</span>` --profile root-ca`

- 특정 호스트명을 위한 인증서를 생성하고 루트 CA로 서명 (CSR 생성을 생략하여 간소화 가능):

`step certificate create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname.example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/hostname.crt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/hostname.key</span>` --profile leaf --ca `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/root-ca.crt</span>` --ca-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/root-ca.key</span>

- 인증서 체인 검증:

`step certificate verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/호스트명.crt</span>` --roots `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/root-ca.crt</span>` --verbose`

- PEM 형식 인증서를 DER로 변환하여 디스크에 저장:

`step certificate format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인증서.pem</span>` --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인증서.der</span>

- 시스템 기본 신뢰 저장소에 루트 인증서를 설치하거나 제거:

`step certificate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/root-ca.crt</span>

- RSA/EC 개인 및 공개 키 쌍 생성 (개인 키 비밀번호 보호를 건너뛰려면 `--no-password --insecure` 추가):

`step crypto keypair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/공개_키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀_키</span>` --kty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">RSA|EC</span>

- 하위 명령에 대한 도움말 표시:

`step `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path|base64|certificate|completion|context|crl|crypto|oauth|ca|beta|ssh</span>` --help`
