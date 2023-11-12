---
layout: page
title: common/virsh-undefine (한국어)
description: "가상 머신을 삭제합니다."
content_hash: 1de951e144e030fc9170caaceda5e0935122b726
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/virsh-undefine.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-undefine.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh-undefine

가상 머신을 삭제합니다.
더 많은 정보: <https://manned.org/virsh>.

- 가상 머신 구성 파일만 삭제:

`virsh undefine --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상머신_이름</span>

- 구성 파일 및 모든 관련 스토리지 불륨을 삭제:

`virsh undefine --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상머신_이름</span>` --remove-all-storage`

- 대상 이름 또는 소스 이름 (`virsh domblklist` 명령에서 얻은 이름)을 사용하여 구성 파일과 지정된 스토리지 볼륨을 삭제:

`virsh undefine --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상머신_이름</span>` --storage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sda,경로/대상/소스</span>
