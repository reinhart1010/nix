---
layout: page
title: common/pass (한국어)
description: "비밀번호나 기타 민감한 데이터를 저장하고 읽기."
content_hash: 1e0af401012a318b63c282cefbe11faa94706c5c
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/common/pass.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pass

비밀번호나 기타 민감한 데이터를 저장하고 읽기.
모든 데이터는 GPG로 암호화되며, Git 저장소로 관리됩니다.
더 많은 정보: <https://www.passwordstore.org>.

- 하나 이상의 GPG ID를 사용하여 저장소 초기화 (또는 재암호화):

`pass init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpg_id_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpg_id_2</span>

- 새 비밀번호 및 추가 정보 저장 (새 줄에서 Ctrl + D를 눌러 완료):

`pass insert --multiline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터</span>

- 항목 편집:

`pass edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터</span>

- 비밀번호(데이터 파일의 첫 번째 줄)를 클립보드에 복사:

`pass -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터</span>

- 전체 저장소 트리 나열:

`pass`

- 지정된 길이의 새로운 무작위 비밀번호 생성 및 클립보드에 복사:

`pass generate -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>

- 새로운 Git 저장소 초기화 (pass에 의해 이루어진 모든 변경 사항은 자동으로 커밋됨):

`pass git init`

- 비밀번호 저장소를 대신하여 Git 명령 실행:

`pass git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
