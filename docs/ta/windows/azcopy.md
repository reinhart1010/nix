---
layout: page
title: windows/azcopy (தமிழ்)
description: "அஸூர் கிளவுட் சேமிப்பகம் கணக்குகளில் பதிவேற்றுவதற்கான கோப்பு பரிமாற்றக் கருவி."
content_hash: 48efbb5d4654b8fe6bf46acd3775ed52afc69b2e
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/windows/azcopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# azcopy

அஸூர் கிளவுட் சேமிப்பகம் கணக்குகளில் பதிவேற்றுவதற்கான கோப்பு பரிமாற்றக் கருவி.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10>.

- அசூர் குத்தகைதாரரிடம் உள்நுழையவும்:

`azopy login`

- உள்ளூர் கோப்பைப் பதிவேற்றவும்:

`azcopy copy '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்_கோப்பு\பாதை</span>`' 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சேமிப்பு_கணக்கு_பெயர்</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குமிழ்_பெயர்</span>`'`

- `.txt` மற்றும் `.jpg` நீட்டிப்புகளுடன் கோப்புகளைப் பதிவேற்றவும்:

`azcopy copy '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்_அடைவு\பாதை</span>`' 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சேமிப்பு_கணக்கு_பெயர்</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>`' --include-pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt;*.jpg</span>`'`

- இரண்டு அசூர் சேமிப்பு கணக்குகளுக்கு இடையே நேரடியாக ஒரு கொள்கலனை நகலெடுக்கவும்:

`azcopy copy 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்_சேமிப்பு_கணக்கு_பெயர்</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>`' 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சேருமிடம்_சேமிப்பு_கணக்கு_பெயர்</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>`'`

- ஒரு உள்ளூர் கோப்பகத்தை ஒத்திசைக்கவும், மேலும் மூலத்தில் கோப்புகள் இல்லை என்றால் இலக்கில் உள்ள கோப்புகளை நீக்கவும்:

`azcopy sync '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்_அடைவு\பாதை</span>`' 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சேமிப்பு_கணக்கு_பெயர்</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>`' --recursive --delete-destination=true`

- விரிவான பயன்பாட்டுத் தகவலைக் காண்பி:

`azcopy --help`
