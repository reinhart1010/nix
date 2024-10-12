---
layout: page
title: common/cs-java (한국어)
description: "`java` 및 `java-home` 명령은 JVM을 가져오고 설치. `java` 명령으로도 설치됨."
content_hash: 7fdd587fc6b686cdc179c30b404e410dcdbed1a6
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/cs-java.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cs java

`java` 및 `java-home` 명령은 JVM을 가져오고 설치. `java` 명령으로도 설치됨.
더 많은 정보: <https://get-coursier.io/docs/cli-java>.

- coursier를 사용하여 Java 버전 표시:

`cs java -version`

- coursier를 사용하여 사용자 정의 속성으로 특정 Java 버전을 호출:

`cs java --jvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jvm_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jvm_버전</span>` -Xmx32m -X`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">다른_jvm_옵션</span>` -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/jar_이름.jar</span>

- coursier 기본 인덱스에 사용 가능한 모든 JVM을 나열:

`cs java --available`

- 시스템에 설치된 모든 JVM을 자신의 위치와 함께 나열:

`cs java --installed`

- 특정 JVM을 셸 인스턴스의 일회성 기본값으로 설정:

`cs java --jvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jvm_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jvm_버전</span>` --env`

- 기본 JVM 설정에 대한 변경 사항을 되돌림:

`eval "$(cs java --disable)"`

- 특정 JVM을 전체 시스템의 기본값으로 설정:

`cs java --jvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jvm_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jvm_버전</span>` --setup`
