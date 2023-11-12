---
layout: page
title: common/git (മലയാളം)
description: "പ്രോഗ്രാമുകളുടെ പല പതിപ്പുകൾ പലയിടങ്ങളിലായി സൂക്ഷിക്കുവാനും നിയന്ത്രിക്കുവാനും ഉള്ള വികേന്ദ്രീകൃത പതിപ്പ് നിയന്ത്രണ സംവിധാനം."
content_hash: 30c357d7899b1f0b0208eff5b5eae2aa3d50db3d
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/git.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/common/git.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git

പ്രോഗ്രാമുകളുടെ പല പതിപ്പുകൾ പലയിടങ്ങളിലായി സൂക്ഷിക്കുവാനും നിയന്ത്രിക്കുവാനും ഉള്ള വികേന്ദ്രീകൃത പതിപ്പ് നിയന്ത്രണ സംവിധാനം.
`commit`, `add`, `branch`, `checkout`, `push` മുതലായ ചില ഉപകമാൻഡുകൾക്ക് അവരുടേതായ ഡോക്യുമെന്റേഷൻ ഉണ്ട്, `tldr git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഉപകമാൻഡ്</span> വഴി അവ കാണാൻ കഴിയും.
കൂടുതൽ വിവരങ്ങൾ: <https://git-scm.com/>.

- നിങ്ങൾ ഉപയോഗിക്കുന്ന ഗിറ്റിന്റെ പതിപ്പ് പരിശോധിക്കാൻ:

`git --version`

- സഹായ നിർദേശങ്ങൾ കാണുവാൻ:

`git --help`

- `clone`, `add`, `push`, `log` പോലുള്ള ഉപകമാൻഡുകളുടെ സഹായ നിർദേശങ്ങൾ കാണുവാൻ:

`git help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഉപകമാൻഡ്</span>

- ഗിറ്റ് ഉപകമാന്റുകൾ എക്സിക്യൂട്ട് ചെയ്യുവാൻ:

`git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഉപകമാൻഡ്</span>

- ഒരു ഇഷ്‌ടാനുസൃത ശേഖരണത്തിന്റെ/റിപ്പോസിറ്ററിയുടെ റൂട്ട് പാതയിൽ ഒരു Git സബ്‌കമാൻഡ് എക്‌സിക്യൂട്ട് ചെയ്യാൻ:

`git -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ശേഖരണത്തിലേക്കുള്ള/പാത</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഉപകമാൻഡ്</span>

- ഒരു കോൺഫിഗറേഷൻ സെറ്റ് ഉപയോഗിച്ച് Git ഉപകമാൻഡ് എക്സിക്യൂട്ട് ചെയ്യാൻ:

`git -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">കോൺഫിഗ്.പേര്</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">മൂല്യം</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഉപകമാൻഡ്</span>
