---
layout: page
title: common/jmap (한국어)
description: "Java 메모리 맵 도구."
content_hash: f8523ac341165852d02db3f51fe5612575e3134d
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jmap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/jmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jmap

Java 메모리 맵 도구.
더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/jmap.html>.

- Java 프로세스에 대한 공유 객체 매핑 출력 (pmap과 유사한 출력):

`jmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- 힙 요약 정보 출력:

`jmap -heap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명.jar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- 타입별 힙 사용량 히스토그램 출력:

`jmap -histo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- 힙의 내용을 바이너리 파일로 덤프하여 jhat로 분석:

`jmap -dump:format=b,file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- 힙의 활성 객체를 바이너리 파일로 덤프하여 jhat로 분석:

`jmap -dump:live,format=b,file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>
