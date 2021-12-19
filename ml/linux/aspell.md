---
layout: page
title: linux/aspell (മലയാളം)
description: "ഒരു ഇന്ററാക്ടിവ് സ്പെൽ ചെക്കർ."
content_hash: 37ce9313c22dcf4aa4630a785caf1a7f184d3a26
related_topics:
  - title: Deutsch version
    url: /de/linux/aspell.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aspell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aspell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aspell.html
    icon: bi bi-globe
---
# aspell

ഒരു ഇന്ററാക്ടിവ് സ്പെൽ ചെക്കർ.
കൂടുതൽ വിവരങ്ങൾ: <http://aspell.net/>.

- ഒരു ഫയലിലെ തെറ്റായ പദങ്ങൾ കണ്ടെത്തുവാൻ:

`aspell check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയലിന്റെ/പാത്/</span>

- സ്റ്റാൻഡേഡ് ഇൻപുറ്റിൽ നിന്ന് തെറ്റായ പദങ്ങൾ കണ്ടെത്തുവാൻ:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയൽ</span>` | aspell list`

- പദശുദ്ധി കണ്ടെത്താൻ ഉപയോഗിക്കാവുന്ന ഭാഷാ-നിഘണ്ടുകൾ കാണുവാൻ:

`aspell dicts`

- മറ്റൊരു ഭാഷയുടെ പദശുദ്ധി കാണുവാൻ (ISO 639 ഭാഷാ-കോഡ് അനുസൃതം):

`aspell --lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cs</span>

- പേഴ്സണൽ ലിസ്റ്റിൽ ഇല്ലാത്തതും സ്റ്റാൻഡേഡ് ഇൻപുറ്റിൽ ഉള്ളതുമായ തെറ്റുകൾ കാണുവാൻ:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയൽ</span>` | aspell --personal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">പേഴ്സണൽ-വേർഡ്-ലിസ്റ്റ്.pws</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ലിസ്റ്റ്</span>
