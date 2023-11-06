---
layout: page
title: common/docker-compose (नेपाली)
description: "बहु कन्टेनर डकर अनुप्रयोगहरू चलाउनुहोस् र व्यवस्थापन गर्नुहोस्।"
content_hash: eeb20c3602c7d25394042b68aede2f95c0dd2351
last_modified_at: 2023-11-06
related_topics:
  - title: Deutsch version
    url: /de/common/docker-compose.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-compose.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker-compose.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-compose.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker-compose.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-compose.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-compose.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
---
# docker compose

बहु कन्टेनर डकर अनुप्रयोगहरू चलाउनुहोस् र व्यवस्थापन गर्नुहोस्।
थप जानकारी: <https://docs.docker.com/compose/reference/>।

- सबै चलिरहेको कन्टेनरहरू सूचीबद्ध गर्नुहोस्:

`docker compose ps`

- हालको डाइरेक्टरीबाट `docker-compose.yml` फाइल प्रयोग गरेर पृष्ठभूमिमा सबै कन्टेनरहरू सिर्जना गर्नुहोस् र सुरु गर्नुहोस्:

`docker compose up --detach`

- सबै कन्टेनरहरू सुरु गर्नुहोस्, आवश्यक भएमा पुन: निर्माण गर्नुहोस्:

`docker compose up --build`

- प्रोजेक्तको नाम निर्दिष्ट गरेर र वैकल्पिक रचना फाइल प्रयोग गरेर सबै कन्टेनरहरू सुरु गर्नुहोस्:

`docker compose -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">परियोजनाको_नाम</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल/को/पथ</span>` up`

- चलिरहेको सबै कन्टेनरहरू रोक्नुहोस्:

`docker compose stop`

- सबै कन्टेनरहरू, नेटवर्कहरू, छविहरू, र भोल्युमहरू हटाउनुहोस् र रोक्नुहोस्:

`docker compose down --rmi all --volumes`

- सबै कन्टेनरहरूको लागि लगहरू फलो गर्नुहोस्:

`docker compose logs --follow`

- विशेष कन्टेनरको लागि लगहरू पछ्याउनुहोस्:

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">कन्टेनर_नाम</span>
