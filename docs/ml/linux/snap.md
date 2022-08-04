---
layout: page
title: linux/snap (മലയാളം)
description: "സ്നാപ്പ് സെൽഫ് കൺറ്റൈൻഡ് പാക്കേജുകൾ നിയന്ത്രിക്കുവാനുള്ള യൂട്ടിലിറ്റി."
content_hash: 094ad893eb4ae6ea0ad0172609dd4b843e935211
related_topics:
  - title: বাংলা version
    url: /bn/linux/snap.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/snap.html
    icon: bi bi-globe
---
# snap

സ്നാപ്പ് സെൽഫ് കൺറ്റൈൻഡ് പാക്കേജുകൾ നിയന്ത്രിക്കുവാനുള്ള യൂട്ടിലിറ്റി.
`apt` നോട് സാദൃശ്യമുള്ളത്.
കൂടുതൽ വിവരങ്ങൾ: <https://manned.org/snap>.

- ഒരു പാക്കേജ് സെർച്ച് ചെയ്യുവാൻ:

`snap find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">പാക്കേജിന്റെ_പേര്</span>

- ഒരു പാക്കേജ് ഇൻസ്റ്റാൾ ചെയ്യുവാൻ:

`snap install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">പാക്കേജിന്റെ_പേര്</span>

- ഒരു പാക്കേജ് അപ്ഡേറ്റ് ചെയ്യുവാൻ:

`snap refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">പാക്കേജിന്റെ_പേര്</span>

- ഒരു പാക്കേജ് മറ്റൊരു ചാനലിലേക്ക് അപ്ഡേറ്റ് ചെയ്യുവാൻ (ട്രാക്ക്, റിസ്ക്, ബ്രാഞ്ച്):

`snap refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">പാക്കേജിന്റെ_പേര്</span>` --channel=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ചാനൽ</span>

- എല്ലാ പാക്കേജുകളും അപ്ഡേറ്റ് ചെയ്യുവാൻ:

`snap refresh`

- ഇൻസ്റ്റാൾ ചെയ്യപ്പെട്ട സോഫ്ട്‍വെയറുകൾ കാണുവാൻ:

`snap list`

- ഒരു പാക്കേജ് അൺഇൻസ്റ്റാൾ ചെയ്യുവാൻ:

`snap remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">പാക്കേജിന്റെ_പേര്</span>

- സിസ്റ്റത്തിലെ സ്നാപ്പ് ചേഞ്ചുകൾ അറിയുവാൻ:

`snap changes`
