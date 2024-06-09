---
layout: page
title: common/magick-mogrify (Nederlands)
description: "Voer bewerkingen uit op meerdere afbeeldingen, zoals het wijzigen van de grootte, bijsnijden, omkeren en effecten toevoegen."
content_hash: 6b250b12324836a5da880af26af652936c4e646a
last_modified_at: 2024-06-09
related_topics:
  - title: English version
    url: /en/common/magick-mogrify.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick mogrify

Voer bewerkingen uit op meerdere afbeeldingen, zoals het wijzigen van de grootte, bijsnijden, omkeren en effecten toevoegen.
Wijzigingen worden direct toegepast op het originele bestand.
Bekijk ook: `magick`.
Meer informatie: <https://imagemagick.org/script/mogrify.php>.

- Wijzig de grootte van alle JPEG afbeeldingen in de map naar 50% van hun oorspronkelijke grootte:

`magick mogrify -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- Wijzig de grootte van alle afbeeldingen die beginnen met `DSC` naar 800x600:

`magick mogrify -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DSC*</span>

- Converteer alle PNG's in de map naar JPEG:

`magick mogrify -format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- Halveer de verzadiging van alle afbeeldingsbestanden in de huidige map:

`magick mogrify -modulate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100,50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- Verdubbel de helderheid van alle afbeeldingsbestanden in de huidige map:

`magick mogrify -modulate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>
