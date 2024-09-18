---
layout: page
title: linux/apt (മലയാളം)
description: "ഡെബിയൻ അടിസ്ഥാനമാക്കിയുള്ള വിതരണങ്ങൾക്കായുള്ള പാക്കേജ് മാനേജുമെന്റ് യൂട്ടിലിറ്റി."
content_hash: 61f8617c282c81abd01b70d1b4630740c6e7f8bf
last_modified_at: 2024-09-18
related_topics:
  - title: العربية version
    url: /ar/linux/apt.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/apt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt

ഡെബിയൻ അടിസ്ഥാനമാക്കിയുള്ള വിതരണങ്ങൾക്കായുള്ള പാക്കേജ് മാനേജുമെന്റ് യൂട്ടിലിറ്റി.
ഉബുണ്ടു പതിപ്പുകളിൽ 16.04ലും അതിനുശേഷമുള്ളതിലും സംവേദനാത്മകമായി ഉപയോഗിക്കുമ്പോൾ `apt-get` പകരം വയ്ക്കാൻ ശുപാർശ ചെയ്യുന്നതു.
കൂടുതൽ വിവരങ്ങൾ: <https://manned.org/apt.8>.

- ലഭ്യമായ പാക്കേജുകളുടെയും പതിപ്പുകളുടെയും പട്ടിക അപ്‌ഡേറ്റുചെയ്യുക (മറ്റ് `apt` കമാൻഡുകൾക്ക് മുമ്പ് ഇത് പ്രവർത്തിപ്പിക്കാൻ ശുപാർശ ചെയ്യുന്നു):

`sudo apt update`

- പാക്കേജിനായി തിരയുക:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">പാക്കേജ്</span>

- ഒരു പാക്കേജിന്റെ വിവരങ്ങൾ കാണിക്കുക:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">പാക്കേജ്</span>

- ഒരു പാക്കേജ് ഇൻസ്റ്റാൾ ചെയ്യുക, അല്ലെങ്കിൽ ലഭ്യമായ ഏറ്റവും പുതിയ പതിപ്പിലേക്ക് അപ്‌ഡേറ്റ് ചെയ്യുക:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">പാക്കേജ്</span>

- ഒരു പാക്കേജ് നീക്കംചെയ്യുക (പകരം `purge` ഉപയോഗിക്കുന്നത് അതിന്റെ കോൺഫിഗറേഷൻ ഫയലുകളും നീക്കംചെയ്യുന്നു):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">പാക്കേജ്</span>

- ഇൻസ്റ്റാളുചെയ്‌ത എല്ലാ പാക്കേജുകളും ലഭ്യമായ ഏറ്റവും പുതിയ പതിപ്പുകളിലേക്ക് അപ്‌ഗ്രേഡുചെയ്യുക:

`sudo apt upgrade`

- എല്ലാ പാക്കേജുകളും കാണിക്കുക:

`apt list`

- ഇൻസ്റ്റാൾ ചെയ്ത പാക്കേജുകൾ കാണിക്കുക:

`apt list --installed`
