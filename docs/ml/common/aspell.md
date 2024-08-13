---
layout: page
title: common/aspell (മലയാളം)
description: "ഒരു ഇന്ററാക്ടിവ് സ്പെൽ ചെക്കർ."
content_hash: c551c70bb243f8e48c5c95912309ab3ef8b96a1d
last_modified_at: 2024-08-13
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aspell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aspell

ഒരു ഇന്ററാക്ടിവ് സ്പെൽ ചെക്കർ.
കൂടുതൽ വിവരങ്ങൾ: <http://aspell.net/>.

- ഒരു ഫയലിലെ തെറ്റായ പദങ്ങൾ കണ്ടെത്തുവാൻ:

`aspell check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയലിലേക്കുള്ള/പാത</span>

- സ്റ്റാൻഡേഡ് ഇൻപുറ്റിൽ നിന്ന് തെറ്റായ പദങ്ങൾ കണ്ടെത്തുവാൻ:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയൽ</span>` | aspell list`

- പദശുദ്ധി കണ്ടെത്താൻ ഉപയോഗിക്കാവുന്ന ഭാഷാ-നിഘണ്ടുകൾ കാണുവാൻ:

`aspell dicts`

- മറ്റൊരു ഭാഷയുടെ പദശുദ്ധി കാണുവാൻ (ISO 639 ഭാഷാ-കോഡ് അനുസൃതം):

`aspell --lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cs</span>

- പേഴ്സണൽ ലിസ്റ്റിൽ ഇല്ലാത്തതും സ്റ്റാൻഡേഡ് ഇൻപുറ്റിൽ ഉള്ളതുമായ തെറ്റുകൾ കാണുവാൻ:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയൽ</span>` | aspell --personal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">പേഴ്സണൽ-വേർഡ്-ലിസ്റ്റ്.pws</span>` list`
