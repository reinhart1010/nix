---
layout: page
title: common/todoist (தமிழ்)
description: "கட்டளை வரியிலிருந்து Todoist ஐ அணுகவும்."
content_hash: baf4b6dddfc42c0c1ad1c20696ed4cfb40fbb376
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/todoist.html
    icon: bi bi-globe
  - title: română version
    url: /ro/common/todoist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# todoist

கட்டளை வரியிலிருந்து Todoist ஐ அணுகவும்.
மேலும் விவரத்திற்கு: <https://github.com/sachaos/todoist>.

- பணியைச் சேர்க்கவும்:

`todoist add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பணி_பெயர்</span>`"`

- லேபிள், திட்டம் மற்றும் நிலுவைத் தேதியுடன் அதிக முன்னுரிமை பணியைச் சேர்க்கவும்:

`todoist add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பணி_பெயர்</span>`" --priority `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --label-ids "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">லேபிள்_ஐடி</span>`" --project-name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">திட்டத்தின்_பெயர்</span>`" --date "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நாளை காலை 9 மணி</span>`"`

- Aவிரைவு பயன்முறையில் லேபிள், திட்டப்பணி மற்றும் நிலுவைத் தேதியுடன் அதிக முன்னுரிமைப் பணியைச் சேர்க்கவும்:

`todoist quick '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">திட்டத்தின்_பெயர்</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நாளை காலை 9 மணி</span>`" p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பணி_பெயர்</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">லேபிள்_பெயர்</span>`'`

- தலைப்பு மற்றும் வண்ணத்துடன் அனைத்து பணிகளையும் பட்டியலிடுங்கள்:

`todoist --header --color list`

- அனைத்து உயர் முன்னுரிமைப் பணிகளையும் பட்டியலிடுங்கள்:

`todoist list --filter p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- குறிப்பிடப்பட்ட லேபிளைக் கொண்ட இன்றைய பணிகளை அதிக முன்னுரிமையுடன் பட்டியலிடுங்கள்:

`todoist list --filter '(@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">லேபிள்_பெயர்</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">இன்று</span>`) & p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`'`
