# Generates the static pages from shared partials: python3 build.py
from pathlib import Path

DIR = Path(__file__).parent
A = 'assets'
ARROW = '<svg width="18" height="14" viewBox="0 0 18 14" aria-hidden="true"><path d="M0 7h16M10 1l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2"/></svg>'
CHEV = '<svg width="12" height="8" viewBox="0 0 12 8" aria-hidden="true"><path d="M1 1l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2"/></svg>'

PRODUCTS = [
    dict(slug='notranja-oprema', title='Notranja stanovanjska oprema po naročilu', short='Notranja oprema',
         sub='Kuhinje, spalnice, kopalnice', img='gen/kuhinja.jpg',
         h1=['Notranja', 'oprema', 'po naročilu.'],
         intro=['Izdelava pohištva po meri je prava izbira, če želite dom opremiti skladno s svojimi željami in idejami. Zagotavljamo izdelavo celotne stanovanjske opreme, ki jo izdelamo po načrtih vašega arhitekta oziroma oblikovalca, ali pa vam pomagamo pri načrtovanju.',
                'Pri delu smo izredno prilagodljivi. S sodobno tehnologijo, bogatim znanjem, izkušnjami in najkvalitetnejšimi materiali uresničimo skoraj vse vaše želje.'],
         items_title='Opremimo celoten dom.',
         items=[('Kuhinje', 'gen/kuhinja.jpg'), ('Jedilnice', 'img/stanovanjska-oprema.jpg'), ('Spalnice', None), ('Otroške sobe', None), ('Kopalnice', 'gen/kerrock.jpg'), ('Predsobe', 'gen/montaza.jpg')],
         gallery=[('img/stanovanjska-oprema.jpg', 'w8'), ('gen/dleto.jpg', 'tall'), ('gen/svetovanje.jpg', 'w6'), ('gen/montaza.jpg', 'w6')]),
    dict(slug='stavbno-pohistvo', title='Stavbno pohištvo po naročilu', short='Stavbno pohištvo',
         sub='Okna, vrata, stopnice, ograje', img='gen/okno.jpg',
         h1=['Stavbno', 'pohištvo', 'po meri.'],
         intro=['Izdelujemo stavbno pohištvo po meri. Pri delu smo izredno prilagodljivi. S sodobno tehnologijo, bogatim znanjem, izkušnjami in najkvalitetnejšimi materiali uresničimo skoraj vse vaše želje.',
                'Za naša lesena okna je mogoče pridobiti subvencijo Eko sklada, pri čemer vam seveda pomagamo.'],
         items_title='Od okna do stopnišča.',
         items=[('Okna', 'gen/okno.jpg'), ('Vhodna vrata', None), ('Notranja vrata', 'gen/montaza.jpg'), ('Drsna vrata', None), ('Požarna vrata', None), ('Stopnice', 'gen/stopnice.jpg'), ('Stopniščne ograje', 'gen/stopnice.jpg'), ('Balkonske ograje', None)],
         gallery=[('img/fasada-okna.jpg', 'w8'), ('gen/stopnice.jpg', 'tall'), ('gen/montaza.jpg', 'w6'), ('gen/dleto.jpg', 'w6')],
         note=('Lesena okna s subvencijo Eko sklada.', 'Za naša lesena okna je mogoče pridobiti nepovratna sredstva Eko sklada. Pri pripravi vloge vam pomagamo.')),
    dict(slug='poslovni-prostori', title='Oprema poslovnih prostorov', short='Poslovni prostori',
         sub='Pisarne, gostinstvo, hoteli', img='img/poslovni-prostori.jpg',
         h1=['Oprema', 'poslovnih', 'prostorov.'],
         intro=['Opremljanje poslovnih prostorov je pomemben del naše dejavnosti. Pri izdelavi opreme upoštevamo standarde in izbiramo materiale z dolgo življenjsko dobo, da zadostimo potrebam in željam naročnika.',
                'Z opremljanjem različnih poslovnih prostorov imamo veliko izkušenj, zato vam lahko pomagamo pri načrtovanju in izvedbi celotnega projekta, od zasnove do montaže.'],
         items_title='Prostori, ki delajo.',
         items=[('Sprejemne in konferenčne sobe', 'img/poslovni-prostori.jpg'), ('Pisarniško pohištvo', 'gen/svetovanje.jpg'), ('Oprema gostinskih objektov', 'img/marina-bar.jpg'), ('Oprema hotelskih sob', None)],
         gallery=[('img/marina-bar.jpg', 'w8'), ('img/marina-zunaj.jpg', 'tall'), ('img/poslovni-prostori.jpg', 'w6'), ('gen/cnc.jpg', 'w6')]),
    dict(slug='max-compact', title='Izdelki iz Max Compact plošč', short='Max Compact',
         sub='Fasade, kabine, predelne stene', img='gen/compact.jpg',
         h1=['Max Compact.', 'Za prostore,', 'ki veliko zdržijo.'],
         intro=['Izdelki iz Max Compact plošč so pomemben del naše dejavnosti. Izdelujemo jih že vrsto let in imamo na tem področju ogromno znanja in izkušenj.',
                'Primerni so za objekte, kjer se dnevno izmenja veliko ljudi, in za prostore s povečano vlago. Compact plošče so vodoodporne in visoko odporne na površinske poškodbe.'],
         items_title='Kjer šteje odpornost.',
         items=[('Fasadne obloge', 'img/os-dobrna.jpg'), ('Balkonske ograje', 'img/bloki.jpg'), ('Sanitarne predelne stene', 'img/kabine-2.jpg'), ('Tuš kabine', 'img/kabine-1.jpg'), ('Garderobne kabine', 'img/kabine-3.jpg')],
         gallery=[('img/os-dobrna.jpg', 'w8'), ('img/kabine-4.jpg', 'tall'), ('img/fasada-compact.jpg', 'w6'), ('img/kabine-2.jpg', 'w6'), ('img/bloki.jpg', 'w6'), ('img/kabine-1.jpg', 'w6')]),
    dict(slug='kerrock', title='Izdelki iz Kerrocka', short='Kerrock',
         sub='Pulti in higienske površine', img='gen/kerrock.jpg',
         h1=['Kerrock.', 'Brez stikov,', 'brez kompromisov.'],
         intro=['Iz Kerrocka izdelujemo kuhinjske in kopalniške pulte ter higienske površine za zdravstvene domove, bolnišnice in vrtce.',
                'Izdelke iz Kerrocka smo med drugim vgradili v Splošni bolnici Celje in Zdravstvenem domu Celje.'],
         items_title='Gladko, higienično, trajno.',
         items=[('Kuhinjski pulti', 'gen/kuhinja.jpg'), ('Kopalniški pulti', 'gen/kerrock.jpg'), ('Higienske površine za zdravstvo in vrtce', 'img/kerrock-pult.jpg')],
         gallery=[('gen/kerrock.jpg', 'w8'), ('img/kerrock-pult.jpg', 'tall'), ('gen/kuhinja.jpg', 'w6'), ('gen/cnc.jpg', 'w6')]),
]

REFS = [
    ('Abanka d.d.', 'stavbno pohištvo in oprema'),
    ('Alpeks d.o.o.', 'stavbno pohištvo'),
    ('Arena Petrol Celje', 'stavbno pohištvo in Max Compact'),
    ('AVO Celje d.o.o., salon Toyota', 'stavbno pohištvo'),
    ('Banka Celje d.d.', 'stavbno pohištvo in oprema'),
    ('Cinkarna Celje d.d.', 'stavbno pohištvo in oprema pisarn v upravni stavbi'),
    ('Dinos d.d.', 'stavbno pohištvo in oprema'),
    ('Gropik d.o.o.', 'stavbno pohištvo in oprema'),
    ('Istrabenz plini d.o.o.', 'pohištvena oprema'),
    ('Juteks d.o.o.', 'stavbno pohištvo upravne stavbe v Žalcu'),
    ('Kana d.o.o.', 'stavbno pohištvo in notranja oprema'),
    ('Klinika Zdrav splet d.o.o.', 'Max Compact fasada, stavbno pohištvo, pohištvena oprema'),
    ('Merkscha d.o.o.', 'stavbno pohištvo in oprema'),
    ('Oplast d.o.o.', 'pohištvo'),
    ('Marina Sutomiščica', 'notranja oprema, zunanja oprema, Max Compact izdelki'),
    ('Bloki Latkova vas', 'Max Compact fasada'),
    ('Bloki Lava', 'stavbno pohištvo'),
    ('Bloki Štore', 'Max Compact fasada, stavbno pohištvo'),
    ('Bloki Velenje', 'Max Compact fasada'),
    ('Bolnica Jesenice', 'stavbno pohištvo in oprema'),
    ('Cerkev Galicija', 'stavbno pohištvo'),
    ('Cerkev Tepanje', 'stavbno pohištvo'),
    ('Dijaški dom Celje', 'pohištvena oprema sob'),
    ('Dom upokojencev Vojnik', 'stavbno pohištvo'),
    ('I. gimnazija v Celju', 'stavbno pohištvo, pohištvena oprema, fasada nove telovadnice'),
    ('Knjižnici Luče in Ljubno', 'pohištvena oprema'),
    ('Mestna občina Celje', 'stavbno pohištvo in oprema'),
    ('OŠ Dobrna', 'Max Compact fasada, stavbno pohištvo'),
    ('OŠ Vojnik', 'stavbno pohištvo'),
    ('Pošta Slovenije d.o.o.', 'stavbno pohištvo in oprema več pošt po Sloveniji'),
    ('Splošna bolnišnica Celje', 'urgentni center, diabetični, pljučni in ortopedski oddelek: stavbno pohištvo, oprema, Max Compact sanitarije, Kerrock'),
    ('Vrtci Občine Celje', 'stavbno pohištvo, pohištvena oprema, Max Compact sanitarije'),
    ('ZD Celje', 'stavbno pohištvo, oprema splošnih, ortodontskih in zobnih ambulant, Kerrock'),
    ('ZZZS Celje', 'pohištvena oprema'),
]
HOME_REFS = ['Splošna bolnišnica Celje', 'Cinkarna Celje d.d.', 'Pošta Slovenije d.o.o.', 'Mestna občina Celje', 'Marina Sutomiščica',
             'ZD Celje', 'I. gimnazija v Celju', 'Abanka d.d.', 'Klinika Zdrav splet d.o.o.', 'OŠ Dobrna']
REF_PHOTOS = ['img/os-dobrna.jpg', 'img/marina-bar.jpg', 'img/fasada-compact.jpg', 'img/fasada-okna.jpg', 'img/kabine-2.jpg', 'img/bloki.jpg', 'img/poslovni-prostori.jpg']

NAV = [('o-podjetju.html', 'O podjetju'), ('reference.html', 'Reference'), ('kontakt.html', 'Kontakt')]


def head(title, desc):
    return f'''<!doctype html>
<html lang="sl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{A}/gen/hero.jpg">
<link rel="icon" href="{A}/img/logo_mizar.jpg">
<link rel="preload" href="{A}/fonts/Switzer-Variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{A}/css/site.css">
<script>
(function () {{
  if (!/[?&]r=/.test(location.search)) return;
  var s = document.createElement('script');
  s.async = true;
  s.referrerPolicy = 'no-referrer';
  s.setAttribute('data-landing', location.href);
  s.src = 'https://phplaravel-758037-6569212.cloudwaysapps.com/v/script.js';
  document.head.appendChild(s);
}})();
</script>
</head>
<body>'''


def header(cur):
    mega = ''.join(f'''<a class="mega__card" href="{p['slug']}.html"><div class="mega__img"><img src="{A}/{p['img']}" alt="" loading="lazy"></div><strong>{p['short']}</strong><span>{p['sub']}</span></a>''' for p in PRODUCTS)
    links = ''.join(f'<a href="{h}"{" class=is-cur" if h == cur else ""}>{l}</a>' for h, l in NAV[1:])
    msub = ''.join(f'<a class="sub" href="{p["slug"]}.html">{p["short"]}</a>' for p in PRODUCTS)
    izd_cur = ' is-cur' if cur in [p['slug'] + '.html' for p in PRODUCTS] else ''
    return f'''
<div class="loader" aria-hidden="true"><div class="loader__in"><img src="{A}/img/logo_mizar.jpg" alt=""><div class="loader__num">0</div></div></div>
<header class="hdr">
  <a class="hdr__logo" href="index.html" aria-label="Mizar d.o.o., domov"><img src="{A}/img/logo_mizar.jpg" alt="Mizar, z vami že od leta 1990" width="236" height="85"></a>
  <nav class="hdr__nav" aria-label="Glavna navigacija">
    <a href="o-podjetju.html"{" class=is-cur" if cur == "o-podjetju.html" else ""}>O podjetju</a>
    <button type="button" data-mega aria-expanded="false" class="{izd_cur.strip()}">Izdelki {CHEV}</button>
    {links}
  </nav>
  <a class="hdr__tel" href="tel:+38634253950">03 425 39 50</a>
  <a class="btn hdr__cta" href="kontakt.html#povprasevanje">Povpraševanje {ARROW}</a>
  <button class="hdr__burger" type="button" aria-label="Meni" aria-expanded="false"><i></i></button>
</header>
<div class="mega" aria-label="Izdelki"><div class="mega__grid">{mega}</div></div>
<div class="mega-scrim"></div>
<nav class="mnav" aria-label="Mobilna navigacija">
  <a href="index.html">Domov</a>
  <a href="o-podjetju.html">O podjetju</a>
  {msub}
  <a href="reference.html">Reference</a>
  <a href="kontakt.html">Kontakt</a>
  <div class="mnav__foot"><a href="tel:+38634253950">03 425 39 50</a><a href="mailto:mizarce@siol.net">mizarce@siol.net</a><span class="mute">Medlog 7e, 3000 Celje</span></div>
</nav>
<main>'''


def contact(light=False, title='Imate idejo? Pogovorimo se.'):
    opts = ''.join(f'<option>{p["short"]}</option>' for p in PRODUCTS)
    return f'''
<section class="cta{' cta--light' if light else ''} sec" id="povprasevanje">
  <div class="wrap grid">
    <h2 class="d2 cta__head" data-reveal>{title}</h2>
    <dl class="cta__info" data-reveal>
      <div><dt>Telefon</dt><dd><a href="tel:+38634253950">03 425 39 50</a><br><a href="tel:+38634910291">03 491 02 91</a></dd></div>
      <div><dt>Mobilni</dt><dd><a href="tel:+38641614041">041 614 041</a><br><a href="tel:+38641372660">041 372 660</a><br><a href="tel:+38631310994">031 310 994</a></dd></div>
      <div><dt>E-pošta</dt><dd><a href="mailto:mizarce@siol.net">mizarce@siol.net</a></dd></div>
      <div><dt>Naslov</dt><dd>Mizar, d.o.o. Celje<br>Medlog 7e, 3000 Celje</dd></div>
    </dl>
    <form class="form" data-reveal="1" novalidate>
      <label>Ime in priimek<input name="ime" required autocomplete="name"></label>
      <label>Telefon<input name="tel" type="tel" autocomplete="tel"></label>
      <label class="full">E-pošta<input name="email" type="email" required autocomplete="email"></label>
      <label class="full">Kaj načrtujete<select name="podrocje"><option>Izberite področje</option>{opts}<option>Drugo</option></select></label>
      <label class="full">Sporočilo<textarea name="sporocilo" rows="4" required></textarea></label>
      <div class="form__foot"><small>Odgovorimo v najkrajšem možnem času. Podatke uporabimo samo za odgovor na vaše povpraševanje.</small><button class="btn{' btn--light' if not light else ''}" type="submit">Pošljite {ARROW}</button></div>
      <p class="form__ok">Hvala, sporočilo smo prejeli. Oglasimo se kmalu.</p>
    </form>
  </div>
</section>'''


def footer():
    prods = ''.join(f'<a href="{p["slug"]}.html">{p["short"]}</a>' for p in PRODUCTS)
    return f'''
</main>
<footer class="ftr">
  <div class="wrap grid ftr__top">
    <div class="ftr__logo"><img src="{A}/img/logo_mizar.jpg" alt="Mizar" width="236" height="85"><p>Mizarski izdelki po naročilu za zasebne in poslovne prostore.</p></div>
    <div class="ftr__col"><h4>Izdelki</h4>{prods}</div>
    <div class="ftr__col"><h4>Podjetje</h4><a href="o-podjetju.html">O podjetju</a><a href="reference.html">Reference</a><a href="kontakt.html">Kontakt</a></div>
    <div class="ftr__col"><h4>Kontakt</h4><a href="tel:+38634253950">03 425 39 50</a><a href="mailto:mizarce@siol.net">mizarce@siol.net</a><span>Medlog 7e<br>3000 Celje</span></div>
    <div class="ftr__badges">
      <img src="{A}/img/eu.png" alt="Evropska unija, Evropski sklad za regionalni razvoj">
      <p>Naziv operacije: Polokrogla in okrogla okna z dodatnimi profili, za stara mestna jedra. Naložba v vašo prihodnost.</p>
      <img class="sq" src="{A}/img/sq.png" alt="Slovenska kakovost">
    </div>
    <div class="ftr__bottom"><span>© 2026 Mizar, d.o.o. Celje. Vse pravice pridržane.</span><a href="#">Politika piškotkov</a></div>
  </div>
  <div class="wrap ftr__word" aria-hidden="true"><span style="display:inline-block">mizar 1990</span></div>
</footer>
<script src="{A}/js/gsap.min.js"></script>
<script src="{A}/js/ScrollTrigger.min.js"></script>
<script src="{A}/js/lenis.min.js"></script>
<script src="{A}/js/site.js"></script>
</body>
</html>'''


def lines(parts, cls='d1', red_last=False):
    out = []
    for i, p in enumerate(parts):
        c = ' class="red"' if red_last and i == len(parts) - 1 else ''
        out.append(f'<span class="ln"><span{c}>{p}</span></span>')
    return ''.join(out)


def home():
    tiles = []
    for i, p in enumerate(PRODUCTS):
        cls = 'tile tile--a' if i == 0 else 'tile tile--b' if i == 1 else 'tile'
        items = ', '.join(x[0] for x in p['items'])
        tiles.append(f'''<a class="{cls}" href="{p['slug']}.html" data-reveal="{i % 3}">
      <div class="frame"><img src="{A}/{p['img']}" alt="{p['short']}" loading="lazy" data-parallax></div>
      <div class="tile__meta"><h3>{p['short']}</h3>{ARROW}</div>
      <p>{items}</p>
    </a>''')
    refs = ''.join(f'<li><b>{n}</b><span>{w}</span></li>' for n, w in REFS if n in HOME_REFS)
    photos = ''.join(f'<img src="{A}/{s}" alt=""{" class=on" if i == 0 else ""} loading="lazy">' for i, s in enumerate(REF_PHOTOS))
    return head('Mizar d.o.o. Celje, mizarski izdelki po naročilu', 'Mizarski izdelki po naročilu za zasebne in poslovne prostore. Svetujemo, izdelujemo in montiramo, od leta 1990.') + header('index.html') + f'''
<section class="hero">
  <div class="wrap grid hero__top">
    <h1 class="d1 hero__title">{lines(['Svetujemo.', 'Izdelujemo.', 'Montiramo.'], red_last=True)}</h1>
    <div class="hero__aside">
      <p class="lead">Z osebnim pristopom vam pomagamo uresničiti vaše ideje. Mizarski izdelki po naročilu za domove in poslovne prostore, od leta 1990.</p>
      <a class="btn" href="#izdelki">Poglejte, kaj izdelujemo {ARROW}</a>
    </div>
  </div>
  <div class="hero__media"><div class="frame hero__frame" data-expand><img src="{A}/gen/hero.jpg" alt="Mizarska delavnica" data-parallax fetchpriority="high"></div></div>
</section>

<section class="sec">
  <div class="wrap grid">
    <p class="d3 intro__text" data-fill>Mizar je zasebno podjetje, ustanovljeno leta 1990. Izdelujemo mizarske izdelke po naročilu za zasebne in poslovne prostore. Z znanjem dolgoletnih izkušenj, sodobno tehnologijo in najkvalitetnejšimi materiali nastajajo izdelki za najzahtevnejše naročnike.</p>
    <div class="frame intro__img" data-reveal><img src="{A}/gen/dleto.jpg" alt="Dleto v hrastovem lesu" loading="lazy" data-parallax></div>
    <div class="stats">
      <div class="stat" data-reveal><b data-count="1990">1990</b><span>leto ustanovitve podjetja v Celju</span></div>
      <div class="stat" data-reveal="1"><b data-count="5">5</b><span>področij, od notranje opreme do Kerrocka</span></div>
      <div class="stat" data-reveal="2"><b data-count="34">34</b><span>referenčnih naročnikov, od bolnišnic do bank</span></div>
    </div>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="wrap grid">
    <div class="proc__head"><h2 class="d2" data-reveal>Od ideje do montaže.</h2><p class="lead mute" data-reveal="1">En partner za celoten projekt. Na podlagi strokovne usposobljenosti in dolgoletnih izkušenj vas vodimo od prve skice do zadnjega vijaka.</p></div>
    <article class="proc__item" data-reveal><div class="frame"><img src="{A}/gen/svetovanje.jpg" alt="Načrtovanje pohištva" loading="lazy" data-parallax></div><h3 class="d4">Svetujemo</h3><p>Izdelamo po načrtih vašega arhitekta ali oblikovalca, ali pa načrt pripravimo skupaj z vami.</p></article>
    <article class="proc__item" data-reveal="1"><div class="frame"><img src="{A}/gen/cnc.jpg" alt="CNC obdelava v delavnici" loading="lazy" data-parallax></div><h3 class="d4">Izdelujemo</h3><p>S pomočjo najnovejše tehnologije in najkvalitetnejših materialov izdelamo vsak kos v naši delavnici.</p></article>
    <article class="proc__item" data-reveal="2"><div class="frame"><img src="{A}/gen/montaza.jpg" alt="Montaža notranjih vrat" loading="lazy" data-parallax></div><h3 class="d4">Montiramo</h3><p>Želeni mizarski izdelek natančno zmontiramo na objektu, od posameznih vrat do celotnih projektov.</p></article>
  </div>
</section>

<section class="sec" id="izdelki" style="padding-top:0">
  <div class="wrap">
    <div class="grid"><div class="prod__head"><h2 class="d2" data-reveal>Kaj izdelujemo.</h2><a class="link" href="kontakt.html#povprasevanje" data-reveal="1">Pošljite povpraševanje {ARROW}</a></div></div>
    <div class="bento">{''.join(tiles)}</div>
  </div>
</section>

<section class="state sec">
  <div class="wrap grid">
    <p class="d2 state__q" data-fill>Merilo naše uspešnosti so zadovoljne stranke, ki se vračajo k nam.</p>
    <div class="state__by"><span>Zavezujemo se h kakovosti izdelkov in estetski prefinjenosti.</span><span>Mizar, d.o.o. Celje</span></div>
  </div>
</section>

<section class="sec">
  <div class="wrap grid eko">
    <div class="frame" data-reveal><img src="{A}/img/fasada-okna.jpg" alt="Lesena okna v starem mestnem jedru" loading="lazy" data-parallax></div>
    <div class="eko__txt">
      <h2 class="d3" data-reveal>Lesena okna s subvencijo Eko sklada.</h2>
      <p class="lead mute" data-reveal="1">Za naša lesena okna je mogoče pridobiti subvencijo Eko sklada. Pri vlogi vam pomagamo. Z dodatnimi profili izdelamo tudi polkrožna in okrogla okna za stara mestna jedra.</p>
      <a class="link" href="stavbno-pohistvo.html" data-reveal="2">Stavbno pohištvo {ARROW}</a>
    </div>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="wrap grid">
    <div class="refs__side">
      <h2 class="d2" data-reveal>Zaupali so nam.</h2>
      <p class="lead mute" data-reveal="1">Bolnišnice, šole, banke, občine in domovi. Merilo naše uspešnosti so stranke, ki se vračajo.</p>
      <div class="refs__photos" data-reveal="2">{photos}</div>
    </div>
    <div class="refs__list-wrap" style="grid-column:7/13">
      <ul class="refs__list" style="grid-column:auto">{refs}</ul>
      <a class="link refs__more" href="reference.html">Vseh 34 referenc {ARROW}</a>
    </div>
  </div>
</section>
''' + contact() + footer()


def product(p):
    items = ''.join(f'<li><span>{n}</span>{f"<img src={chr(34)}{A}/{img}{chr(34)} alt={chr(34)}{chr(34)} loading=lazy>" if img else ""}</li>' for n, img in p['items'])
    gal = ''.join(f'<div class="frame {c}" data-reveal="{i % 2}"><img src="{A}/{s}" alt="" loading="lazy" data-parallax></div>' for i, (s, c) in enumerate(p['gallery']))
    note = ''
    if p.get('note'):
        note = f'''<section class="sec--tight"><div class="wrap grid"><div class="note" data-reveal><h3 class="d3">{p['note'][0]}</h3><div><p class="lead mute">{p['note'][1]}</p><a class="btn" href="kontakt.html#povprasevanje">Vprašajte nas {ARROW}</a></div></div></div></section>'''
    others = [o for o in PRODUCTS if o is not p][:3]
    more = ''.join(f'''<a class="tile" href="{o['slug']}.html" data-reveal="{i}"><div class="frame"><img src="{A}/{o['img']}" alt="{o['short']}" loading="lazy" data-parallax></div><div class="tile__meta"><h3>{o['short']}</h3>{ARROW}</div><p>{o['sub']}</p></a>''' for i, o in enumerate(others))
    intro = ''.join(f'<p class="lead{" mute" if i else ""}">{t}</p>' for i, t in enumerate(p['intro']))
    return head(f"{p['title']} | Mizar d.o.o.", p['intro'][0][:155]) + header(p['slug'] + '.html') + f'''
<section class="phero">
  <div class="wrap grid">
    <div class="phero__crumb"><a href="index.html">Domov</a><span>/</span><span>Izdelki</span></div>
    <h1 class="d1 phero__title">{lines(p['h1'], red_last=True)}</h1>
    <div class="phero__intro">{intro}</div>
  </div>
  <div class="phero__media"><div class="frame hero__frame" data-expand><img src="{A}/{p['img']}" alt="{p['short']}" data-parallax fetchpriority="high"></div></div>
</section>
<section class="sec">
  <div class="wrap grid">
    <div class="sub2"><h2 class="d2" data-reveal>{p['items_title']}</h2><a class="link" href="kontakt.html#povprasevanje" data-reveal="1">Pošljite povpraševanje {ARROW}</a></div>
    <ul class="items" data-reveal>{items}</ul>
  </div>
</section>
{note}
<section class="sec" style="padding-top:0"><div class="wrap gal">{gal}</div></section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="grid"><div class="prod__head"><h2 class="d3" data-reveal>Še več po meri.</h2></div></div>
    <div class="bento">{more}</div>
  </div>
</section>
''' + contact(light=True) + footer()


def about():
    return head('O podjetju | Mizar d.o.o.', 'Mizar d.o.o. je zasebno podjetje, ustanovljeno leta 1990, ki izdeluje mizarske izdelke po naročilu.') + header('o-podjetju.html') + f'''
<section class="phero">
  <div class="wrap grid">
    <div class="phero__crumb"><a href="index.html">Domov</a><span>/</span><span>O podjetju</span></div>
    <h1 class="d1 phero__title">{lines(['Z vami že', 'od leta 1990.'], red_last=True)}</h1>
    <div class="phero__intro">
      <p class="lead">Mizar d.o.o. je zasebno podjetje, ustanovljeno leta 1990. Ukvarjamo se z izdelavo mizarskih izdelkov po naročilu za zasebne in poslovne prostore.</p>
      <p class="lead mute">Z znanjem, pridobljenim z dolgoletnimi izkušnjami, s kombinacijo najsodobnejših tehnoloških postopkov in najkvalitetnejših materialov izdelujemo visoko kakovostne izdelke za najzahtevnejše naročnike.</p>
    </div>
  </div>
  <div class="phero__media"><div class="frame hero__frame" data-expand><img src="{A}/gen/hero.jpg" alt="Mizarska delavnica" data-parallax fetchpriority="high"></div></div>
</section>
<section class="sec">
  <div class="wrap grid">
    <p class="d3 intro__text" data-fill style="grid-column:1/-1;max-width:24ch">Naša referenčna lista obsega veliko zadovoljnih naročnikov. Merilo naše uspešnosti so zadovoljne stranke, ki se vračajo k nam.</p>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap grid">
    <div class="vm" data-reveal><h3 class="d3">Vizija</h3><p class="lead mute">Želimo ohraniti stabilno podjetje in stremimo k vsakoletni trajnostni rasti. Sledimo cilju dobrega razmerja med kakovostjo izdelkov in ceno.</p></div>
    <div class="vm" data-reveal="1"><h3 class="d3">Poslanstvo</h3><p class="lead mute">Zavezujemo se h kakovosti izdelkov in estetski prefinjenosti. Z osebnim pristopom strankam ponujamo edinstvene izdelke in storitve.</p></div>
  </div>
</section>
<section class="sec" style="padding-top:0"><div class="wrap gal">
  <div class="frame w8" data-reveal style="aspect-ratio:16/10"><img src="{A}/gen/cnc.jpg" alt="" loading="lazy" data-parallax></div>
  <div class="frame tall" data-reveal="1"><img src="{A}/gen/dleto.jpg" alt="" loading="lazy" data-parallax></div>
</div></section>
<section class="sec" style="padding-top:0">
  <div class="wrap card">
    <h2 class="d3" data-reveal style="grid-column:1/5">Vizitka</h2>
    <dl data-reveal="1">
      <dt>Podjetje</dt><dd>Mizar, d.o.o. Celje</dd>
      <dt>Naslov</dt><dd>Medlog 7e, 3000 Celje</dd>
      <dt>Davčna številka</dt><dd>SI60420740 (davčni zavezanec)</dd>
      <dt>Matična številka</dt><dd>5356750000</dd>
      <dt>IBAN</dt><dd>SI56 0510 0801 5150 034 (Abanka d.d.)</dd>
      <dt>Sodni register</dt><dd>Vpis 1. 5. 1990 pod št. 10160900 pri Okrožnem sodišču Celje</dd>
    </dl>
    <p class="legal">Spoštujemo veljavno zakonodajo o varstvu potrošnikov. Pogoje poslovanja sklepamo individualno. Po svojih najboljših močeh si prizadevamo, da se morebitni spori rešijo sporazumno. Če spora ni mogoče rešiti sporazumno, je zanj pristojno Okrožno sodišče v Celju, saj ne priznavamo nobenega izvajalca izvensodnega reševanja potrošniških sporov kot pristojnega za reševanje potrošniškega spora, ki bi ga potrošnik lahko sprožil v skladu z Zakonom o izvensodnem reševanju potrošniških sporov.</p>
  </div>
</section>
''' + contact(light=True) + footer()


def references():
    refs = ''.join(f'<li><b>{n}</b><span>{w}</span></li>' for n, w in REFS)
    gal = [('img/os-dobrna.jpg', 'w8'), ('img/marina-zunaj.jpg', 'tall'), ('img/fasada-compact.jpg', 'w6'), ('img/marina-bar.jpg', 'w6'),
           ('img/bloki.jpg', ''), ('img/kabine-1.jpg', ''), ('img/fasada-compact-2.jpg', ''), ('img/fasada-okna.jpg', 'w6'), ('img/kabine-2.jpg', 'w6')]
    g = ''.join(f'<div class="frame {c}" data-reveal="{i % 3}"><img src="{A}/{s}" alt="" loading="lazy" data-parallax></div>' for i, (s, c) in enumerate(gal))
    return head('Reference | Mizar d.o.o.', 'Naročniki, ki so nam v zadnjih letih zaupali stavbno pohištvo, opremo, Max Compact in Kerrock izdelke.') + header('reference.html') + f'''
<section class="phero">
  <div class="wrap grid">
    <div class="phero__crumb"><a href="index.html">Domov</a><span>/</span><span>Reference</span></div>
    <h1 class="d1 phero__title">{lines(['Zaupali', 'so nam.'], red_last=True)}</h1>
    <div class="phero__intro"><p class="lead">V zadnjih letih so nam zaupali bolnišnice, šole, vrtci, banke, občine, podjetja in cerkve. Tu je izbor naročnikov in del, ki smo jih zanje izdelali.</p></div>
  </div>
</section>
<section class="sec">
  <div class="wrap grid">
    <div class="refs__side">
      <p class="d1" style="margin:0"><b data-count="34" style="font-weight:520">34</b></p>
      <p class="lead mute">referenčnih naročnikov iz javnega in zasebnega sektorja.</p>
    </div>
    <ul class="refs__list" data-reveal>{refs}</ul>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap grid"><div class="sub2"><h2 class="d2" data-reveal>Izvedeni projekti.</h2></div></div>
  <div class="wrap gal">{g}</div>
</section>
''' + contact(light=True, title='Naslednji projekt je lahko vaš.') + footer()


def kontakt():
    return head('Kontakt | Mizar d.o.o.', 'Mizar, d.o.o. Celje, Medlog 7e, 3000 Celje. Telefon 03 425 39 50, mizarce@siol.net.') + header('kontakt.html') + f'''
<section class="phero">
  <div class="wrap grid">
    <div class="phero__crumb"><a href="index.html">Domov</a><span>/</span><span>Kontakt</span></div>
    <h1 class="d1 phero__title">{lines(['Pišite nam', 'ali pokličite.'], red_last=True)}</h1>
    <div class="phero__intro"><p class="lead">Povejte nam, kaj načrtujete. Pripravimo predlog, svetujemo pri materialih in izdelamo ponudbo.</p></div>
  </div>
</section>
''' + contact(light=True, title='Povpraševanje.') + f'''
<section class="sec--tight" style="padding-top:0;background:var(--paper)">
  <div class="wrap grid"><div class="map" style="margin-top:0"><iframe title="Zemljevid, Medlog 7e, Celje" loading="lazy" src="https://www.google.com/maps?q=Medlog+7e,+3000+Celje&amp;output=embed"></iframe></div></div>
</section>
''' + footer()


pages = {'index.html': home(), 'o-podjetju.html': about(), 'reference.html': references(), 'kontakt.html': kontakt()}
for p in PRODUCTS:
    pages[p['slug'] + '.html'] = product(p)
for name, html in pages.items():
    (DIR / name).write_text(html, encoding='utf-8')
print('built', len(pages), 'pages')
