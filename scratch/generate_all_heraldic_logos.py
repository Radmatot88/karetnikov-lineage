import os
import math

SVG_DIR = r"c:\Karetnikov_Lineage\public\images\heraldry\logos_svg"
os.makedirs(SVG_DIR, exist_ok=True)

PBR_DEFS = """
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF5B8" />
      <stop offset="25%" stop-color="#E5C158" />
      <stop offset="60%" stop-color="#B8860B" />
      <stop offset="100%" stop-color="#6B4E03" />
    </linearGradient>
    <linearGradient id="madderRed" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D93838" />
      <stop offset="40%" stop-color="#8B1E1E" />
      <stop offset="85%" stop-color="#4A0E0E" />
      <stop offset="100%" stop-color="#240404" />
    </linearGradient>
    <linearGradient id="azureGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#5B86E5" />
      <stop offset="45%" stop-color="#1E3A8A" />
      <stop offset="100%" stop-color="#0B193D" />
    </linearGradient>
    <linearGradient id="emeraldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34D399" />
      <stop offset="50%" stop-color="#065F46" />
      <stop offset="100%" stop-color="#022C22" />
    </linearGradient>
    <linearGradient id="steelGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="35%" stop-color="#E2E8F0" />
      <stop offset="70%" stop-color="#94A3B8" />
      <stop offset="100%" stop-color="#334155" />
    </linearGradient>
    <linearGradient id="darkSlate" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" />
      <stop offset="50%" stop-color="#0F172A" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <filter id="pbrEmboss" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="2.5" result="blur" />
      <feSpecularLighting in="blur" surfaceScale="3" specularConstant="1.2" specularExponent="22" lighting-color="#FFF9DB" result="specOut">
        <fePointLight x="-80" y="-120" z="220" />
      </feSpecularLighting>
      <feComposite in="specOut" in2="SourceAlpha" operator="in" result="specular" />
      <feComposite in="SourceGraphic" in2="specular" operator="arithmetic" k1="0" k2="1" k3="1" k4="0" />
    </filter>
    <filter id="dropShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="6" stdDeviation="5" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>
"""

def base_svg(filename, title, subtitle, content, bg="url(#darkSlate)"):
    code = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="500" height="500">
{PBR_DEFS}
  <rect width="500" height="500" rx="28" fill="{bg}" />
  <rect x="16" y="16" width="468" height="468" rx="22" fill="none" stroke="url(#goldGrad)" stroke-width="2.5" stroke-dasharray="10, 5" opacity="0.85" />
  <rect x="26" y="26" width="448" height="448" rx="16" fill="none" stroke="url(#goldGrad)" stroke-width="1.5" />
  <text x="250" y="65" text-anchor="middle" font-family="'Times New Roman', Georgia, serif" font-size="18" font-weight="bold" fill="url(#goldGrad)" letter-spacing="2.5">{title.upper()}</text>
  <line x1="110" y1="78" x2="390" y2="78" stroke="url(#goldGrad)" stroke-width="1.5" />
  <g transform="translate(0, 10)" filter="url(#pbrEmboss)">
    {content}
  </g>
  <line x1="130" y1="432" x2="370" y2="432" stroke="url(#goldGrad)" stroke-width="1.5" />
  <text x="250" y="456" text-anchor="middle" font-family="'Times New Roman', Georgia, serif" font-size="13" fill="#E2E8F0" letter-spacing="1.5">{subtitle}</text>
</svg>"""
    p = os.path.join(SVG_DIR, filename)
    with open(p, "w", encoding="utf-8") as f:
        f.write(code)
    return p

def wheel(cx, cy, r, spokes=8, col="url(#goldGrad)", stroke_w=5):
    lines = []
    for i in range(spokes):
        a = (2 * math.pi / spokes) * i
        lines.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + r*math.cos(a):.1f}" y2="{cy + r*math.sin(a):.1f}" stroke="{col}" stroke-width="{stroke_w}"/>')
    return f"""<g filter="url(#dropShadow)">
      <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{stroke_w*1.4}"/>
      <circle cx="{cx}" cy="{cy}" r="{r*0.86:.1f}" fill="none" stroke="{col}" stroke-width="{stroke_w*0.6}"/>
      {"".join(lines)}
      <circle cx="{cx}" cy="{cy}" r="{r*0.22:.1f}" fill="{col}" stroke="#0F172A" stroke-width="2.5"/>
      <circle cx="{cx}" cy="{cy}" r="{r*0.1:.1f}" fill="#0F172A"/>
    </g>"""

def crown(cx, cy, scale=1.0, pearls=9):
    w = 120 * scale
    h = 45 * scale
    x = cx - w/2
    y = cy
    p_dots = "".join([f'<circle cx="{x + w*i/(pearls-1):.1f}" cy="{y - (8 if i in [0, pearls-1] else 18):.1f}" r="{4*scale:.1f}" fill="url(#steelGrad)" stroke="url(#goldGrad)" stroke-width="1"/>' for i in range(pearls)])
    return f"""<g filter="url(#dropShadow)">
      <path d="M {x} {y+h} L {x+w} {y+h} L {x+w*0.95} {y+h*0.3} L {x+w} {y} L {x+w*0.75} {y+h*0.4} L {x+w*0.5} {y-5} L {x+w*0.25} {y+h*0.4} L {x} {y} L {x+w*0.05} {y+h*0.3} Z" fill="url(#goldGrad)" stroke="#553D00" stroke-width="2"/>
      <rect x="{x+w*0.08}" y="{y+h*0.65}" width="{w*0.84}" height="{h*0.25}" rx="3" fill="url(#madderRed)" stroke="url(#goldGrad)" stroke-width="1.5"/>
      {p_dots}
    </g>"""

def eagle(cx, cy, s=1.0):
    return f"""<g transform="translate({cx},{cy}) scale({s})" filter="url(#dropShadow)">
      <!-- Double-headed Imperial Eagle Silhouette -->
      <path d="M 0,-40 C -15,-55 -30,-45 -35,-30 C -45,-30 -50,-20 -40,-10 C -60,0 -80,25 -70,60 C -55,50 -40,45 -30,55 C -25,75 -10,85 0,80 C 10,85 25,75 30,55 C 40,45 55,50 70,60 C 80,25 60,0 40,-10 C 50,-20 45,-30 35,-30 C 30,-45 15,-55 0,-40 Z" fill="url(#goldGrad)" stroke="#4A3B00" stroke-width="2"/>
      <circle cx="-16" cy="-45" r="4" fill="url(#steelGrad)"/>
      <circle cx="16" cy="-45" r="4" fill="url(#steelGrad)"/>
      <path d="M -8,-25 L 8,-25 L 12,10 L 0,22 L -12,10 Z" fill="url(#madderRed)" stroke="url(#goldGrad)" stroke-width="2"/>
    </g>"""

# === GROUP 1 (12 LOGOS) ===
for i in range(1, 13):
    idx = f"01_{i:02d}"
    if i == 1:
        c = f"{eagle(250, 180, 0.85)}{wheel(250, 310, 65)}<text x='250' y='318' text-anchor='middle' font-family='serif' font-size='26' font-weight='bold' fill='#0F172A'>АК</text>"
        t, sub = "Имперский Триумф 1896", "Т-во Мануфактур А. Каретниковой"
    elif i == 2:
        c = f"{wheel(250, 240, 95)}<text x='250' y='248' text-anchor='middle' font-family='serif' font-size='32' font-weight='bold' fill='url(#goldGrad)'>С.И.К.</text>"
        t, sub = "Пломба Степана Каретникова", "Основано въ 1787 году"
    elif i == 3:
        c = f"""<circle cx='250' cy='240' r='100' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='4'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='56' font-weight='bold' fill='url(#goldGrad)'>ИПК</text>
        <circle cx='250' cy='240' r='85' fill='none' stroke='url(#goldGrad)' stroke-width='1.5' stroke-dasharray='6,4'/>"""
        t, sub = "Пунцовый Венец Тейкова", "Иванъ Петровичъ Каретниковъ"
    elif i == 4:
        c = f"""<path d='M 170,150 L 330,150 L 310,310 L 250,350 L 190,310 Z' fill='url(#azureGrad)' stroke='url(#goldGrad)' stroke-width='4'/>
        <text x='250' y='265' text-anchor='middle' font-family='serif' font-size='60' font-weight='bold' fill='url(#goldGrad)'>ВК</text>
        {crown(250, 115, 0.9)}"""
        t, sub = "Купеческий Торговый Дом", "Василій Степановичъ Каретниковъ"
    elif i == 5:
        c = f"""<polygon points='250,130 280,210 360,210 295,260 320,340 250,290 180,340 205,260 140,210 220,210' fill='url(#goldGrad)' opacity='0.3'/>
        {wheel(250, 240, 75)}<text x='250' y='247' text-anchor='middle' font-family='serif' font-size='22' font-weight='bold' fill='#0F172A'>ОРЕНБУРГЪ</text>"""
        t, sub = "Караванный Звездный Медальон", "Оренбургскій Меновой Дворъ"
    elif i == 6:
        c = f"""<rect x='130' y='160' width='240' height='160' rx='18' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='4'/>
        <rect x='140' y='170' width='220' height='140' rx='12' fill='none' stroke='url(#steelGrad)' stroke-width='2' stroke-dasharray='8,4'/>
        <text x='250' y='225' text-anchor='middle' font-family='serif' font-size='24' font-weight='bold' fill='url(#steelGrad)'>КАРЕТНИКОВЪ</text>
        <text x='250' y='275' text-anchor='middle' font-family='serif' font-size='18' font-weight='bold' fill='url(#goldGrad)'>ВЫСШІЙ СОРТЪ</text>"""
        t, sub = "Клеймо Высшего Сорта", "Штемпель кромки полотна"
    elif i == 7:
        c = f"""<circle cx='250' cy='240' r='100' fill='url(#goldGrad)' stroke='#6B4E03' stroke-width='6'/>
        <circle cx='250' cy='240' r='88' fill='url(#darkSlate)' stroke='url(#goldGrad)' stroke-width='2'/>
        <text x='250' y='230' text-anchor='middle' font-family='serif' font-size='22' font-weight='bold' fill='url(#goldGrad)'>ЗА ПОЛЕЗНОЕ</text>
        <text x='250' y='268' text-anchor='middle' font-family='serif' font-size='16' fill='#E2E8F0'>1835 • ТРУДЫ</text>"""
        t, sub = "Медаль За Полезное 1835", "Первая выставка мануфактуръ"
    elif i == 8:
        c = f"""<circle cx='250' cy='240' r='105' fill='none' stroke='url(#goldGrad)' stroke-width='8' stroke-dasharray='14,4'/>
        <circle cx='250' cy='240' r='85' fill='url(#azureGrad)' stroke='url(#goldGrad)' stroke-width='3'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='38' font-weight='bold' fill='url(#goldGrad)'>Т.М.А.К.</text>"""
        t, sub = "Паевой Капиталъ 1877", "Товарищество Александры Каретниковой"
    elif i == 9:
        c = f"""<circle cx='250' cy='240' r='95' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='4'/>
        <path d='M 250,150 Q 290,190 280,240 Q 270,290 230,300 Q 190,290 200,240 Q 210,190 250,150 Z' fill='url(#goldGrad)'/>
        <text x='250' y='245' text-anchor='middle' font-family='serif' font-size='24' font-weight='bold' fill='#8B1E1E'>К</text>"""
        t, sub = "Пунцовый Огурец Экспорта", "Азіатская набивная марка"
    elif i == 10:
        c = f"""<line x1='160' y1='160' x2='340' y2='320' stroke='url(#goldGrad)' stroke-width='10' stroke-linecap='round'/>
        <line x1='340' y1='160' x2='160' y2='320' stroke='url(#goldGrad)' stroke-width='10' stroke-linecap='round'/>
        <circle cx='250' cy='240' r='45' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='4'/>
        <text x='250' y='252' text-anchor='middle' font-family='serif' font-size='36' font-weight='bold' fill='url(#goldGrad)'>К</text>"""
        t, sub = "Челнокъ и Веретено", "Ткацкая слава Тейкова"
    elif i == 11:
        c = f"""{wheel(250, 240, 85, 12)}
        <circle cx='250' cy='240' r='50' fill='url(#azureGrad)' stroke='url(#goldGrad)' stroke-width='3'/>
        <text x='250' y='248' text-anchor='middle' font-family='serif' font-size='22' font-weight='bold' fill='url(#goldGrad)'>МСК • НН</text>"""
        t, sub = "Большая Ярмарочная Печать", "Нижегородско-Московскій торгъ"
    else:
        c = f"""<polygon points='250,140 330,175 350,260 295,330 205,330 150,260 170,175' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='5'/>
        <text x='250' y='258' text-anchor='middle' font-family='serif' font-size='56' font-weight='bold' fill='url(#goldGrad)'>К</text>
        <circle cx='250' cy='180' r='6' fill='url(#goldGrad)'/>"""
        t, sub = "Сердоликовый Перстень К", "Купеческая личная инталія"
    base_svg(f"logo_{idx}.svg", t, sub, c)

# === GROUP 2 (12 LOGOS) ===
for i in range(1, 13):
    idx = f"02_{i:02d}"
    if i == 1:
        c = f"""<rect x='160' y='150' width='180' height='180' rx='14' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='5'/>
        <rect x='175' y='165' width='150' height='150' rx='10' fill='none' stroke='url(#steelGrad)' stroke-width='2' stroke-dasharray='6,4'/>
        <text x='250' y='265' text-anchor='middle' font-family='serif' font-size='70' font-weight='bold' fill='url(#goldGrad)'>К</text>"""
        t, sub = "Золотая Набивная Манера", "Грушевая матрица с латунью"
    elif i == 2:
        c = f"""<path d='M 250,140 Q 330,200 310,280 Q 290,340 220,335 Q 160,330 175,270 Q 190,200 250,140 Z' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='5'/>
        {wheel(245, 260, 38, 8)}"""
        t, sub = "Царский Пунцовый Огурец", "Адріанопольскій секретъ красителя"
    elif i == 3:
        c = f"""<rect x='130' y='170' width='240' height='140' fill='#8B2500' stroke='#3E1000' stroke-width='5'/>
        <rect x='145' y='185' width='210' height='110' fill='#5A1800' stroke='none'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='32' font-weight='bold' fill='#FFD7A8'>Т.М.А.К.</text>"""
        t, sub = "Кирпичное Клеймо Т.М.А.К.", "Кладка фабричныхъ корпусовъ"
    elif i == 4:
        c = f"""<circle cx='250' cy='240' r='100' fill='url(#darkSlate)' stroke='url(#steelGrad)' stroke-width='6'/>
        <circle cx='250' cy='240' r='88' fill='none' stroke='url(#goldGrad)' stroke-width='2' stroke-dasharray='12,6'/>
        <text x='250' y='245' text-anchor='middle' font-family='serif' font-size='52' font-weight='bold' fill='url(#steelGrad)'>АК</text>
        <text x='250' y='285' text-anchor='middle' font-family='serif' font-size='24' font-weight='bold' fill='url(#goldGrad)'>1882</text>"""
        t, sub = "Чугунная Лестница 1882", "Подлинное литье въ Тейковѣ"
    elif i == 5:
        c = f"""<path d='M 170,300 C 190,260 240,270 250,285 C 260,270 310,260 330,300 L 330,320 C 310,280 260,290 250,305 C 240,290 190,280 170,320 Z' fill='url(#steelGrad)'/>
        <circle cx='250' cy='210' r='35' fill='url(#goldGrad)'/>
        <text x='250' y='218' text-anchor='middle' font-family='serif' font-size='22' font-weight='bold' fill='#0F172A'>ИВК</text>"""
        t, sub = "Светоч Библиотеки 1894", "Бесплатная народная библіотека"
    elif i == 6:
        c = f"""<path d='M 250,150 C 230,150 200,180 195,280 L 305,280 C 300,180 270,150 250,150 Z' fill='url(#goldGrad)' stroke='#553D00' stroke-width='3'/>
        <rect x='185' y='280' width='130' height='20' rx='4' fill='url(#goldGrad)' stroke='#553D00' stroke-width='2'/>
        <text x='250' y='240' text-anchor='middle' font-family='serif' font-size='28' font-weight='bold' fill='#240404'>СК</text>
        <text x='250' y='265' text-anchor='middle' font-family='serif' font-size='14' fill='#240404'>1844</text>"""
        t, sub = "Ктиторский Колокол 1844", "Ильинскій храмъ въ Тейковѣ"
    elif i == 7:
        c = f"""<circle cx='250' cy='240' r='90' fill='url(#emeraldGrad)' stroke='url(#goldGrad)' stroke-width='4'/>
        <circle cx='250' cy='240' r='40' fill='#FFFFFF' stroke='url(#goldGrad)' stroke-width='2'/>
        <text x='250' y='248' text-anchor='middle' font-family='serif' font-size='24' font-weight='bold' fill='#065F46'>ХЛОПОКЪ</text>"""
        t, sub = "Крапп и Хлопок", "Символъ текстильной династіи"
    elif i == 8:
        c = f"""<polygon points='250,150 330,240 250,330 170,240' fill='url(#darkSlate)' stroke='url(#goldGrad)' stroke-width='4'/>
        <text x='250' y='260' text-anchor='middle' font-family='serif' font-size='60' font-weight='bold' fill='url(#goldGrad)'>К</text>"""
        t, sub = "Латунное Пико Мастера", "Точечный наборъ узора"
    elif i == 9:
        c = f"""<path d='M 180,320 L 180,210 Q 250,140 320,210 L 320,320 Z' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='5'/>
        <circle cx='250' cy='220' r='24' fill='url(#goldGrad)'/>
        <text x='250' y='280' text-anchor='middle' font-family='serif' font-size='22' font-weight='bold' fill='url(#goldGrad)'>1787</text>"""
        t, sub = "Тейковская Арка Фабрики", "Прядильный и ткацкій корпусъ"
    elif i == 10:
        c = f"""<rect x='160' y='150' width='180' height='180' fill='url(#steelGrad)' stroke='url(#goldGrad)' stroke-width='5'/>
        <text x='250' y='240' text-anchor='middle' font-family='serif' font-size='28' font-weight='bold' fill='#0F172A'>84 ПРОБА</text>
        <text x='250' y='275' text-anchor='middle' font-family='serif' font-size='16' fill='#0F172A'>В.С.К. • 1868</text>"""
        t, sub = "Серебряный Оклад 84", "Вкладъ въ Никольскій соборъ"
    elif i == 11:
        c = f"""<circle cx='250' cy='240' r='90' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='4'/>
        <path d='M 210,240 Q 250,180 290,240 Q 250,300 210,240 Z' fill='url(#goldGrad)'/>
        <circle cx='250' cy='240' r='15' fill='#8B1E1E'/>"""
        t, sub = "Роза и Золотой Колос", "Купеческое хлѣбосольство"
    else:
        c = f"""<line x1='250' y1='150' x2='250' y2='330' stroke='url(#goldGrad)' stroke-width='8'/>
        <line x1='190' y1='210' x2='310' y2='210' stroke='url(#goldGrad)' stroke-width='8'/>
        <line x1='215' y1='175' x2='285' y2='175' stroke='url(#goldGrad)' stroke-width='5'/>
        <line x1='220' y1='290' x2='280' y2='290' stroke='url(#goldGrad)' stroke-width='5'/>"""
        t, sub = "Вечный Крест Памяти", "Некрополь храма въ Тейковѣ"
    base_svg(f"logo_{idx}.svg", t, sub, c)

# === GROUP 3 (15 LOGOS) ===
for i in range(1, 16):
    idx = f"03_{i:02d}"
    if i == 1:
        c = f"{wheel(250, 240, 85, 8)}<text x='250' y='250' text-anchor='middle' font-family='serif' font-size='32' font-weight='bold' fill='url(#goldGrad)'>К</text>"
        t, sub = "Золотое Колесо Каретника", "Царскій каретный мастеръ"
    elif i == 2:
        c = f"""<path d='M 170,220 C 170,180 210,170 250,170 C 290,170 330,180 330,220 L 320,280 L 180,280 Z' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='4'/>
        {wheel(190, 290, 30, 8)}
        {wheel(310, 290, 30, 8)}
        {crown(250, 115, 0.75)}"""
        t, sub = "Герб Каретного Ряда", "Парадная карета на рессорахъ"
    elif i == 3:
        c = f"""{wheel(250, 240, 85, 12)}
        <line x1='180' y1='170' x2='320' y2='310' stroke='url(#steelGrad)' stroke-width='8' stroke-linecap='round'/>
        <line x1='320' y1='170' x2='180' y2='310' stroke='url(#steelGrad)' stroke-width='8' stroke-linecap='round'/>"""
        t, sub = "Циркуль и Тесло Мастера", "Ремесленный цеховой инструментъ"
    elif i == 4:
        c = f"""<path d='M 170,160 L 330,160 L 310,300 L 250,340 L 190,300 Z' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='4'/>
        <circle cx='250' cy='235' r='45' fill='none' stroke='url(#goldGrad)' stroke-width='6'/>
        <line x1='250' y1='160' x2='250' y2='310' stroke='url(#goldGrad)' stroke-width='5'/>
        <line x1='170' y1='235' x2='330' y2='235' stroke='url(#goldGrad)' stroke-width='5'/>"""
        t, sub = "Стрелецкое Знамя Мценска", "Служилые люди XVII вѣка"
    elif i == 5:
        c = f"""<line x1='160' y1='240' x2='340' y2='240' stroke='url(#steelGrad)' stroke-width='16' stroke-linecap='round'/>
        {wheel(250, 240, 75, 12)}
        <circle cx='250' cy='240' r='20' fill='url(#madderRed)'/>"""
        t, sub = "Пушкарский Лафет Орла", "Обозные мастера черты"
    elif i == 6:
        c = f"""<circle cx='250' cy='240' r='90' fill='none' stroke='url(#steelGrad)' stroke-width='12'/>
        <text x='250' y='268' text-anchor='middle' font-family='serif' font-size='90' font-weight='bold' fill='url(#steelGrad)'>К</text>"""
        t, sub = "Тавро Кирилла Каретникова", "с. Владиміровка • 1858 г."
    elif i == 7:
        c = f"""<rect x='170' y='180' width='160' height='120' rx='14' fill='none' stroke='url(#steelGrad)' stroke-width='10'/>
        <line x1='250' y1='135' x2='250' y2='180' stroke='url(#steelGrad)' stroke-width='10'/>
        <line x1='225' y1='155' x2='275' y2='155' stroke='url(#steelGrad)' stroke-width='10'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='50' font-weight='bold' fill='url(#steelGrad)'>И-К</text>"""
        t, sub = "Тавро Ивана Кирилловича", "с. Залесово Бузулукскаго уѣзда"
    elif i == 8:
        c = f"""<path d='M 180,180 C 180,240 230,260 250,280 C 270,260 320,240 320,180' fill='none' stroke='url(#goldGrad)' stroke-width='12' stroke-linecap='round'/>
        <line x1='250' y1='280' x2='250' y2='330' stroke='url(#goldGrad)' stroke-width='12'/>
        <text x='250' y='225' text-anchor='middle' font-family='serif' font-size='60' font-weight='bold' fill='url(#goldGrad)'>Г</text>"""
        t, sub = "Степной Ключ Григория", "Прадедъ Григорій Ивановичъ #8"
    elif i == 9:
        c = f"""<path d='M 180,170 C 180,290 320,290 320,170' fill='none' stroke='url(#steelGrad)' stroke-width='14'/>
        {wheel(250, 230, 45, 8)}"""
        t, sub = "Подкова и Каретный Обод", "Кузнечное мастерство степи"
    elif i == 10:
        c = f"""<line x1='250' y1='150' x2='250' y2='330' stroke='url(#steelGrad)' stroke-width='8'/>
        <line x1='190' y1='200' x2='310' y2='200' stroke='url(#steelGrad)' stroke-width='8'/>
        <line x1='250' y1='330' x2='200' y2='300' stroke='url(#steelGrad)' stroke-width='8'/>
        <line x1='250' y1='330' x2='300' y2='300' stroke='url(#steelGrad)' stroke-width='8'/>"""
        t, sub = "Троеперстный Межевой Рубеж", "Однодворческое знамя пашни"
    elif i == 11:
        c = f"""{wheel(250, 240, 85, 8)}
        <polygon points='250,170 270,220 320,230 280,260 295,310 250,280 205,310 220,260 180,230 230,220' fill='url(#goldGrad)'/>"""
        t, sub = "Степной Тулпар и Колесо", "Вольная степь Оренбуржья"
    elif i == 12:
        c = f"""<rect x='170' y='160' width='160' height='160' fill='url(#darkSlate)' stroke='url(#steelGrad)' stroke-width='10'/>
        <circle cx='250' cy='240' r='50' fill='none' stroke='url(#steelGrad)' stroke-width='6'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='42' font-weight='bold' fill='url(#steelGrad)'>К</text>"""
        t, sub = "Клеймо Кованой Оси", "Ударный стальной чеканъ"
    elif i == 13:
        c = f"""<rect x='235' y='140' width='30' height='190' fill='url(#steelGrad)' stroke='url(#goldGrad)' stroke-width='3'/>
        <polygon points='250,110 275,140 225,140' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='2'/>
        {wheel(250, 260, 45, 8)}"""
        t, sub = "Подорожный Столб Тракта", "Орёлъ — Самара — Оренбургъ"
    elif i == 14:
        c = f"""<polygon points='200,150 300,150 330,240 300,330 200,330 170,240' fill='url(#goldGrad)' stroke='#6B4E03' stroke-width='4'/>
        <text x='250' y='252' text-anchor='middle' font-family='serif' font-size='36' font-weight='bold' fill='#0F172A'>ЖЕРЕБЕЙ</text>"""
        t, sub = "Жеребьевая Бирка Общины", "Сходъ села Ивановка"
    else:
        c = f"""{wheel(250, 240, 85, 16)}
        <circle cx='250' cy='240' r='98' fill='none' stroke='url(#goldGrad)' stroke-width='3' stroke-dasharray='12,6'/>
        <circle cx='250' cy='240' r='30' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='3'/>
        <text x='250' y='248' text-anchor='middle' font-family='serif' font-size='24' font-weight='bold' fill='url(#goldGrad)'>∞</text>"""
        t, sub = "Солнечное Колесо Пути", "Символъ вѣчнаго движенія рода"
    base_svg(f"logo_{idx}.svg", t, sub, c)

# === GROUP 4 (10 LOGOS) ===
for i in range(1, 11):
    idx = f"04_{i:02d}"
    if i == 1:
        c = f"""<path d='M 170,240 C 210,180 290,180 330,240 C 290,300 210,300 170,240 Z' fill='none' stroke='url(#goldGrad)' stroke-width='6'/>
        <circle cx='250' cy='240' r='20' fill='url(#goldGrad)'/>
        <text x='250' y='246' text-anchor='middle' font-family='serif' font-size='16' font-weight='bold' fill='#0F172A'>СК</text>"""
        t, sub = "Узел Чести Степана 1842", "Купеческій росчеркъ пера"
    elif i == 2:
        c = f"""<circle cx='250' cy='240' r='90' fill='url(#darkSlate)' stroke='url(#steelGrad)' stroke-width='4'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='50' font-weight='bold' fill='url(#steelGrad)'>ВК</text>
        <path d='M 190,270 Q 250,290 310,265' fill='none' stroke='url(#goldGrad)' stroke-width='4'/>"""
        t, sub = "Росчерк Деда Валентина #4", "Энергичный трудовой вензель"
    elif i == 3:
        c = f"""<polygon points='250,150 270,210 330,210 280,240 300,300 250,265 200,300 220,240 170,210 230,210' fill='url(#steelGrad)' stroke='url(#goldGrad)' stroke-width='3'/>
        {wheel(250, 240, 35, 8)}"""
        t, sub = "Оровайский Воинский Крест", "195-й пѣхотный полкъ • 1811–1911"
    elif i == 4:
        c = f"""<line x1='160' y1='170' x2='340' y2='310' stroke='url(#goldGrad)' stroke-width='14' stroke-linecap='round'/>
        <line x1='340' y1='170' x2='160' y2='310' stroke='url(#goldGrad)' stroke-width='14' stroke-linecap='round'/>
        <polygon points='250,195 262,230 300,230 270,250 280,285 250,265 220,285 230,250 200,230 238,230' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='2'/>"""
        t, sub = "Артиллерийский Щит ВОВ", "Гвардіи ст. сержантъ Ф. Каретниковъ"
    elif i == 5:
        c = f"""<path d='M 180,160 L 320,160 L 300,290 L 250,330 L 200,290 Z' fill='url(#azureGrad)' stroke='url(#goldGrad)' stroke-width='4'/>
        <path d='M 230,260 C 230,220 270,220 270,260 L 270,280 L 230,280 Z' fill='url(#goldGrad)'/>
        {wheel(250, 210, 30, 8)}"""
        t, sub = "Олень Бузулука и Колесо", "Ивановская волость"
    elif i == 6:
        c = f"""<line x1='180' y1='320' x2='320' y2='160' stroke='url(#goldGrad)' stroke-width='6'/>
        <line x1='180' y1='160' x2='320' y2='320' stroke='url(#steelGrad)' stroke-width='6'/>
        <circle cx='250' cy='240' r='25' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='2'/>"""
        t, sub = "Перо и Штык Рода", "Лѣтопись и ратный подвигъ"
    elif i == 7:
        c = f"""<polygon points='250,140 272,210 345,210 285,250 308,320 250,275 192,320 215,250 155,210 228,210' fill='url(#steelGrad)' stroke='url(#goldGrad)' stroke-width='4'/>
        <text x='250' y='250' text-anchor='middle' font-family='serif' font-size='28' font-weight='bold' fill='#0F172A'>К</text>"""
        t, sub = "Звезда Отваги Предков", "Медаль «За отвагу» 1944 г."
    elif i == 8:
        c = f"""<line x1='250' y1='150' x2='250' y2='330' stroke='url(#steelGrad)' stroke-width='8'/>
        <path d='M 210,230 Q 250,170 290,230' fill='none' stroke='url(#goldGrad)' stroke-width='6'/>
        <path d='M 210,270 Q 250,210 290,270' fill='none' stroke='url(#goldGrad)' stroke-width='6'/>"""
        t, sub = "Подольский Колос и Меч", "Оренбургская земля отцовъ"
    elif i == 9:
        c = f"""<rect x='160' y='160' width='180' height='160' rx='20' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='6'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='44' font-weight='bold' fill='url(#goldGrad)'>ГИК</text>"""
        t, sub = "Перстень Григория Ивановича", "Семейная сургучная печать"
    else:
        c = f"""<path d='M 200,320 L 300,320 L 280,280 L 220,280 Z' fill='url(#goldGrad)'/>
        <path d='M 250,150 C 290,200 300,240 250,280 C 200,240 210,200 250,150 Z' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='3'/>"""
        t, sub = "Вечный Огонь Поколений", "Память прадедовъ-воиновъ"
    base_svg(f"logo_{idx}.svg", t, sub, c)

# === GROUP 5 (12 LOGOS - KUMANIN) ===
for i in range(1, 13):
    idx = f"05_{i:02d}"
    if i == 1:
        c = f"""<path d='M 170,160 L 330,160 L 310,290 L 250,335 L 190,290 Z' fill='url(#azureGrad)' stroke='url(#goldGrad)' stroke-width='4'/>
        <path d='M 170,160 L 330,160 L 330,245 L 170,245 Z' fill='url(#goldGrad)' opacity='0.4'/>
        <path d='M 200,210 C 220,180 250,180 260,200 L 230,225 Z' fill='#000000'/>
        <circle cx='230' cy='200' r='5' fill='url(#steelGrad)'/>
        <text x='250' y='300' text-anchor='middle' font-family='serif' font-size='22' font-weight='bold' fill='url(#goldGrad)'>ОГ XI, 54</text>"""
        t, sub = "Герб Куманиных ОГ XI, 54", "Дворянскій жалованный гербъ"
    elif i == 2:
        c = f"""<path d='M 180,240 C 220,160 300,160 330,200 C 300,220 280,250 260,280 C 240,260 210,250 180,240 Z' fill='#000000' stroke='url(#steelGrad)' stroke-width='2'/>
        <polygon points='270,195 275,208 290,208 278,216 282,230 270,220 258,230 262,216 250,208 265,208' fill='url(#steelGrad)'/>"""
        t, sub = "Черное Крыло и Звезда", "Символъ высочайшаго возвышенія"
    elif i == 3:
        c = f"""<line x1='250' y1='150' x2='250' y2='330' stroke='url(#goldGrad)' stroke-width='8'/>
        <circle cx='250' cy='150' r='14' fill='url(#goldGrad)'/>
        <path d='M 220,190 Q 250,170 280,190 Q 250,210 220,230 Q 250,250 280,270' fill='none' stroke='url(#steelGrad)' stroke-width='4'/>"""
        t, sub = "Кадуцей Градоначальника", "Алексей Алексѣевичъ Куманинъ 1812"
    elif i == 4:
        c = f"""<path d='M 190,280 C 190,200 270,180 300,210 C 280,220 230,230 220,280 Z' fill='url(#steelGrad)' stroke='url(#goldGrad)' stroke-width='2'/>
        <line x1='220' y1='280' x2='200' y2='310' stroke='url(#goldGrad)' stroke-width='6'/>
        <line x1='250' y1='310' x2='300' y2='200' stroke='url(#goldGrad)' stroke-width='4'/>"""
        t, sub = "Серп и Колосья Шуструя", "Хлѣбопашество и благотвореніе"
    elif i == 5:
        c = f"""<circle cx='250' cy='240' r='90' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='4'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='50' font-weight='bold' fill='url(#goldGrad)'>ААК</text>"""
        t, sub = "Вензель Мэра 1812 — ААК", "Герой Отечественной войны"
    elif i == 6:
        c = f"""<rect x='170' y='200' width='160' height='120' fill='url(#darkSlate)' stroke='url(#goldGrad)' stroke-width='4'/>
        <line x1='190' y1='200' x2='190' y2='320' stroke='url(#steelGrad)' stroke-width='6'/>
        <line x1='230' y1='200' x2='230' y2='320' stroke='url(#steelGrad)' stroke-width='6'/>
        <line x1='270' y1='200' x2='270' y2='320' stroke='url(#steelGrad)' stroke-width='6'/>
        <line x1='310' y1='200' x2='310' y2='320' stroke='url(#steelGrad)' stroke-width='6'/>
        <polygon points='250,150 340,200 160,200' fill='url(#goldGrad)'/>"""
        t, sub = "Усадьба Ордынка 17", "Опекуны Ѳ. М. Достоевскаго"
    elif i == 7:
        c = f"""<path d='M 170,160 L 330,160 L 300,320 L 250,340 L 200,320 Z' fill='url(#azureGrad)' stroke='url(#steelGrad)' stroke-width='4'/>
        <line x1='250' y1='160' x2='250' y2='340' stroke='url(#madderRed)' stroke-width='8'/>
        <line x1='170' y1='230' x2='330' y2='230' stroke='url(#madderRed)' stroke-width='8'/>"""
        t, sub = "Стяг Ломовской Черты", "Служилые казаки 1640 г."
    elif i == 8:
        c = f"""<circle cx='210' cy='220' r='45' fill='none' stroke='url(#goldGrad)' stroke-width='6'/>
        <circle cx='290' cy='220' r='45' fill='none' stroke='url(#goldGrad)' stroke-width='6'/>
        <circle cx='250' cy='280' r='45' fill='none' stroke='url(#goldGrad)' stroke-width='6'/>"""
        t, sub = "Три Кольца Согласия", "Братья Куманины"
    elif i == 9:
        c = f"""<ellipse cx='250' cy='240' rx='75' ry='95' fill='url(#darkSlate)' stroke='url(#goldGrad)' stroke-width='5'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='56' font-weight='bold' fill='url(#goldGrad)'>КК</text>
        {crown(250, 115, 0.75)}"""
        t, sub = "Инталия Константина Куманина", "Дипломъ ДС XIX, 30 • 1836 г."
    elif i == 10:
        c = f"""<path d='M 170,270 Q 250,330 330,270 L 310,240 L 190,240 Z' fill='url(#azureGrad)' stroke='url(#goldGrad)' stroke-width='3'/>
        <line x1='250' y1='160' x2='250' y2='240' stroke='url(#goldGrad)' stroke-width='5'/>
        <polygon points='250,170 290,200 250,230' fill='url(#steelGrad)'/>"""
        t, sub = "Ладья Переславля", "Горицкій монастырь XVI в."
    elif i == 11:
        c = f"""<circle cx='250' cy='240' r='90' fill='url(#azureGrad)' stroke='url(#steelGrad)' stroke-width='4'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='44' font-weight='bold' fill='url(#steelGrad)'>ВСК</text>"""
        t, sub = "Вензель Валентины #7", "Бабушка по матери Куманина"
    else:
        c = f"""<circle cx='250' cy='240' r='95' fill='none' stroke='url(#goldGrad)' stroke-width='6'/>
        <circle cx='250' cy='240' r='80' fill='url(#steelGrad)' opacity='0.2'/>
        <text x='250' y='235' text-anchor='middle' font-family='serif' font-size='20' font-weight='bold' fill='url(#goldGrad)'>ВѢРНОСТЬЮ</text>
        <text x='250' y='265' text-anchor='middle' font-family='serif' font-size='16' fill='#FFFFFF'>И БЛАГОТВОРЕНІЕМЪ</text>"""
        t, sub = "Хрустальная Печать Рода", "Девизъ Дома Куманиныхъ"
    base_svg(f"logo_{idx}.svg", t, sub, c)

# === GROUP 6 (12 LOGOS - ZUBKOV & YUKHIN) ===
for i in range(1, 13):
    idx = f"06_{i:02d}"
    if i <= 6:
        # Zubkov (1-6)
        if i == 1:
            c = f"""<path d='M 170,160 L 330,160 L 310,290 L 250,330 L 190,290 Z' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='4'/>
            <path d='M 180,260 L 200,260 L 200,240 L 220,240 L 220,260 L 240,260 L 240,240 L 260,240 L 260,260 L 280,260 L 280,240 L 300,240 L 300,260 L 320,260 L 310,290 L 250,330 L 190,290 Z' fill='url(#azureGrad)'/>
            <line x1='250' y1='170' x2='250' y2='290' stroke='url(#steelGrad)' stroke-width='8'/>"""
            t, sub = "Гласный Щит Зубковых", "Зубчатая стѣна и мечъ"
        elif i == 2:
            c = f"""<line x1='170' y1='170' x2='330' y2='310' stroke='url(#steelGrad)' stroke-width='10' stroke-linecap='round'/>
            <line x1='330' y1='170' x2='170' y2='310' stroke='url(#steelGrad)' stroke-width='10' stroke-linecap='round'/>
            <circle cx='250' cy='240' r='30' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='3'/>
            <text x='250' y='250' text-anchor='middle' font-family='serif' font-size='32' font-weight='bold' fill='url(#goldGrad)'>З</text>"""
            t, sub = "Бердыши Нового Шуструя", "Ратные люди Ломовской черты"
        elif i == 3:
            c = f"""<polygon points='250,150 330,290 170,290' fill='none' stroke='url(#goldGrad)' stroke-width='5'/>
            <circle cx='250' cy='230' r='12' fill='url(#steelGrad)'/>
            <text x='250' y='275' text-anchor='middle' font-family='serif' font-size='16' font-weight='bold' fill='url(#goldGrad)'>1818</text>"""
            t, sub = "Звезда Просвещения 1818", "Ложа «Соединённыхъ славянъ»"
        elif i == 4:
            c = f"""<polygon points='250,150 320,185 320,275 250,310 180,275 180,185' fill='url(#darkSlate)' stroke='url(#goldGrad)' stroke-width='4'/>
            <text x='250' y='250' text-anchor='middle' font-family='serif' font-size='48' font-weight='bold' fill='url(#goldGrad)'>VZ</text>
            {crown(250, 125, 0.65)}"""
            t, sub = "Печатка Сенатора VZ", "Василій Петровичъ Зубковъ"
        elif i == 5:
            c = f"""<circle cx='250' cy='240' r='90' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='5'/>
            <text x='250' y='250' text-anchor='middle' font-family='serif' font-size='48' font-weight='bold' fill='url(#goldGrad)'>ВЗ</text>
            <text x='250' y='285' text-anchor='middle' font-family='serif' font-size='16' fill='#FFFFFF'>15 ДВОРОВЪ</text>"""
            t, sub = "Пятнадцать Дворов Шуструя", "Перепись 1917 г. • Дѣдъ Владиміръ"
        else:
            c = f"""<line x1='190' y1='310' x2='310' y2='170' stroke='url(#goldGrad)' stroke-width='6'/>
            <line x1='190' y1='170' x2='310' y2='310' stroke='url(#steelGrad)' stroke-width='6'/>
            <circle cx='250' cy='240' r='20' fill='url(#azureGrad)' stroke='url(#goldGrad)' stroke-width='2'/>"""
            t, sub = "Перо и Шпага Дружбы", "Союзъ съ А. С. Пушкинымъ"
    else:
        # Yukhin (7-12)
        if i == 7:
            c = f"""<path d='M 170,160 L 330,160 L 310,290 L 250,330 L 190,290 Z' fill='url(#goldGrad)' stroke='#6B4E03' stroke-width='4'/>
            <path d='M 170,220 Q 210,250 250,220 Q 290,190 330,220 L 320,260 Q 290,230 250,260 Q 210,290 170,260 Z' fill='url(#azureGrad)'/>"""
            t, sub = "Пояс Реки Кондурча", "д. Четыровка Самарской губ."
        elif i == 8:
            c = f"""<line x1='250' y1='150' x2='250' y2='330' stroke='url(#steelGrad)' stroke-width='8'/>
            <path d='M 230,200 Q 210,160 250,140 Q 290,160 270,200 Z' fill='url(#madderRed)'/>
            <line x1='220' y1='180' x2='280' y2='180' stroke='url(#goldGrad)' stroke-width='6'/>"""
            t, sub = "Меч Архистратига Михаила", "Приходъ с. Русская Васильевка"
        elif i == 9:
            c = f"""<circle cx='250' cy='240' r='90' fill='url(#goldGrad)' stroke='#553D00' stroke-width='4'/>
            <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='56' font-weight='bold' fill='#0F172A'>ПЮ</text>
            <text x='250' y='285' text-anchor='middle' font-family='serif' font-size='16' fill='#0F172A'>#10 • ПЕТРЪ</text>"""
            t, sub = "Сноп Петра Юхина #10", "Хлѣбопашецъ Самарскаго Заволжья"
        elif i == 10:
            c = f"""{wheel(250, 240, 75, 8, "url(#steelGrad)")}
            <path d='M 240,160 L 260,160 L 255,320 L 245,320 Z' fill='url(#goldGrad)'/>"""
            t, sub = "Мельничное Колесо Кондурчи", "Водяныя мельницы Кошекъ"
        elif i == 11:
            c = f"""<circle cx='250' cy='240' r='90' fill='url(#azureGrad)' stroke='url(#steelGrad)' stroke-width='4'/>
            <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='44' font-weight='bold' fill='url(#steelGrad)'>КПЮ</text>"""
            t, sub = "Вензель Клавдии #5", "Бабушка по отцу Юхина"
        else:
            c = f"""<circle cx='250' cy='240' r='90' fill='url(#darkSlate)' stroke='url(#goldGrad)' stroke-width='4'/>
            <path d='M 210,250 C 210,210 290,210 290,250 Z' fill='url(#steelGrad)'/>
            <text x='250' y='280' text-anchor='middle' font-family='serif' font-size='18' font-weight='bold' fill='url(#goldGrad)'>ЧЕТЫРОВКА</text>"""
            t, sub = "Колыбель Четыровки", "1391 Битва • 1840 Поселеніе"
    base_svg(f"logo_{idx}.svg", t, sub, c)

# === GROUP 7 (20 LOGOS - COUNT KARETNIKOV MASTER SET) ===
for i in range(1, 21):
    idx = f"07_{i:02d}"
    if i == 1:
        c = f"""<path d='M 170,160 L 330,160 L 310,290 L 250,335 L 190,290 Z' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='5'/>
        <line x1='250' y1='160' x2='250' y2='335' stroke='url(#goldGrad)' stroke-width='4'/>
        <line x1='170' y1='245' x2='330' y2='245' stroke='url(#goldGrad)' stroke-width='4'/>
        {wheel(210, 202, 28, 8)}
        <circle cx='290' cy='202' r='14' fill='#000000'/>
        <line x1='210' y1='290' x2='210' y2='265' stroke='url(#steelGrad)' stroke-width='4'/>
        <path d='M 270,285 Q 290,270 310,285' stroke='url(#azureGrad)' stroke-width='4' fill='none'/>
        {crown(250, 115, 0.9)}"""
        t, sub = "Большой Парадный Герб", "Домъ Графа Каретникова"
    elif i == 2:
        c = f"""<path d='M 180,170 L 320,170 L 305,290 L 250,330 L 195,290 Z' fill='url(#darkSlate)' stroke='url(#goldGrad)' stroke-width='4'/>
        {crown(250, 120, 0.8)}
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='36' font-weight='bold' fill='url(#goldGrad)'>ГК</text>"""
        t, sub = "Средний Герб Рода", "Корона о девяти жемчужинахъ"
    elif i == 3:
        c = f"""<path d='M 190,180 L 310,180 L 295,280 L 250,315 L 205,280 Z' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='3'/>
        <line x1='250' y1='180' x2='250' y2='315' stroke='url(#goldGrad)' stroke-width='2'/>
        <line x1='190' y1='247' x2='310' y2='247' stroke='url(#goldGrad)' stroke-width='2'/>
        {crown(250, 140, 0.6)}"""
        t, sub = "Малый Щит Четырех Родов", "Шапка веб-хранилища"
    elif i == 4:
        c = f"""<circle cx='250' cy='240' r='85' fill='url(#azureGrad)' stroke='url(#goldGrad)' stroke-width='4'/>
        <text x='250' y='258' text-anchor='middle' font-family='serif' font-size='60' font-weight='bold' fill='url(#goldGrad)'>ГК</text>
        {crown(250, 130, 0.65)}"""
        t, sub = "Сердцевой Щиток ГК", "Фавиконъ и знакъ аватара"
    elif i == 5:
        c = f"""<ellipse cx='250' cy='240' rx='80' ry='100' fill='url(#darkSlate)' stroke='url(#goldGrad)' stroke-width='4'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='44' font-weight='bold' fill='url(#goldGrad)'>ДИК</text>
        <circle cx='250' cy='240' r='70' fill='none' stroke='url(#goldGrad)' stroke-width='1.5' stroke-dasharray='6,4'/>"""
        t, sub = "Монограмма ДИК", "Дмитрій Ивановичъ Каретниковъ"
    elif i == 6:
        c = f"""<circle cx='250' cy='240' r='100' fill='none' stroke='url(#goldGrad)' stroke-width='6'/>
        <circle cx='250' cy='240' r='85' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='2'/>
        {wheel(250, 240, 50, 8)}
        <text x='250' y='248' text-anchor='middle' font-family='serif' font-size='22' font-weight='bold' fill='#0F172A'>ГК</text>"""
        t, sub = "Sigillum Comitis Karetnikov", "Латинская сургучная печать 42 мм"
    elif i == 7:
        c = f"""<circle cx='250' cy='240' r='100' fill='none' stroke='url(#goldGrad)' stroke-width='6'/>
        <circle cx='250' cy='240' r='85' fill='url(#azureGrad)' stroke='url(#goldGrad)' stroke-width='2'/>
        <text x='250' y='235' text-anchor='middle' font-family='serif' font-size='24' font-weight='bold' fill='url(#goldGrad)'>ПЕЧАТЬ</text>
        <text x='250' y='265' text-anchor='middle' font-family='serif' font-size='16' fill='#FFFFFF'>ДОМА КАРЕТНИКОВЫХЪ</text>"""
        t, sub = "Славянская Родовая Печать", "Грамоты и сертификаты"
    elif i == 8:
        c = f"""<line x1='250' y1='150' x2='250' y2='330' stroke='url(#goldGrad)' stroke-width='12'/>
        <line x1='160' y1='240' x2='340' y2='240' stroke='url(#goldGrad)' stroke-width='12'/>
        <circle cx='250' cy='240' r='30' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='3'/>
        <text x='250' y='247' text-anchor='middle' font-family='serif' font-size='18' font-weight='bold' fill='url(#goldGrad)'>ГК</text>"""
        t, sub = "Крест Четырех Стихий", "Союзъ 4 фамильныхъ клановъ"
    elif i == 9:
        c = f"""{wheel(250, 260, 60, 8)}
        <path d='M 250,220 C 220,160 160,170 150,220 C 180,210 220,220 250,250 Z' fill='url(#steelGrad)' stroke='url(#goldGrad)' stroke-width='2'/>
        <path d='M 250,220 C 280,160 340,170 350,220 C 320,210 280,220 250,250 Z' fill='url(#steelGrad)' stroke='url(#goldGrad)' stroke-width='2'/>"""
        t, sub = "Колесо и Орлиные Крылья", "Отцовская и материнская вершины"
    elif i == 10:
        c = f"""{wheel(250, 290, 45, 8)}
        <path d='M 250,250 C 250,190 200,160 210,140 C 230,160 270,160 290,140 C 300,160 250,190 250,250 Z' fill='url(#goldGrad)'/>"""
        t, sub = "Древо 7 Колен и Колесо", "127 прямыхъ предковъ"
    elif i == 11:
        c = f"""<rect x='160' y='150' width='180' height='180' rx='16' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='5'/>
        {wheel(250, 240, 55, 8)}
        <text x='250' y='248' text-anchor='middle' font-family='serif' font-size='26' font-weight='bold' fill='#0F172A'>ГК</text>"""
        t, sub = "Вензель на Пунцовой Манере", "Люксовый книжный переплетъ"
    elif i == 12:
        c = f"""<path d='M 180,170 L 320,170 L 300,290 L 250,330 L 200,290 Z' fill='url(#steelGrad)' stroke='url(#goldGrad)' stroke-width='4'/>
        <line x1='160' y1='150' x2='340' y2='330' stroke='url(#madderRed)' stroke-width='6'/>
        <line x1='340' y1='150' x2='160' y2='330' stroke='url(#madderRed)' stroke-width='6'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='32' font-weight='bold' fill='#0F172A'>1640–1945</text>"""
        t, sub = "Воинский Щит Памяти", "Ратные подвиги предъковъ"
    elif i == 13:
        c = f"""<polygon points='250,140 340,240 250,330 160,240' fill='url(#darkSlate)' stroke='url(#goldGrad)' stroke-width='5'/>
        {wheel(250, 240, 50, 8)}
        <text x='250' y='247' text-anchor='middle' font-family='serif' font-size='22' font-weight='bold' fill='url(#goldGrad)'>ОРЕЛЪ</text>"""
        t, sub = "Золотое Руно Тейкова и Степи", "Купеческо-степное наслѣдіе"
    elif i == 14:
        c = f"""<polygon points='250,145 320,175 345,240 320,305 250,335 180,305 155,240 180,175' fill='url(#darkSlate)' stroke='url(#goldGrad)' stroke-width='5'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='48' font-weight='bold' fill='url(#goldGrad)'>ГК</text>"""
        t, sub = "Восьмигранный Перстневой Знак", "Лазерная гравировка на металлѣ"
    elif i == 15:
        c = f"""<circle cx='250' cy='240' r='90' fill='url(#darkSlate)' stroke='url(#goldGrad)' stroke-width='5'/>
        <circle cx='250' cy='220' r='18' fill='url(#goldGrad)'/>
        <polygon points='243,225 257,225 262,265 238,265' fill='url(#goldGrad)'/>
        {crown(250, 120, 0.65)}"""
        t, sub = "Хранитель Zero-Knowledge Vault", "Криптографическій щитъ"
    elif i == 16:
        c = f"""<polygon points='250,135 345,240 250,340 155,240' fill='url(#azureGrad)' stroke='url(#goldGrad)' stroke-width='4'/>
        <text x='250' y='230' text-anchor='middle' font-family='serif' font-size='16' font-weight='bold' fill='url(#goldGrad)'>САМАРА • ОРЕНБУРГЪ</text>
        <text x='250' y='265' text-anchor='middle' font-family='serif' font-size='16' font-weight='bold' fill='url(#steelGrad)'>ПЕНЗА • ИВАНОВО</text>"""
        t, sub = "Ромб Четырех Губерний", "Географія родовой колонизаціи"
    elif i == 17:
        c = f"""<circle cx='250' cy='240' r='90' fill='url(#madderRed)' stroke='url(#goldGrad)' stroke-width='4'/>
        <text x='250' y='270' text-anchor='middle' font-family='serif' font-size='90' font-weight='bold' fill='url(#goldGrad)'>К</text>
        {crown(250, 120, 0.75)}"""
        t, sub = "Литера К — Имперский Стиль", "Монументальная классика"
    elif i == 18:
        c = f"""<rect x='160' y='140' width='180' height='200' rx='12' fill='url(#darkSlate)' stroke='url(#goldGrad)' stroke-width='4'/>
        <text x='250' y='210' text-anchor='middle' font-family='serif' font-size='18' font-weight='bold' fill='url(#goldGrad)'>ЧЕСТЬЮ</text>
        <text x='250' y='245' text-anchor='middle' font-family='serif' font-size='18' font-weight='bold' fill='url(#steelGrad)'>ТРУДОМЪ</text>
        <text x='250' y='280' text-anchor='middle' font-family='serif' font-size='18' font-weight='bold' fill='url(#goldGrad)'>СЛУЖЕНІЕМЪ</text>"""
        t, sub = "Экслибрис Летописи Рода", "Девизный книжный картушъ"
    elif i == 19:
        c = f"""<circle cx='250' cy='240' r='80' fill='url(#madderRed)' stroke='#4A0E0E' stroke-width='6' filter='url(#dropShadow)'/>
        <text x='250' y='255' text-anchor='middle' font-family='serif' font-size='50' font-weight='bold' fill='#FFD7A8'>ГК</text>"""
        t, sub = "Сургучная Капля ГК", "Рельефная метка главъ книги"
    else:
        c = f"""<polygon points='250,130 275,200 350,200 290,240 315,310 250,270 185,310 210,240 150,200 225,200' fill='url(#steelGrad)' stroke='url(#goldGrad)' stroke-width='3'/>
        <circle cx='250' cy='240' r='45' fill='url(#azureGrad)' stroke='url(#goldGrad)' stroke-width='2'/>
        <text x='250' y='248' text-anchor='middle' font-family='serif' font-size='16' font-weight='bold' fill='url(#goldGrad)'>1640–2026</text>"""
        t, sub = "Орденская Звезда Рода", "Юбилей 386 лѣтъ служенія"
    base_svg(f"logo_{idx}.svg", t, sub, c)

print("ALL 93 SVG LOGOS GENERATED SUCCESSFULLY!")
