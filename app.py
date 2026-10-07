from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# ----------------------------------------------------------------- ДЕРЕКТЕР
SITE = {
    "title": "Тұлға және дәуір: цифрлық тарихи портрет — М. М. Оразалиев",
    "brand": "Тарихи Портрет",
    "short_name": "М. Оразалиев",
    "full_name": "Молдияр Молыбайұлы Оразалиев",
    "subtitle": "Әділет генерал-майоры, Тәуелсіз Қазақстанның құқық қорғау жүйесінің негізін қалаушылардың бірі",
}

NAV = [
    ("biography", "Өмірбаяны"),
    ("impact", "Дәуір мен Ықпал"),
    ("reform", "Ғылым мен Реформа"),
    ("human", "Адами келбеті"),
    ("archive", "Цифрлық Архив"),
]

BADGES = [
    ("star", "Генерал-майор"),
    ("graduation-cap", "Заң ғылымдарының кандидаты"),
    ("shield-check", "IІМ ардагері"),
]

STATS = [
    {"counter": 40, "suffix": "+ жыл", "label": "Қоғамдық қауіпсіздік сақшысы"},
    {"counter": 1996, "suffix": " ж.", "label": "Генерал-майор шені берілген жыл"},
    {"text": "Оңтүстік, Алматы, Қостанай", "label": "Басқарған өңірлік ІІД-лер"},
]

TIMELINE = [
    {"year": "1974", "icon": "graduation-cap",
     "title": "Қарағанды Жоғары мектебін аяқтау",
     "text": "Қарағанды Жоғары мектебін аяқтап, жедел уәкілдік қызметті бастады. Бұл — 40 жылдан астам созылған қоғамдық қауіпсіздік жолының бастауы.",
     "context": "Кеңестік құқық қорғау жүйесі кезеңі"},
    {"year": "1990-жылдар", "icon": "gavel",
     "title": "Мемлекеттік тергеу комитеті және ұйымдасқан қылмыспен күрес",
     "text": "Тәуелсіздіктің алғашқы онжылдығында Мемлекеттік тергеу комитетінде (ГСК) қызмет етіп, ұйымдасқан қылмыспен күреске қатысты. Өтпелі кезеңде қоғамдық тәртіпті сақтау үшін аса маңызды сала болды. 1996 жылы генерал-майор шені берілді.",
     "context": "Тәуелсіз Қазақстанның мемлекеттілігі қалыптасқан кезең"},
    {"year": "2000-жылдар", "icon": "building-2",
     "title": "ІІМ Бірінші вице-министрі, Алматы қ. ІІББ бастығы, заң институтының басшысы",
     "text": "ІІМ Бірінші вице-министрі, Алматы қ. ІІББ бастығы және Қарағанды заң институтының басшысы қызметтерін атқарды. Басқару тәжірибесін кадр даярлау ісімен ұштастырды.",
     "context": "Институционалдық реформалар және кадр даярлау"},
    {"year": "ТМД деңгейі", "icon": "globe",
     "title": "Терроризмге қарсы орталықтағы халықаралық қызмет",
     "text": "ТМД-ның Терроризмге қарсы орталығында халықаралық деңгейде қызмет етіп, өңірлік қауіпсіздікті нығайтуға үлес қосты.",
     "context": "Экстремизм мен терроризмге қарсы өңірлік әрекеттестік"},
]

IMPACT = [
    {"n": "01", "icon": "shield", "title": "Криминогендік ахуалды тұрақтандыру",
     "text": "90-жылдардағы өтпелі кезеңдегі ел ішіндегі тәртіпті қамтамасыз ету."},
    {"n": "02", "icon": "book-open", "title": "Заңнама және Ғылым",
     "text": "Орташа ауырлықтағы қылмыстар бойынша зерттеулері, заңнамалық ұсыныстары."},
    {"n": "03", "icon": "users", "title": "Кадрлық мектеп",
     "text": "Жаңа буын полиция офицерлерін тәрбиелеудегі білім беру реформасы."},
    {"n": "04", "icon": "globe", "title": "Халықаралық қауіпсіздік",
     "text": "ТМД кеңістігіндегі экстремизм мен терроризмге қарсы әрекеттестік."},
]

PRINCIPLES = [
    {"icon": "scale", "t": "Заң үстемдігі",
     "d": "Заң — барлығына бірдей. Лауазымы мен шені қандай болса да, ешкім заңнан жоғары тұрмайды.",
     "q": "Заң жеке қарым-қатынас пен қысымнан жоғары тұрмаса, қоғамда не болады?"},
    {"icon": "shield-check", "t": "Офицерлік ар-намыс",
     "d": "Ар-намыс — қызмет борышын адал, сенімді және сөз бен істің бірлігімен атқару.",
     "q": "Ешкім көрмесе де, дұрыс шешім қабылдау неге маңызды?"},
    {"icon": "heart-handshake", "t": "Қоғам алдындағы жауапкершілік",
     "d": "Құқық қорғаушының басты міндеті — адамдардың тыныштығы мен қауіпсіздігін сақтау.",
     "q": "Қоғамның полицияға деген сенімін не қалыптастырады?"},
    {"icon": "book-open-check", "t": "Білім және тәрбие",
     "d": "Жаңа буын кадрлар білімді де адамгершілікті болуы тиіс. Тәрбие — реформаның өзегі.",
     "q": "Жақсы маман мен жақсы азаматтың айырмасы қандай?"},
]

QUIZ = [
    {"q": "Генерал-майор шені қай жылы берілді?", "o": ["1974", "1996", "2005"], "a": 1},
    {"q": "Қай жылы Қарағанды Жоғары мектебін аяқтап, жедел уәкілдік қызметті бастады?",
     "o": ["1974", "1991", "2001"], "a": 0},
    {"q": "Төмендегілердің қайсысы жобадағы тұлғаның музыкалық қызығушылығына жатады?",
     "o": ["Домбыра мен қобыз", "Гитара мен барабан", "Фортепиано"], "a": 1},
    {"q": "Тұлға қай өңірлердің ІІД-лерін басқарды?",
     "o": ["Оңтүстік, Алматы, Қостанай", "Астана, Ақтөбе", "Батыс және Шығыс"], "a": 0},
]

MODALS = {
    "music": {"icon": "guitar", "title": "Музыкаға деген құштарлық", "body": [
        "Қатаң қызмет пен жауапкершілікпен қатар Молдияр Молыбайұлы музыкаға ерекше қызығушылық танытты.",
        "Ол гитара мен барабанда ойнап, әуендер жазумен айналысты. Бұл — тәртіп пен шығармашылықтың бір адамда үйлесуінің көрінісі.",
        "Талқылау сұрағы: өнер адамның қызметіне және мінезіне қалай әсер етеді?"]},
    "family": {"icon": "users-round", "title": "Отбасылық мұра", "body": [
        "Ол педагогтар отбасынан шықты: білімге, тәрбиеге және еңбекке құрмет — ең алғашқы үлгі болды.",
        "Кейін өз отбасында офицерлік династия құрды. Қызмет үлгісі мен адалдық дәстүрі ұрпақтан ұрпаққа жалғасты.",
        "Талқылау сұрағы: отбасы мен тәрбие тұлғаның таңдауына қандай әсер етеді?"]},
}

# ----------------------------------------------------------------- ШАБЛОН
TEMPLATE = r"""<!DOCTYPE html>
<html lang="kk" class="scroll-smooth">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ site.title }}</title>
<meta name="description" content="Әділет генерал-майоры Молдияр Молыбайұлы Оразалиевтің өмірі, қоғамдық ықпалы және тарихи мұрасы туралы цифрлық жоба.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Noto+Serif:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/aos@2.3.4/dist/aos.css">
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {
  darkMode: 'class',
  theme: { extend: {
    colors: { navy: { 950: '#0b1220', 900: '#0f172a', 800: '#1e293b', 700: '#334155' }, gold: { 400: '#fbbf24', 500: '#f59e0b', 600: '#d97706' } },
    fontFamily: { serif: ['"Noto Serif"', 'serif'], sans: ['Inter', 'system-ui', 'sans-serif'] }
  } }
}
</script>
<style>
  body { font-family: 'Inter', system-ui, sans-serif; }
  .font-serif { font-family: 'Noto Serif', serif; }
  .gold-text { background: linear-gradient(90deg,#f59e0b,#fbbf24,#d97706); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .pattern { background-image: radial-gradient(circle at 1px 1px, rgba(245,158,11,.12) 1px, transparent 0); background-size: 28px 28px; }
  .ornament { background-image: repeating-linear-gradient(45deg, rgba(245,158,11,.08) 0 2px, transparent 2px 14px); }
  .tl-line { background: linear-gradient(to bottom, transparent, #f59e0b 8%, #f59e0b 92%, transparent); }
  .card-lift { transition: transform .35s ease, box-shadow .35s ease, border-color .35s ease; }
  .card-lift:hover { transform: translateY(-6px); box-shadow: 0 20px 40px -15px rgba(217,119,6,.35); border-color: #f59e0b; }
  .nav-link { position: relative; }
  .nav-link::after { content:''; position:absolute; left:0; bottom:-4px; width:0; height:2px; background:#f59e0b; transition: width .3s; }
  .nav-link:hover::after { width:100%; }
  .modal-enter { animation: pop .3s ease; }
  @keyframes pop { from { opacity:0; transform: scale(.94) translateY(10px);} to { opacity:1; transform:none; } }
  .float { animation: float 6s ease-in-out infinite; }
  @keyframes float { 0%,100% { transform: translateY(0);} 50% { transform: translateY(-10px);} }
  .principle.active { background: linear-gradient(135deg,#d97706,#f59e0b); color:#0f172a; border-color:#f59e0b; transform: translateY(-4px); }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } html { scroll-behavior: auto; } }
</style>
</head>
<body class="bg-slate-50 text-slate-800 dark:bg-navy-950 dark:text-slate-200 transition-colors duration-300 antialiased">

<header id="top" class="fixed top-0 inset-x-0 z-50 backdrop-blur-md bg-white/80 dark:bg-navy-900/80 border-b border-slate-200 dark:border-navy-700">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
    <a href="#top" class="flex items-center gap-2 font-serif font-bold text-navy-900 dark:text-white">
      <span class="w-9 h-9 rounded-lg bg-navy-900 dark:bg-gold-500 flex items-center justify-center"><i data-lucide="scale" class="w-5 h-5 text-gold-400 dark:text-navy-900"></i></span>
      <span class="text-sm sm:text-base leading-tight">{{ site.brand }} <span class="text-gold-600">|</span> {{ site.short_name }}</span>
    </a>
    <nav class="hidden lg:flex items-center gap-7 text-sm font-medium">
      {% for id, label in nav %}<a class="nav-link hover:text-gold-600" href="#{{ id }}">{{ label }}</a>{% endfor %}
    </nav>
    <div class="flex items-center gap-2">
      <button id="themeToggle" aria-label="Тақырыпты ауыстыру" class="w-10 h-10 rounded-full border border-slate-300 dark:border-navy-700 flex items-center justify-center hover:bg-slate-100 dark:hover:bg-navy-800 transition">
        <i data-lucide="moon" class="w-5 h-5 dark:hidden"></i><i data-lucide="sun" class="w-5 h-5 hidden dark:block text-gold-400"></i>
      </button>
      <button id="menuBtn" aria-label="Мәзір" class="lg:hidden w-10 h-10 rounded-full border border-slate-300 dark:border-navy-700 flex items-center justify-center"><i data-lucide="menu" class="w-5 h-5"></i></button>
    </div>
  </div>
  <div id="mobileMenu" class="hidden lg:hidden border-t border-slate-200 dark:border-navy-700 bg-white dark:bg-navy-900 px-6 py-4 space-y-3 text-sm font-medium">
    {% for id, label in nav %}<a class="block hover:text-gold-600" href="#{{ id }}">{{ label }}</a>{% endfor %}
  </div>
</header>

<main>
<section class="relative overflow-hidden bg-navy-900 text-white pt-28 pb-20 pattern">
  <div class="absolute -top-24 -right-24 w-96 h-96 rounded-full bg-gold-500/10 blur-3xl"></div>
  <div class="absolute -bottom-32 -left-24 w-96 h-96 rounded-full bg-gold-600/10 blur-3xl"></div>
  <div class="relative max-w-7xl mx-auto px-4 sm:px-6 grid lg:grid-cols-5 gap-12 items-center">
    <div class="lg:col-span-3" data-aos="fade-up">
      <p class="inline-flex items-center gap-2 text-gold-400 text-xs sm:text-sm tracking-widest uppercase mb-5"><i data-lucide="landmark" class="w-4 h-4"></i> Тұлға және дәуір · цифрлық тарихи портрет</p>
      <h1 class="font-serif font-bold text-4xl sm:text-5xl lg:text-6xl leading-tight">Молдияр <span class="gold-text">Молыбайұлы</span> Оразалиев</h1>
      <p class="mt-6 text-lg sm:text-xl text-slate-300 max-w-2xl leading-relaxed">{{ site.subtitle }}</p>
      <div class="mt-8 flex flex-wrap gap-3">
        <a href="#biography" class="px-6 py-3 rounded-full bg-gold-500 text-navy-900 font-semibold hover:bg-gold-400 transition flex items-center gap-2">Портретті ашу <i data-lucide="arrow-down" class="w-4 h-4"></i></a>
        <a href="#quiz" class="px-6 py-3 rounded-full border border-gold-500/60 text-gold-400 font-semibold hover:bg-gold-500/10 transition">Білімді тексеру</a>
      </div>
    </div>
    <div class="lg:col-span-2" data-aos="zoom-in" data-aos-delay="150">
      <div class="float relative rounded-3xl p-1 bg-gradient-to-br from-gold-400 via-gold-600 to-gold-500 shadow-2xl shadow-gold-600/20">
        <div class="rounded-[1.4rem] bg-navy-800 p-7 ornament">
          <div class="w-28 h-28 mx-auto rounded-full bg-gradient-to-br from-gold-400 to-gold-600 flex items-center justify-center ring-4 ring-navy-900">
            <span class="font-serif text-4xl font-bold text-navy-900">МО</span>
          </div>
          <h3 class="mt-5 text-center font-serif text-xl font-semibold">Оразалиев Молдияр Молыбайұлы</h3>
          <p class="text-center text-slate-400 text-sm mt-1">Тарихи портрет · цифрлық жоба</p>
          <div class="mt-6 flex flex-wrap justify-center gap-2 text-xs sm:text-sm font-medium">
            {% for icon, label in badges %}
            <span class="px-3 py-1.5 rounded-full {{ 'bg-gold-500 text-navy-900' if loop.first else 'bg-navy-900 border border-gold-500/50 text-gold-400' }} flex items-center gap-1"><i data-lucide="{{ icon }}" class="w-3.5 h-3.5"></i>{{ label }}</span>
            {% endfor %}
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="relative max-w-7xl mx-auto px-4 sm:px-6 mt-16 grid sm:grid-cols-3 gap-4">
    {% for s in stats %}
    <div class="rounded-2xl bg-white/5 border border-white/10 p-6 text-center card-lift" data-aos="fade-up" data-aos-delay="{{ loop.index0 * 100 }}">
      {% if s.counter %}
      <div class="font-serif text-4xl font-bold gold-text"><span class="counter" data-target="{{ s.counter }}">0</span>{{ s.suffix }}</div>
      {% else %}
      <div class="font-serif text-xl sm:text-2xl font-bold gold-text leading-snug py-1.5">{{ s.text }}</div>
      {% endif %}
      <p class="mt-2 text-slate-300 text-sm">{{ s.label }}</p>
    </div>
    {% endfor %}
  </div>
</section>

<section id="biography" class="py-24 bg-slate-50 dark:bg-navy-950">
  <div class="max-w-5xl mx-auto px-4 sm:px-6">
    <div class="text-center mb-16" data-aos="fade-up">
      <p class="text-gold-600 font-semibold tracking-widest text-sm uppercase">Өмірбаяны</p>
      <h2 class="font-serif text-3xl sm:text-4xl font-bold mt-2 text-navy-900 dark:text-white">Дәуір шежіресі</h2>
      <p class="mt-4 text-slate-600 dark:text-slate-400 max-w-2xl mx-auto">Тұлғаның жолы — Тәуелсіз Қазақстанның қалыптасу тарихымен тығыз байланысты. Кезеңді басып, толығырақ оқыңыз.</p>
    </div>
    <div class="relative">
      <div class="tl-line absolute left-5 md:left-1/2 top-0 bottom-0 w-0.5 -translate-x-1/2"></div>
      <div id="timeline" class="space-y-12"></div>
    </div>
  </div>
</section>

<section id="impact" class="py-24 bg-white dark:bg-navy-900 border-y border-slate-200 dark:border-navy-800">
  <div class="max-w-7xl mx-auto px-4 sm:px-6">
    <div class="text-center mb-14" data-aos="fade-up">
      <p class="text-gold-600 font-semibold tracking-widest text-sm uppercase">Дәуір мен Ықпал</p>
      <h2 class="font-serif text-3xl sm:text-4xl font-bold mt-2 text-navy-900 dark:text-white">Қоғамға және Мемлекетке қосқан ықпалы</h2>
      <p class="mt-4 text-slate-600 dark:text-slate-400 max-w-2xl mx-auto">Лауазымдар тізімінен тыс — тұлғаның қоғамдық қауіпсіздікке, институционалдық реформаға және кадр тәрбиесіне әсері.</p>
    </div>
    <div id="reform" class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
      {% for c in impact %}
      <article class="card-lift rounded-2xl border border-slate-200 dark:border-navy-700 bg-slate-50 dark:bg-navy-800 p-7" data-aos="fade-up" data-aos-delay="{{ loop.index0 * 100 }}">
        <div class="w-12 h-12 rounded-xl bg-gold-500/15 text-gold-600 flex items-center justify-center mb-5"><i data-lucide="{{ c.icon }}" class="w-6 h-6"></i></div>
        <span class="text-gold-600 font-serif font-bold text-sm">{{ c.n }}</span>
        <h3 class="font-serif font-semibold text-lg mt-1 text-navy-900 dark:text-white">{{ c.title }}</h3>
        <p class="mt-3 text-sm text-slate-600 dark:text-slate-400 leading-relaxed">{{ c.text }}</p>
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section id="human" class="py-24 bg-slate-50 dark:bg-navy-950">
  <div class="max-w-6xl mx-auto px-4 sm:px-6">
    <div class="text-center mb-14" data-aos="fade-up">
      <p class="text-gold-600 font-semibold tracking-widest text-sm uppercase">Адами келбеті</p>
      <h2 class="font-serif text-3xl sm:text-4xl font-bold mt-2 text-navy-900 dark:text-white">Адами келбеті мен Өнер</h2>
      <p class="mt-4 text-slate-600 dark:text-slate-400 max-w-2xl mx-auto">Погондар мен лауазымның артындағы адам. Картаны басып, толығырақ қараңыз.</p>
    </div>
    <div class="grid md:grid-cols-2 gap-8">
      <button data-modal="music" class="card-lift text-left rounded-3xl p-8 bg-navy-900 text-white border border-navy-700 relative overflow-hidden group" data-aos="fade-right">
        <div class="absolute -right-6 -bottom-6 opacity-10 group-hover:opacity-20 transition"><i data-lucide="music" class="w-40 h-40 text-gold-400"></i></div>
        <div class="w-14 h-14 rounded-2xl bg-gold-500 text-navy-900 flex items-center justify-center mb-6"><i data-lucide="guitar" class="w-7 h-7"></i></div>
        <h3 class="font-serif text-2xl font-semibold">Музыкаға деген құштарлық</h3>
        <p class="mt-3 text-slate-300">Гитара мен барабанда ойнау, әуендер жазу.</p>
        <span class="mt-6 inline-flex items-center gap-2 text-gold-400 font-medium text-sm">Толығырақ <i data-lucide="arrow-right" class="w-4 h-4"></i></span>
      </button>
      <button data-modal="family" class="card-lift text-left rounded-3xl p-8 bg-white dark:bg-navy-800 border border-slate-200 dark:border-navy-700 relative overflow-hidden group" data-aos="fade-left">
        <div class="absolute -right-6 -bottom-6 opacity-10 group-hover:opacity-20 transition"><i data-lucide="home" class="w-40 h-40 text-gold-600"></i></div>
        <div class="w-14 h-14 rounded-2xl bg-navy-900 dark:bg-gold-500 text-gold-400 dark:text-navy-900 flex items-center justify-center mb-6"><i data-lucide="users-round" class="w-7 h-7"></i></div>
        <h3 class="font-serif text-2xl font-semibold text-navy-900 dark:text-white">Отбасылық мұра</h3>
        <p class="mt-3 text-slate-600 dark:text-slate-400">Педагогтар отбасынан шығып, офицерлік династия құруы.</p>
        <span class="mt-6 inline-flex items-center gap-2 text-gold-600 font-medium text-sm">Толығырақ <i data-lucide="arrow-right" class="w-4 h-4"></i></span>
      </button>
    </div>
  </div>
</section>

<section id="archive" class="py-24 bg-navy-900 text-white pattern">
  <div class="max-w-6xl mx-auto px-4 sm:px-6">
    <div class="text-center mb-12" data-aos="fade-up">
      <p class="text-gold-400 font-semibold tracking-widest text-sm uppercase">Цифрлық Архив · Оқушыларға арналған модуль</p>
      <h2 class="font-serif text-3xl sm:text-4xl font-bold mt-2">Офицерлік ар-намыс және Заң үстемдігі</h2>
      <p class="mt-4 text-slate-300 max-w-2xl mx-auto">Қағидатты таңдап, ойлануға арналған сұрақты оқыңыз. Содан кейін қысқа тесттен өтіңіз.</p>
    </div>
    <div class="grid lg:grid-cols-5 gap-6 items-start">
      <div id="principles" class="lg:col-span-2 grid grid-cols-2 gap-3"></div>
      <div class="lg:col-span-3 rounded-3xl bg-white/5 border border-white/10 p-8 min-h-[280px]" aria-live="polite">
        <i data-lucide="quote" class="w-10 h-10 text-gold-500"></i>
        <h3 id="pTitle" class="font-serif text-2xl font-semibold mt-3"></h3>
        <p id="pText" class="mt-3 text-slate-300 leading-relaxed"></p>
        <div class="mt-6 p-4 rounded-xl bg-navy-950/60 border-l-4 border-gold-500">
          <p class="text-xs uppercase tracking-widest text-gold-400 mb-1">Ойлан</p>
          <p id="pQ" class="text-slate-100"></p>
        </div>
        <textarea id="pNote" rows="3" placeholder="Өз ойыңызды осында жазыңыз (құрылғыда ғана қалады)…" class="mt-5 w-full rounded-xl bg-navy-950/60 border border-white/10 focus:border-gold-500 focus:outline-none p-3 text-sm text-white placeholder-slate-500"></textarea>
      </div>
    </div>
    <div id="quiz" class="mt-20 max-w-3xl mx-auto rounded-3xl bg-white dark:bg-navy-800 text-slate-800 dark:text-slate-100 p-8 shadow-2xl" data-aos="fade-up">
      <div class="flex items-center justify-between mb-6">
        <h3 class="font-serif text-2xl font-semibold text-navy-900 dark:text-white">Қысқа тест</h3>
        <span id="qCount" class="text-sm text-gold-600 font-semibold"></span>
      </div>
      <div id="quizBody"></div>
    </div>
  </div>
</section>
</main>

<footer class="bg-navy-950 text-slate-400 py-12 border-t border-navy-800">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 grid md:grid-cols-3 gap-8 text-sm">
    <div>
      <p class="font-serif text-white font-semibold text-lg">{{ site.brand }} <span class="text-gold-500">|</span> {{ site.short_name }}</p>
      <p class="mt-2">Тұлға және дәуір: цифрлық тарихи портрет.</p>
    </div>
    <div>
      <p class="text-white font-medium mb-2">Жоба туралы</p>
      <p>Мектептің қазақстан тарихы бойынша оқу жобасы. Материалдар білім беру мақсатында дайындалған.</p>
    </div>
    <div>
      <p class="text-white font-medium mb-2">Назар аударыңыз</p>
      <p>Жариялау алдында деректерді ресми дереккөздермен және отбасы архивімен салыстырып тексеру ұсынылады.</p>
    </div>
  </div>
  <p class="text-center text-xs mt-10 text-slate-500">© {{ year }} Мектеп тарих жобасы. Барлық құқықтар қорғалған.</p>
</footer>

<div id="modal" class="fixed inset-0 z-[60] hidden items-center justify-center p-4 bg-black/70 backdrop-blur-sm" role="dialog" aria-modal="true">
  <div class="modal-enter relative max-w-lg w-full rounded-3xl bg-white dark:bg-navy-800 p-8 shadow-2xl">
    <button id="modalClose" aria-label="Жабу" class="absolute top-4 right-4 w-9 h-9 rounded-full hover:bg-slate-100 dark:hover:bg-navy-700 flex items-center justify-center"><i data-lucide="x" class="w-5 h-5"></i></button>
    <div id="modalIcon" class="w-14 h-14 rounded-2xl bg-gold-500 text-navy-900 flex items-center justify-center mb-5"></div>
    <h3 id="modalTitle" class="font-serif text-2xl font-semibold text-navy-900 dark:text-white"></h3>
    <div id="modalBody" class="mt-4 text-slate-600 dark:text-slate-300 leading-relaxed space-y-3"></div>
  </div>
</div>

<button id="toTop" aria-label="Жоғарыға" class="fixed bottom-6 right-6 z-40 w-12 h-12 rounded-full bg-gold-500 text-navy-900 shadow-lg hidden items-center justify-center hover:bg-gold-400 transition"><i data-lucide="arrow-up" class="w-5 h-5"></i></button>

<script src="https://unpkg.com/lucide@latest"></script>
<script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
<script>
/* Деректер Python-нан келеді */
const timeline = {{ timeline | tojson }};
const principles = {{ principles | tojson }};
const quiz = {{ quiz | tojson }};
const modals = {{ modals | tojson }};
{% raw %}
const $ = s => document.querySelector(s);
lucide.createIcons();
AOS.init({ duration: 800, once: true, offset: 60 });

const root = document.documentElement;
try { if (localStorage.getItem('theme') === 'dark') root.classList.add('dark'); } catch(e){}
$('#themeToggle').addEventListener('click', () => {
  root.classList.toggle('dark');
  try { localStorage.setItem('theme', root.classList.contains('dark') ? 'dark' : 'light'); } catch(e){}
});
$('#menuBtn').addEventListener('click', () => $('#mobileMenu').classList.toggle('hidden'));
document.querySelectorAll('#mobileMenu a').forEach(a => a.addEventListener('click', () => $('#mobileMenu').classList.add('hidden')));

/* timeline */
const tl = $('#timeline');
timeline.forEach((e, i) => {
  const left = i % 2 === 0;
  const row = document.createElement('div');
  row.className = 'relative md:grid md:grid-cols-2 md:gap-14 pl-14 md:pl-0';
  row.setAttribute('data-aos', 'fade-up');
  row.innerHTML = `
    <span class="absolute left-5 md:left-1/2 top-6 -translate-x-1/2 w-11 h-11 rounded-full bg-navy-900 dark:bg-navy-800 border-2 border-gold-500 flex items-center justify-center z-10"><i data-lucide="${e.icon}" class="w-5 h-5 text-gold-500"></i></span>
    <div class="${left ? 'md:col-start-1 md:text-right' : 'md:col-start-2'}">
      <button class="tl-card card-lift w-full text-left ${left ? 'md:text-right' : ''} rounded-2xl p-6 bg-white dark:bg-navy-800 border border-slate-200 dark:border-navy-700" aria-expanded="false">
        <span class="font-serif text-3xl font-bold gold-text">${e.year}</span>
        <h3 class="mt-1 font-serif font-semibold text-navy-900 dark:text-white">${e.title}</h3>
        <div class="tl-more hidden mt-3 text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
          <p>${e.text}</p>
          <p class="mt-3 inline-block px-3 py-1 rounded-full bg-gold-500/15 text-gold-600 text-xs font-semibold">Тарихи контекст: ${e.context}</p>
        </div>
        <span class="mt-3 inline-flex items-center gap-1 text-xs text-gold-600 font-medium tl-hint">Толығырақ ↓</span>
      </button>
    </div>`;
  tl.appendChild(row);
});
lucide.createIcons();
document.querySelectorAll('.tl-card').forEach(c => c.addEventListener('click', () => {
  const more = c.querySelector('.tl-more');
  const open = more.classList.toggle('hidden') === false;
  c.setAttribute('aria-expanded', open);
  c.querySelector('.tl-hint').textContent = open ? 'Жасыру ↑' : 'Толығырақ ↓';
}));

/* counters */
const io = new IntersectionObserver(entries => entries.forEach(en => {
  if (!en.isIntersecting) return;
  const el = en.target, target = +el.dataset.target, dur = 1400, t0 = performance.now();
  const step = t => { const p = Math.min((t - t0) / dur, 1); el.textContent = Math.floor(target * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(step); };
  requestAnimationFrame(step); io.unobserve(el);
}), { threshold: .6 });
document.querySelectorAll('.counter').forEach(c => io.observe(c));

/* modals */
const modal = $('#modal');
function openModal(k) {
  const m = modals[k];
  $('#modalIcon').innerHTML = `<i data-lucide="${m.icon}" class="w-7 h-7"></i>`;
  $('#modalTitle').textContent = m.title;
  $('#modalBody').innerHTML = m.body.map(p => `<p>${p}</p>`).join('');
  lucide.createIcons();
  modal.classList.remove('hidden'); modal.classList.add('flex');
  document.body.style.overflow = 'hidden';
}
function closeModal() { modal.classList.add('hidden'); modal.classList.remove('flex'); document.body.style.overflow = ''; }
document.querySelectorAll('[data-modal]').forEach(b => b.addEventListener('click', () => openModal(b.dataset.modal)));
$('#modalClose').addEventListener('click', closeModal);
modal.addEventListener('click', e => { if (e.target === modal) closeModal(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });

/* principles */
const pWrap = $('#principles');
function selectP(i) {
  document.querySelectorAll('.principle').forEach((b, j) => b.classList.toggle('active', i === j));
  const p = principles[i];
  $('#pTitle').textContent = p.t; $('#pText').textContent = p.d; $('#pQ').textContent = p.q;
  $('#pNote').value = '';
}
principles.forEach((p, i) => {
  const b = document.createElement('button');
  b.className = 'principle card-lift rounded-2xl border border-white/15 bg-white/5 p-5 text-left transition';
  b.innerHTML = `<i data-lucide="${p.icon}" class="w-7 h-7 mb-3"></i><span class="font-serif font-semibold block leading-snug">${p.t}</span>`;
  b.addEventListener('click', () => selectP(i));
  pWrap.appendChild(b);
});
lucide.createIcons(); selectP(0);

/* quiz */
let qi = 0, score = 0;
function renderQuiz() {
  const body = $('#quizBody');
  if (qi >= quiz.length) {
    $('#qCount').textContent = '';
    const msg = score === quiz.length ? 'Тамаша! Тарихи портретті жақсы меңгердіңіз.' : score >= quiz.length / 2 ? 'Жақсы нәтиже! Шежірені қайта қарап шығуға болады.' : 'Тарихи шежіре бөліміне қайта оралып көріңіз.';
    body.innerHTML = `<div class="text-center py-6"><p class="font-serif text-5xl font-bold gold-text">${score} / ${quiz.length}</p><p class="mt-4">${msg}</p><button id="again" class="mt-6 px-6 py-3 rounded-full bg-gold-500 text-navy-900 font-semibold hover:bg-gold-400 transition">Қайта өту</button></div>`;
    $('#again').addEventListener('click', () => { qi = 0; score = 0; renderQuiz(); });
    return;
  }
  const q = quiz[qi];
  $('#qCount').textContent = `${qi + 1} / ${quiz.length}`;
  body.innerHTML = `<p class="font-medium text-lg">${q.q}</p><div class="mt-5 space-y-3">${q.o.map((o, i) => `<button data-i="${i}" class="opt w-full text-left px-5 py-3 rounded-xl border border-slate-300 dark:border-navy-700 hover:border-gold-500 hover:bg-gold-500/10 transition">${o}</button>`).join('')}</div><p id="fb" class="mt-4 text-sm min-h-[1.25rem]"></p>`;
  body.querySelectorAll('.opt').forEach(b => b.addEventListener('click', () => {
    const ok = +b.dataset.i === q.a; if (ok) score++;
    body.querySelectorAll('.opt').forEach(x => { x.disabled = true; x.classList.add('cursor-default'); if (+x.dataset.i === q.a) x.classList.add('bg-emerald-500/20', 'border-emerald-500'); });
    if (!ok) b.classList.add('bg-red-500/20', 'border-red-500');
    $('#fb').innerHTML = (ok ? '✅ Дұрыс!' : '❌ Қате. Дұрыс жауап: ' + q.o[q.a]) + ` <button id="next" class="ml-3 text-gold-600 font-semibold underline">${qi === quiz.length - 1 ? 'Нәтиже' : 'Келесі'} →</button>`;
    $('#next').addEventListener('click', () => { qi++; renderQuiz(); });
  }));
}
renderQuiz();

/* to top */
const toTop = $('#toTop');
window.addEventListener('scroll', () => { const s = window.scrollY > 600; toTop.classList.toggle('hidden', !s); toTop.classList.toggle('flex', s); });
toTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
{% endraw %}
</script>
</body>
</html>
"""


# ----------------------------------------------------------------- МАРШРУТТАР
@app.route("/")
def index():
    from datetime import date
    return render_template_string(
        TEMPLATE,
        site=SITE, nav=NAV, badges=BADGES, stats=STATS,
        timeline=TIMELINE, impact=IMPACT,
        principles=PRINCIPLES, quiz=QUIZ, modals=MODALS,
        year=date.today().year,
    )


@app.route("/api/timeline")
def api_timeline():
    """Шежіре деректері JSON ретінде (қосымша)."""
    return jsonify(TIMELINE)


if __name__ == "__main__":
    app.run(debug=True)