---
layout: page
title: linux/pacman (മലയാളം)
description: "ആർച്ച് ലിന്ക്സിന്റെ പാക്കേജ് മാനേജുമെന്റ് യൂട്ടിലിറ്റി."
content_hash: e62ba447d405b43a36ebffde3762835d38ab63a1
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman

ആർച്ച് ലിന്ക്സിന്റെ പാക്കേജ് മാനേജുമെന്റ് യൂട്ടിലിറ്റി.
ഇതും കാണുക: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
കൂടുതൽ വിവരങ്ങൾ: <https://man.archlinux.org/man/pacman.8>.

- ഇൻസ്റ്റാൾ ചെയ്‌ത എല്ലാ പാക്കേജും അപ്‌ഡേറ്റു ചെയ്യുക:

`sudo pacman -Syu`

- പുതിയ പാക്കേജ് ഇൻസ്റ്റാൾ ചെയ്യുക:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">പാക്കേജ്</span>

- ഒരു പാക്കേജും അത് ആശ്രയിക്കുന്ന മറ്റ് പാക്കേജുകളെയും കളയുക:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">പാക്കേജ്</span>

- പാക്കേജ് ഡാറ്റാബേസിൽ ഒരു സൂചകപദം അല്ലെങ്കിൽ റെഗുലർ എക്സ്പ്രെഷൻ വെച്ച് തിരയുക:

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">സെർച്ച് പാറ്റേൺ</span>`"`

- ഇൻസ്റ്റാൾ ചെയ്‌ത എല്ലാ പാക്കേജുകളും അതിന്റെ പതിപ്പും കാണിക്കുക:

`pacman -Q`

- നേരെ ഇൻസ്റ്റാൾ ചെയ്ത പാക്കേജ്‌സ് മാത്റം കാണിക്കുക:

`pacman -Qe`

- ഏത് പാക്കേജാണ് ഒരു ഫയലിന്റെ ഉടമ എന്ന് കണ്ടുപിടിക്കാൻ:

`pacman -Qo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയലിന്റെ പേര്</span>

- പാക്കേജ് ക്യാഷ് കാലിയാക്കി സ്റ്റോറേജ്‌ മുക്തമാക്കുക:

`sudo pacman -Scc`
