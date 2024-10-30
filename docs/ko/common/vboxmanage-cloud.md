---
layout: page
title: common/vboxmanage-cloud (한국어)
description: "클라우드 인스턴스 및 이미지를 관리하기 위한 VirtualBox 명령줄 인터페이스."
content_hash: 4f33a8452c67b475b599a4a900af19269efd95b9
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/vboxmanage-cloud.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vboxmanage-cloud

클라우드 인스턴스 및 이미지를 관리하기 위한 VirtualBox 명령줄 인터페이스.
더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-cloud>.

- 지정된 구획에 속하는 특정 상태의 인스턴스 나열:

`VBoxManage cloud --provider=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제공자_이름</span>` --profile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>` list instances --state=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">running|terminated|paused</span>` --compartment-id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구획_id</span>

- 새 인스턴스 생성:

`VBoxManage cloud --provider=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제공자_이름</span>` --profile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>` instance create --domain-name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>` --image-id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_id</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--옵션...</span>

- 특정 인스턴스에 대한 정보 수집:

`VBoxManage cloud --provider=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제공자_이름</span>` --profile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>` instance info --id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">고유_id</span>

- 인스턴스 종료:

`VBoxManage cloud --provider=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제공자_이름</span>` --profile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>` instance terminate --id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">고유_id</span>

- 특정 구획 및 상태의 이미지 나열:

`VBoxManage cloud --provider=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제공자_이름</span>` --profile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>` list images --compartment-id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구획_id</span>` --state=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">상태_이름</span>

- 새 이미지 생성:

`VBoxManage cloud --provider=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제공자_이름</span>` --profile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>` image create --instance-id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_id</span>` --display-name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표시_이름</span>` --compartment-id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구획_id</span>

- 특정 이미지에 대한 정보 검색:

`VBoxManage cloud --provider=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제공자_이름</span>` --profile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>` image info --id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">고유_id</span>

- 이미지 삭제:

`VBoxManage cloud --provider=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제공자_이름</span>` --profile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>` image delete --id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">고유_id</span>
