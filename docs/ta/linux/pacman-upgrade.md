---
layout: page
title: linux/pacman-upgrade (தமிழ்)
description: "ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு."
content_hash: fbe7c0b5dcc65712efbd6b2d980c8d24b0b06c94
last_modified_at: 2023-11-13
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --upgrade

ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு.
இதையும் பார்க்கவும்: `pacman`.
மேலும் விவரத்திற்கு: <https://man.archlinux.org/man/pacman.8>.

- கோப்புகளிலிருந்து ஒன்று அல்லது அதற்கு மேற்பட்ட தொகுப்புகளை நிறுவவும்:

`sudo pacman --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு1.pkg.tar.zst/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு2.pkg.tar.zst/பாதை</span>

- கேட்காமல் ஒரு தொகுப்பை நிறுவவும்:

`sudo pacman --upgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு.pkg.tar.zst/பாதை</span>

- தொகுப்பு நிறுவலின் போது முரண்பட்ட கோப்புகளை மேலெழுதவும்:

`sudo pacman --upgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு.pkg.tar.zst/பாதை</span>

- சார்பு பதிப்பு சரிபார்ப்புகளைத் தவிர்த்து, தொகுப்பை நிறுவவும்:

`sudo pacman --upgrade --nodeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு.pkg.tar.zst/பாதை</span>

- பாதிக்கப்படக்கூடிய தொகுப்புகளைப் பட்டியலிடுங்கள் (எந்த தொகுப்புகளையும் நிறுவாது):

`pacman --upgrade --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு.pkg.tar.zst/பாதை</span>

- உதவியைக் காட்டு:

`pacman --upgrade --help`
