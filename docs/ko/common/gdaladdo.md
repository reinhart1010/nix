---
layout: page
title: common/gdaladdo (한국어)
description: "래스터 데이터세트의 개요 이미지를 구축."
content_hash: ba505beb831ab1b1e6bd229ebd5c6d590a06cf5f
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gdaladdo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gdaladdo

래스터 데이터세트의 개요 이미지를 구축.
더 많은 정보: <https://gdal.org/programs/gdaladdo.html>.

- "평균" 리샘플링([r]esampling) 방법을 사용하여 래스터 데이터세트의 개요 이미지를 구축:

`gdaladdo -r average `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.tif</span>
