---
layout: page
title: common/chmod (മലയാളം)
description: "ഒരു ഫയലിന്റെയോ ഡയറക്ടറിയുടെയോ പ്രവേശന അനുമതികൾ മാറ്റുക."
content_hash: e68e4119ac378e64c0a0d1e08a8cb7ae6bb00291
last_modified_at: 2023-10-08
related_topics:
  - title: Deutsch version
    url: /de/common/chmod.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chmod.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chmod.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/chmod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chmod.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/chmod.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chmod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chmod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chmod.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chmod.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/chmod.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/chmod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/chmod.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/chmod.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chmod

ഒരു ഫയലിന്റെയോ ഡയറക്ടറിയുടെയോ പ്രവേശന അനുമതികൾ മാറ്റുക.
കൂടുതൽ വിവരങ്ങൾ: <https://www.gnu.org/software/coreutils/chmod>.

- ഒരു ഫയൽ കൈവശമുള്ള [u]ser-ന് അത് e[x]ecute ചെയ്യാനുള്ള അവകാശം നൽകുക:

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയലിലേക്കുള്ള/പാത</span>

- ഒരു ഫയൽ/ഡയറക്‌ടറിയിലേക്ക് [r]ead, [w]rite എന്നിവയ്ക്കുള്ള [u]ser അവകാശങ്ങൾ നൽകുക:

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയലിലേക്കോ_ഡയറക്ടറിയിലേക്കോ/ഉള്ള/പാത</span>

- [g]roup ൽ നിന്ന് e[x]ecutable അവകാശങ്ങൾ നീക്കം ചെയ്യുക:

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയലിലേക്കുള്ള/പാത</span>

- എല്ലാ ഉപയോക്താക്കൾക്കും [r]ead, e[x]ecute എന്നിവയ്ക്കുള്ള അവകാശങ്ങൾ നൽകുക:

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയലിലേക്കുള്ള/പാത</span>

- [o]thers മറ്റുള്ളവർക്കും (ഫയൽ ഉടമയുടെ ഗ്രൂപ്പിലല്ല) [g]roup ൽ അതേ അവകാശങ്ങൾ നൽകുക:

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയലിലേക്കുള്ള/പാത</span>

- [o]thers മറ്റുള്ളവരിൽ നിന്ന് എല്ലാ അവകാശങ്ങളും നീക്കം ചെയ്യുക:

`chmod o= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയലിലേക്കുള്ള/പാത</span>

- ആവർത്തനാനുമതികൾ മാറ്റുക [g]roupൽ  [o]thers മറ്റുള്ളവർക്കും [w]rite റൈറ്റ് ചെയ്യാനുള്ള കഴിവ് നൽകുന്നു:

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഡയറക്ടറിയിലേക്കുള്ള/പാത</span>

- ഫയലുകൾക്കുള്ള [a]ll എല്ലാ ഉപയോക്താക്കൾക്കും [r]ead അനുമതികളും ഒരു ഡയറക്‌ടറിയിലെ ഉപ ഡയറക്‌ടറികൾക്ക് e[x]ecute എക്‌ക്യൂട്ട് അനുമതികളും ആവർത്തിച്ച് നൽകുക:

`chmod -R a+rX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഡയറക്ടറിയിലേക്കുള്ള/പാത</span>
