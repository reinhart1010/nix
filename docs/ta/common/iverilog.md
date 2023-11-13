---
layout: page
title: common/iverilog (தமிழ்)
description: "வெரிலாக் HDL (IEEE-1364) குறியீட்டை உருவகப்படுத்துதலுக்காக இயங்கக்கூடிய நிரல்களாக முன்செயலாக்கி தொகுக்கிறது."
content_hash: 6805e011fd46b333f35c9acd497649140d474962
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/common/iverilog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iverilog

வெரிலாக் HDL (IEEE-1364) குறியீட்டை உருவகப்படுத்துதலுக்காக இயங்கக்கூடிய நிரல்களாக முன்செயலாக்கி தொகுக்கிறது.
மேலும் விவரத்திற்கு: <https://github.com/steveicarus/iverilog>.

- ஒரு மூல கோப்பை இயங்கக்கூடியதாக தொகுக்கவும்:

`iverilog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.v/பாதை</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செயல்படுத்தக்கூடியதின்/பாதை</span>

- அனைத்து எச்சரிக்கைகளையும் காண்பிக்கும் போது ஒரு மூலக் கோப்பை இயங்கக்கூடியதாக தொகுக்கவும்:

`iverilog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.v/பாதை</span>` -Wall -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செயல்படுத்தக்கூடியதின்/பாதை</span>

- VVP இயக்க நேரத்தைப் பயன்படுத்தி வெளிப்படையாக தொகுத்து இயக்கவும்:

`iverilog -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செயல்படுத்தக்கூடியதின்/பாதை</span>` -tvvp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.v/பாதை</span>

- வேறொரு பாதையிலிருந்து வெரிலாக் நூலகக் கோப்புகளைப் பயன்படுத்தி தொகுக்கவும்:

`iverilog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.v/பாதை</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செயல்படுத்தக்கூடியதின்/பாதை</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நூலகம்_கோப்பகம்/பாதை</span>

- தொகுக்காமல் வெரிலாக் குறியீட்டை முன்கூட்டியே செயலாக்கவும்:

`iverilog -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.v/பாதை</span>
