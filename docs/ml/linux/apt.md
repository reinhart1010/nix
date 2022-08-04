---
layout: page
title: linux/apt (മലയാളം)
description: "ഡെബിയൻ അടിസ്ഥാനമാക്കിയുള്ള വിതരണങ്ങൾക്കായുള്ള പാക്കേജ് മാനേജുമെന്റ് യൂട്ടിലിറ്റി."
content_hash: 74b0fc099bf6faeea7277e8dedc1c0941fec3fad
related_topics:
  - title: বাংলা version
    url: /bn/linux/apt.html
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
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
---
# apt

ഡെബിയൻ അടിസ്ഥാനമാക്കിയുള്ള വിതരണങ്ങൾക്കായുള്ള പാക്കേജ് മാനേജുമെന്റ് യൂട്ടിലിറ്റി.
ഉബുണ്ടു പതിപ്പുകളിൽ 16.04ലും അതിനുശേഷമുള്ളതിലും സംവേദനാത്മകമായി ഉപയോഗിക്കുമ്പോൾ `apt-get` പകരം വയ്ക്കാൻ ശുപാർശ ചെയ്യുന്നതു.
കൂടുതൽ വിവരങ്ങൾ: <https://manpages.debian.org/latest/apt/apt.8.html>.

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
