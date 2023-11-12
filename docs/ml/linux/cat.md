---
layout: page
title: linux/cat (മലയാളം)
description: "ഫയലുകൾ പ്രിന്റ് ചെയ്യുവാനും സംയോജിപ്പിക്കുവാനുമുള്ള കമാൻഡ്."
content_hash: 4bb1fee104fdc83e49dc4586ea39a0f7cc0c5a86
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/cat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cat

ഫയലുകൾ പ്രിന്റ് ചെയ്യുവാനും സംയോജിപ്പിക്കുവാനുമുള്ള കമാൻഡ്.
കൂടുതൽ വിവരങ്ങൾ: <https://www.gnu.org/software/coreutils/cat>.

- ഫയലിന്റെ ഉള്ളടക്കം സ്റ്റാൻഡേർഡ് ഔട്പുട്ടിലേക്ക് പ്രിന്റ് ചെയ്യുവാൻ:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയലിലേക്കുള്ള/പാത</span>

- പല ഫയലുകൾ സംയോജിപ്പിച് ഒരു ഔട്ട്പുട്ട് ഫയലുണ്ടാക്കുവാൻ:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയൽ1/ലേക്കുള്ള/പാത ഫയൽ2/ലേക്കുള്ള/പാത ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഔട്ട്പുട്ട്_ഫയൽ/ലേക്കുള്ള/പാത</span>

- പല ഫയലുകൾ അപ്പെൻഡ് ചെയ്‌ത്‌ ഒരു ഔട്ട്പുട്ട് ഫയലുണ്ടാക്കുവാൻ:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയൽ1/ലേക്കുള്ള/പാത ഫയൽ2/ലേക്കുള്ള/പാത ...</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഔട്ട്പുട്ട്_ഫയൽ/ലേക്കുള്ള/പാത</span>

- ഫയലിന്റെ ഉള്ളടക്കം അൺബഫേർഡ് മോഡിൽ ഒരു ഔട്ട്പുട്ട് ഫയലിലേക്ക് കോപ്പിചെയ്യുവാൻ:

`cat -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty12</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty13</span>

- `stdin` ഫയലിലേക്ക് എഴുതുവാൻ:

`cat - > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയലിലേക്കുള്ള/പാത</span>

- ഔട്ട്പുട്ട് ലൈനുകൾ നമ്പർ ചെയ്യുവാൻ:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയലിലേക്കുള്ള/പാത</span>

- വൈറ്റ്സ്പേസും പ്രിന്റ് ചെയ്യപ്പെടാത്ത മറ്റ് ചിഹ്നങ്ങളും കാണുവാൻ (ASCII അല്ലെങ്കിൽ `M-` ആരംഭത്തിൽ ചേർക്കുക):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ഫയലിലേക്കുള്ള/പാത</span>
