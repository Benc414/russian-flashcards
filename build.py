from pathlib import Path
raw = r'''EVERYDAY PHRASES
	1.	I deal with tasks / Я решаю задачи
	2.	Sometimes I go to meet with different colleagues / Иногда встречаюсь с другими коллегами
	3.	I don’t care / Мне всё равно
	4.	He doesn’t care / Ему всё равно
	5.	Can I? / Is it allowed? / Можно
	6.	Need to / Necessary / Нужно
	7.	You can’t / Not allowed / Нельзя
	8.	How’s life, what’s new? / Как жизнь, что нового?
	9.	Tell me about this / Расскажи мне об этом
	10.	That’s why / Поэтому
	11.	Instead / Вместо
	12.	More than / Больше чем
	13.	Only in a week / Только через неделю
	14.	On the first sight / На первый взгляд
	15.	But in reality / Но на самом деле
	16.	I prefer / Я предпочитаю
	17.	Amazing / Потрясающе
	18.	I met new people / Я встретил новых людей
	19.	I drove to Denver / Я ездил в Денвер
	20.	From 5 to 9 / С пяти до девяти
	21.	Need to move / Надо переехать
	22.	He wants to move but later / Он хочет переехать, но позже
	23.	I went to get a haircut / Я ходил на стрижку
	24.	I am growing my hair / Я отращиваю волосы
	25.	I fell down / Я упал вниз
	26.	I was upside down / Я висел вниз ногами
	27.	I crashed into the wall / Я ударился об стену
	28.	Always / Всегда
	29.	Sometimes / Иногда
	30.	Often / Часто
	31.	Seldom / Редко
	32.	Late / Поздно
	33.	Early / Рано
	34.	Together / Вместе
	35.	Which movie? / Какое кино?
	36.	We ate / Мы ели
	37.	He is not finished / Он не закончен
	38.	Have a good weekend! / Хороших выходных!
	39.	See you soon! / До встречи!
	40.	I have a question / У меня есть вопрос
	41.	Two weeks ago / Две недели назад
	42.	An app / Приложение
GRAMMAR — С (WITH)
43. With me / Со мной
44. With you (informal) / С тобой
45. With him / with it / С ним
46. With her / С ней
47. With you (plural/formal) / С вами
48. With them / С ними
49. With us / С нами
50. With my son / С сыном
WORK & PROFESSIONAL
51. Worker / co-worker / Сотрудник
52. Owner of the company / Владелец компании
53. To pay / Платить
54. Accountant / Бухгалтер
55. Paperwork / Бумажками
56. Risk assessment / Оценивание рисков
57. National project / Национальный проект
58. He will allow us to expand / Он позволит увеличить
59. Military / Военный
60. Fame / popular / Известность
61. To get / Получить
62. Mass media / СМИ
63. Workers / Рабочие
64. Artificial intelligence / Искусственный интеллект
65. Build / Строил
66. Goal / Цель
67. Inspections, investigations, meetings / Инспекции, расследования, совещания
68. Everyday working out / Заниматься спортом
69. We do sport / Занимаемся спортом
SPORTS & HOBBIES
70. Rock climbing / Скалолазание
71. Weightlifting / Тяжёлая атлетика
72. Track and field / Лёгкая атлетика
73. Gymnastics / Гимнастика
74. Gym / Зал
75. Mountain bike / Горный велосипед
76. For health / Для здоровья
77. Outside / На улице
78. Running on treadmill / Беговая дорожка
79. Top of the mountain / Вершина горы
80. Belay / Страховать
81. A rope / Верёвка
82. On ice / На льду
83. Mountain / Гора
84. Small hill / slide / Горка
85. To grieve / Горевать
86. Legendary / Легендарный
87. I prefer rock climbing / Я предпочитаю скалолазание
HEALTH & ILLNESS
88. Symptoms / Симптомы
89. Cough / Кашель
90. Runny nose / Насморк
91. Headache / Головная боль
92. Medicine / Лекарства
93. Tea with ginger / Чай с имбирём
94. To feel / Чувствовать
95. To die / dying / Умереть / умирать
96. Hair salon / Парикмахерская
97. Beets / Свекла
98. Beet salad / Винегрет
99. Windy weather / Ветреная погода
100. Comfortable weather / Комфортная погода
101. Wind / Ветер
102. Last year / Прошлый год
103. The day before / Накануне
104. In a dream / sleep / Во сне
TRAVEL & PLACES
105. To visit / Посещать
106. Ship / Корабль
107. Dominican Republic / Доминиканская Республика
108. Made a stop / Делали остановку
109. Got out / Выходили
110. Near the airport / Недалеко от аэропорта
111. Around all the country / По всей стране
112. Apartment / Квартира
113. Private house / Частный дом
114. In Asia / В Азии
115. Light / Свет
116. To own the world / Владеть миром
117. Belief / Вера
118. Near the Colorado Springs airport / Недалеко от аэропорта Колорадо-Спрингс
SCIENCE & MEDICINE
119. Scientific research / Исследования
120. Dangerous infections / Опасные инфекции
121. To create / Создать
122. Reliable protection / Надёжная защита
123. The most dangerous / Самая опасная
124. Only / Только
125. Lab / Лаборатория
126. Unknown diseases / Неизвестные болезни
127. To appear / Появиться
128. Sanitary / Санитарный
129. Sanitary services frontline / Санитарные службы на передовой
130. Top level / Высший уровень
131. Detecting dangerous viruses / Для обнаружения опасных вирусов
132. Manufacturing vaccines / Изготовление новых вакцин
133. Study / Изучение
134. Biological protection / Биологической безопасности
135. Large scale / Масштабного
136. To isolate / Изолировать
137. Special / Специальный
138. Soldiers / Солдаты
139. Civilians / Гражданские
140. Attack / Атака
FOOD & COOKING
141. To cook / Готовить
142. Meat and fish / Мясо и рыба
143. Pork / Свинина
144. Beef / Говядина
145. Chicken / Курица
146. Veal / Телятина
147. Farmers market / Базар
148. Sandwich / Бутерброд
149. Cold borscht / Холодный борщ
150. Hot tea / Горячий чай
151. To cook food / Готовить еду
152. Give gifts / Дарить подарки
153. Go be a guest / Ходить в гости
154. Christmas lights / Рождественские огни
155. Parents / Родители
HOME & HOUSE
156. Big comfortable house / Большой удобный дом
157. Wooden two-storey house / Деревянный двухэтажный дом
158. Four bedrooms / Четыре спальных комнаты
159. Living room / Гостиная
160. Kitchen / Кухня
161. Bathroom / Ванная
162. Hallway / Прихожая
163. Office / Офис
164. Laundry room / Прачечная
165. Big yard / Большой двор
166. Garden / Сад
167. Pine trees / Сосны
168. Flower bed / Клумба с цветами
169. Sofa / Диван
170. Coffee table / Журнальный столик
171. Carpet / Ковёр
172. Air conditioning / Кондиционер
DAYS, MONTHS & SEASONS
173. Monday / Понедельник
174. Tuesday / Вторник
175. Wednesday / Среда
176. Thursday / Четверг
177. Friday / Пятница
178. Saturday / Суббота
179. Sunday / Воскресенье
180. Weekend / Выходные
181. January / Январь
182. February / Февраль
183. March / Март
184. April / Апрель
185. May / Май
186. June / Июнь
187. July / Июль
188. August / Август
189. September / Сентябрь
190. October / Октябрь
191. November / Ноябрь
192. December / Декабрь
193. Summer / Лето
194. Winter / Зима
195. Spring / Весна
196. Autumn / Fall / Осень
197. In summer / Летом
198. In winter / Зимой
199. In spring / Весной
200. In autumn / Осенью
201. Today / Сегодня
202. Tomorrow / Завтра
203. Yesterday / Вчера
204. In the morning / Утром
205. In the evening / Вечером
206. My birthday / Мой день рождения
207. Her birthday was last Monday / Её день рождения был в прошлый понедельник
COUNTRIES & GEOGRAPHY
208. Country / Страна
209. North / Север
210. South / Юг
211. West / Запад
212. East / Восток
213. Europe / Европа
214. Germany / Германия
215. England / Англия
216. France / Франция
217. Spain / Испания
218. Norway / Норвегия
219. Sweden / Швеция
220. Poland / Польша
221. Ukraine / Украина
222. Greece / Греция
223. Mediterranean Sea / Средиземное море
224. Black Sea / Чёрное море
225. Pacific Ocean / Тихий океан
226. Atlantic Ocean / Атлантический океан
227. I want to visit Iceland / Я хочу поехать в Исландию
228. They are allies / Они союзники
229. Buffet / Шведский стол
230. To adore / Обожать
231. I really liked it / Мне понравилось очень сильно
MOVEMENT VERBS
232. To go on foot (one way) / Идти / я иду
233. To go on foot (regularly) / Ходить / я хожу
234. To go by transport (one way) / Ехать / я еду
235. To go by transport (regularly) / Ездить / я езжу
236. To run (one direction) / Бежать
237. To walk on foot / Ходить пешком
238. To return / Возвращаться
239. To rest / relax / Отдыхать
240. To stroll / walk / Гулять
241. Library / Библиотека
242. Shop / Магазин
243. City centre / Центр города
244. To drive someone / Возить
245. To drop off / Отвозить
246. Night / Ночью
247. To search / I search / Искать / я ищу
248. You search / Ты ищешь
249. He searches / Он ищет'''

categories = {
    'EVERYDAY PHRASES': ('Everyday Phrases','💬','Conversation and useful daily chunks'),
    'GRAMMAR — С (WITH)': ('Grammar: С (with)','🧩','Pronouns and the preposition с'),
    'WORK & PROFESSIONAL': ('Work & Professional','💼','Jobs, work language, and professional vocabulary'),
    'SPORTS & HOBBIES': ('Sports & Hobbies','🏔️','Activities, fitness, and hobbies'),
    'HEALTH & ILLNESS': ('Health & Illness','🩺','Symptoms, health, and wellness'),
    'TRAVEL & PLACES': ('Travel & Places','✈️','Travel, homes, and places'),
    'SCIENCE & MEDICINE': ('Science & Medicine','🧪','Research, medicine, and safety terms'),
    'FOOD & COOKING': ('Food & Cooking','🍲','Food, cooking, and guests'),
    'HOME & HOUSE': ('Home & House','🏡','Rooms, furniture, and home life'),
    'DAYS, MONTHS & SEASONS': ('Days, Months & Seasons','🗓️','Time, dates, and seasons'),
    'COUNTRIES & GEOGRAPHY': ('Countries & Geography','🌍','Places, countries, and geography'),
    'MOVEMENT VERBS': ('Movement Verbs','🚶','Core movement verbs and places'),
}

lines = [ln.strip() for ln in raw.splitlines() if ln.strip()]
current = None
cards=[]
import re, json
for line in lines:
    if not re.match(r'^\d+\.', line):
        current = line
        continue
    m = re.match(r'^(\d+)\.\s*(.+)$', line)
    n = int(m.group(1)); rest = m.group(2)
    parts = [p.strip() for p in rest.split(' / ')]
    ru = parts[-1]
    en = ' / '.join(parts[:-1]) if len(parts) > 1 else parts[0]
    if current not in categories:
        raise ValueError(f'Unknown category {current}')
    cat_name, icon, desc = categories[current]
    cards.append({
        'id': n,
        'category_key': current,
        'category': cat_name,
        'icon': icon,
        'category_desc': desc,
        'english': en,
        'russian': ru,
    })

cards_json = json.dumps(cards, ensure_ascii=False)

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <meta name="theme-color" content="#0f172a" />
  <title>Russian Flashcards V2</title>
  <link rel="manifest" href="manifest.json">
  <style>
    :root {{
      --bg: #07111f;
      --panel: rgba(15, 23, 42, 0.82);
      --panel-2: rgba(30, 41, 59, 0.9);
      --line: rgba(148, 163, 184, 0.18);
      --text: #e5eefc;
      --muted: #9fb0cb;
      --accent: #7c3aed;
      --accent-2: #22c55e;
      --warn: #f59e0b;
      --danger: #ef4444;
      --radius: 22px;
      --shadow: 0 18px 60px rgba(0,0,0,.35);
      --safe-bottom: env(safe-area-inset-bottom, 0px);
    }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; min-height: 100%; background:
      radial-gradient(circle at top left, rgba(124,58,237,.20), transparent 28%),
      radial-gradient(circle at top right, rgba(34,197,94,.15), transparent 22%),
      linear-gradient(180deg, #020617 0%, #07111f 100%); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    body {{ padding: 14px 14px calc(18px + var(--safe-bottom)); }}
    .app {{ max-width: 920px; margin: 0 auto; display: grid; gap: 14px; }}
    .glass {{ background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); }}
    .hero {{ padding: 18px; }}
    .topline {{ display:flex; align-items:center; justify-content:space-between; gap: 10px; flex-wrap: wrap; }}
    h1 {{ font-size: clamp(1.5rem, 3vw, 2.4rem); margin: 0; }}
    .sub {{ color: var(--muted); font-size: .98rem; line-height: 1.45; margin-top: 8px; }}
    .pillrow, .stats {{ display:flex; gap:8px; flex-wrap:wrap; margin-top: 12px; }}
    .pill, button, select, input {{ border-radius: 14px; border: 1px solid var(--line); background: rgba(15,23,42,.78); color: var(--text); }}
    .pill {{ padding: 8px 12px; font-size: .88rem; }}
    .stats .pill strong {{ color: white; }}
    .controls {{ padding: 14px; display:grid; gap: 10px; }}
    .row {{ display:grid; gap:10px; grid-template-columns: 1fr; }}
    @media (min-width: 760px) {{ .row.two {{ grid-template-columns: 1.25fr .9fr; }} .row.three {{ grid-template-columns: repeat(3,1fr); }} }}
    input, select, button {{ width: 100%; padding: 14px 16px; font-size: 16px; }}
    button {{ cursor: pointer; font-weight: 700; }}
    button.primary {{ background: linear-gradient(135deg, rgba(124,58,237,.95), rgba(59,130,246,.95)); border: none; }}
    button.secondary {{ background: rgba(15,23,42,.65); }}
    button.good {{ background: rgba(34,197,94,.14); }}
    button.warn {{ background: rgba(245,158,11,.14); }}
    button.bad {{ background: rgba(239,68,68,.14); }}
    button:active {{ transform: translateY(1px) scale(.997); }}
    .modebar {{ display:grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }}
    .modebar button.active {{ outline: 2px solid rgba(124,58,237,.65); background: rgba(124,58,237,.18); }}
    .cardwrap {{ padding: 14px; }}
    .card {{ position: relative; overflow: hidden; min-height: 430px; display:flex; flex-direction:column; justify-content:space-between; padding: 0; }}
    .heroart {{ padding: 18px; background: linear-gradient(135deg, rgba(124,58,237,.26), rgba(56,189,248,.16)); border-bottom: 1px solid var(--line); }}
    .heroart-top {{ display:flex; justify-content:space-between; align-items:flex-start; gap:12px; }}
    .iconbubble {{ width: 68px; height: 68px; border-radius: 20px; display:grid; place-items:center; font-size: 2rem; background: rgba(255,255,255,.1); border:1px solid rgba(255,255,255,.12); }}
    .cardnum {{ font-size: .9rem; color: var(--muted); }}
    .cat {{ font-size: .84rem; letter-spacing: .08em; text-transform: uppercase; color: #d8c8ff; }}
    .cardbody {{ padding: 18px; display:grid; gap: 14px; }}
    .side {{ padding: 16px; border-radius: 18px; background: rgba(255,255,255,.03); border: 1px solid var(--line); }}
    .label {{ font-size: .8rem; color: var(--muted); text-transform: uppercase; letter-spacing: .08em; margin-bottom: 6px; }}
    .phrase-en {{ font-size: clamp(1.15rem, 3vw, 1.5rem); line-height: 1.35; font-weight: 700; }}
    .phrase-ru {{ font-size: clamp(1.35rem, 3.5vw, 1.85rem); line-height: 1.35; font-weight: 800; }}
    .muted {{ color: var(--muted); }}
    .audioRow, .actionGrid, .navGrid {{ display:grid; gap: 10px; }}
    .audioRow, .navGrid {{ grid-template-columns: repeat(2, 1fr); }}
    .actionGrid {{ grid-template-columns: repeat(3, 1fr); }}
    .feedback {{ min-height: 24px; color: #cbd5e1; font-weight:600; }}
    .hidden {{ display:none !important; }}
    .quizbox {{ padding: 16px; border-radius: 18px; background: rgba(255,255,255,.03); border: 1px solid var(--line); display:grid; gap: 12px; }}
    .options {{ display:grid; gap:10px; }}
    .options button {{ text-align:left; font-weight:600; }}
    .footerNote {{ text-align:center; color: var(--muted); font-size: .87rem; padding: 8px 10px 2px; }}
    .tiny {{ font-size:.82rem; color:var(--muted); }}
  </style>
</head>
<body>
  <div class="app">
    <section class="glass hero">
      <div class="topline">
        <div>
          <h1>Russian Flashcards V2</h1>
          <div class="sub">Mobile-first, smoother on phones, and less cursed than the first round. Study mode, quiz mode, streaks, progress memory, category art, and tap-to-speak built in.</div>
        </div>
        <div class="pill">249 cards</div>
      </div>
      <div class="stats">
        <div class="pill">Seen: <strong id="seenCount">0</strong></div>
        <div class="pill">Mastered: <strong id="masteredCount">0</strong></div>
        <div class="pill">Hard: <strong id="hardCount">0</strong></div>
        <div class="pill">Streak: <strong id="streakCount">0</strong></div>
      </div>
    </section>

    <section class="glass controls">
      <div class="modebar">
        <button id="modeStudy" class="active">Study</button>
        <button id="modeQuiz">Quiz</button>
        <button id="modeReview">Review Hard</button>
      </div>
      <div class="row two">
        <input id="searchInput" type="search" placeholder="Search English or Russian" autocomplete="off" />
        <select id="categorySelect"></select>
      </div>
      <div class="row three">
        <button id="shuffleBtn" class="secondary">Shuffle</button>
        <button id="resetFiltersBtn" class="secondary">Reset filters</button>
        <button id="resetProgressBtn" class="bad">Reset progress</button>
      </div>
      <div class="tiny">Best experience: host this folder on Vercel, Netlify, or GitHub Pages. Local mobile files can still be weird because iPhone likes drama.</div>
    </section>

    <section class="glass cardwrap">
      <div id="studyCard" class="card glass">
        <div class="heroart">
          <div class="heroart-top">
            <div>
              <div class="cat" id="cardCategory">Category</div>
              <div class="sub" id="cardCategoryDesc">Description</div>
            </div>
            <div class="iconbubble" id="cardIcon">💬</div>
          </div>
        </div>
        <div class="cardbody">
          <div class="cardnum" id="cardNumber">Card 1 of 249</div>
          <div class="side">
            <div class="label">English</div>
            <div class="phrase-en" id="englishText"></div>
          </div>
          <div class="side">
            <div class="label">Russian</div>
            <div class="phrase-ru" id="russianText"></div>
          </div>
          <div class="audioRow">
            <button id="speakEnBtn" class="secondary">🔊 English</button>
            <button id="speakRuBtn" class="secondary">🔊 Russian</button>
          </div>
          <div class="actionGrid">
            <button id="markSeenBtn" class="secondary">Seen</button>
            <button id="markHardBtn" class="warn">Hard</button>
            <button id="markMasteredBtn" class="good">Mastered</button>
          </div>
          <div class="navGrid">
            <button id="prevBtn" class="secondary">← Prev</button>
            <button id="nextBtn" class="primary">Next →</button>
          </div>
        </div>
      </div>

      <div id="quizCard" class="card glass hidden">
        <div class="heroart">
          <div class="heroart-top">
            <div>
              <div class="cat">Quiz mode</div>
              <div class="sub">Pick the correct translation. Fast reps beat fake motivation.</div>
            </div>
            <div class="iconbubble">🧠</div>
          </div>
        </div>
        <div class="cardbody">
          <div class="quizbox">
            <div class="label">Prompt</div>
            <div class="phrase-en" id="quizPrompt"></div>
            <div class="muted" id="quizDirection">Choose the Russian translation</div>
          </div>
          <div class="options" id="quizOptions"></div>
          <div class="feedback" id="quizFeedback"></div>
          <div class="navGrid">
            <button id="quizSkipBtn" class="secondary">Skip</button>
            <button id="quizNextBtn" class="primary">New question</button>
          </div>
        </div>
      </div>
    </section>

    <div class="footerNote">Offline-friendly static site. Audio uses your device voice engine, so pronunciation quality depends on the browser and installed voices.</div>
  </div>

<script>
const cards = {cards_json};
const STORAGE_KEY = 'russian-flashcards-v2-progress';
const todayKey = () => new Date().toISOString().slice(0,10);
const state = {{
  mode: 'study',
  cards: cards,
  filtered: [...cards],
  idx: 0,
  category: 'all',
  search: '',
  progress: loadProgress(),
  quiz: null,
}};

function loadProgress() {{
  try {{
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : {{ seen: {{}}, hard: {{}}, mastered: {{}}, quizCorrect: 0, streakDays: [], lastActive: null }};
  }} catch {{
    return {{ seen: {{}}, hard: {{}}, mastered: {{}}, quizCorrect: 0, streakDays: [], lastActive: null }};
  }}
}}
function saveProgress() {{
  stampActiveDay();
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state.progress));
  updateStats();
}}
function stampActiveDay() {{
  const tk = todayKey();
  const arr = new Set(state.progress.streakDays || []);
  arr.add(tk);
  state.progress.streakDays = Array.from(arr).sort();
  state.progress.lastActive = tk;
}}
function calculateStreak() {{
  const days = (state.progress.streakDays || []).slice().sort();
  if (!days.length) return 0;
  const set = new Set(days);
  let streak = 0;
  let d = new Date();
  for (;;) {{
    const key = d.toISOString().slice(0,10);
    if (set.has(key)) {{ streak++; d.setDate(d.getDate()-1); }} else {{
      if (streak === 0) {{ d.setDate(d.getDate()-1); if (set.has(d.toISOString().slice(0,10))) {{ streak++; d.setDate(d.getDate()-1); continue; }} }}
      break;
    }}
  }}
  return streak;
}}
function updateStats() {{
  document.getElementById('seenCount').textContent = Object.keys(state.progress.seen || {{}}).length;
  document.getElementById('masteredCount').textContent = Object.keys(state.progress.mastered || {{}}).length;
  document.getElementById('hardCount').textContent = Object.keys(state.progress.hard || {{}}).length;
  document.getElementById('streakCount').textContent = calculateStreak();
}}
function uniqueCategories() {{
  const map = new Map();
  cards.forEach(c => {{ if (!map.has(c.category)) map.set(c.category, c); }});
  return Array.from(map.values());
}}
function populateCategories() {{
  const select = document.getElementById('categorySelect');
  select.innerHTML = '<option value="all">All categories</option>' + uniqueCategories().map(c => `<option value="${{escapeHtml(c.category)}}">${{escapeHtml(c.icon)}} ${{escapeHtml(c.category)}}</option>`).join('');
}}
function escapeHtml(s) {{ return String(s).replace(/[&<>"']/g, ch => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[ch])); }}
function applyFilters() {{
  const q = state.search.trim().toLowerCase();
  state.filtered = state.cards.filter(c => {{
    const matchesCategory = state.category === 'all' || c.category === state.category;
    const matchesSearch = !q || c.english.toLowerCase().includes(q) || c.russian.toLowerCase().includes(q);
    const matchesMode = state.mode !== 'review' || state.progress.hard[c.id];
    return matchesCategory && matchesSearch && matchesMode;
  }});
  if (!state.filtered.length) state.idx = 0; else if (state.idx >= state.filtered.length) state.idx = 0;
  render();
}}
function currentCard() {{ return state.filtered[state.idx] || null; }}
function render() {{
  updateStats();
  document.getElementById('modeStudy').classList.toggle('active', state.mode==='study');
  document.getElementById('modeQuiz').classList.toggle('active', state.mode==='quiz');
  document.getElementById('modeReview').classList.toggle('active', state.mode==='review');
  document.getElementById('studyCard').classList.toggle('hidden', state.mode==='quiz');
  document.getElementById('quizCard').classList.toggle('hidden', state.mode!=='quiz');
  if (state.mode === 'quiz') {{
    renderQuiz();
    return;
  }}
  const card = currentCard();
  const empty = !card;
  document.getElementById('englishText').textContent = empty ? 'No cards match your filter.' : card.english;
  document.getElementById('russianText').textContent = empty ? 'Try a different search or category.' : card.russian;
  document.getElementById('cardNumber').textContent = empty ? '0 cards found' : `Card ${{state.idx+1}} of ${{state.filtered.length}} · #${{card.id}}`;
  document.getElementById('cardCategory').textContent = empty ? 'Nothing here' : card.category;
  document.getElementById('cardCategoryDesc').textContent = empty ? 'Reset filters and try again.' : card.category_desc;
  document.getElementById('cardIcon').textContent = empty ? '🫠' : card.icon;
}}
function mark(type) {{
  const c = currentCard();
  if (!c) return;
  state.progress[type][c.id] = true;
  if (type === 'mastered') delete state.progress.hard[c.id];
  saveProgress();
}}
function unmark(type,id) {{ delete state.progress[type][id]; saveProgress(); }}
function shuffleFiltered() {{
  for (let i = state.filtered.length - 1; i > 0; i--) {{
    const j = Math.floor(Math.random() * (i + 1));
    [state.filtered[i], state.filtered[j]] = [state.filtered[j], state.filtered[i]];
  }}
  state.idx = 0;
  render();
}}
function nextCard() {{ if (!state.filtered.length) return; state.idx = (state.idx + 1) % state.filtered.length; mark('seen'); render(); }}
function prevCard() {{ if (!state.filtered.length) return; state.idx = (state.idx - 1 + state.filtered.length) % state.filtered.length; render(); }}
function getVoices() {{ return speechSynthesis.getVoices(); }}
function speak(text, lang) {{
  if (!('speechSynthesis' in window)) return alert('Speech is not supported in this browser.');
  speechSynthesis.cancel();
  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = lang;
  const voices = getVoices();
  const preferred = voices.find(v => v.lang.toLowerCase().startsWith(lang.toLowerCase().split('-')[0]));
  if (preferred) utter.voice = preferred;
  utter.rate = lang.startsWith('ru') ? 0.9 : 0.98;
  speechSynthesis.speak(utter);
}}
function makeQuiz() {{
  const pool = state.filtered.length ? state.filtered : state.cards;
  const card = pool[Math.floor(Math.random() * pool.length)];
  const askRussian = Math.random() < 0.5;
  const prompt = askRussian ? card.russian : card.english;
  const correct = askRussian ? card.english : card.russian;
  const field = askRussian ? 'english' : 'russian';
  const distractors = pool.filter(c => c.id !== card.id).sort(() => Math.random() - 0.5).slice(0,3).map(c => c[field]);
  const options = [correct, ...distractors].sort(() => Math.random() - 0.5);
  state.quiz = {{ card, askRussian, prompt, correct, options, answered: false }};
}}
function renderQuiz() {{
  if (!state.quiz) makeQuiz();
  const q = state.quiz;
  document.getElementById('quizPrompt').textContent = q.prompt;
  document.getElementById('quizDirection').textContent = q.askRussian ? 'Choose the English translation' : 'Choose the Russian translation';
  const box = document.getElementById('quizOptions');
  box.innerHTML = '';
  q.options.forEach(opt => {{
    const btn = document.createElement('button');
    btn.className = 'secondary';
    btn.textContent = opt;
    btn.onclick = () => answerQuiz(opt, btn);
    box.appendChild(btn);
  }});
  document.getElementById('quizFeedback').textContent = '';
}}
function answerQuiz(opt, btn) {{
  const q = state.quiz;
  if (!q || q.answered) return;
  q.answered = true;
  mark('seen');
  if (opt === q.correct) {{
    btn.className = 'good';
    document.getElementById('quizFeedback').textContent = `Correct. #${{q.card.id}}`; 
    state.progress.quizCorrect = (state.progress.quizCorrect || 0) + 1;
    mark('mastered');
  }} else {{
    btn.className = 'bad';
    document.getElementById('quizFeedback').textContent = `Nope. Correct answer: ${{q.correct}}`;
    mark('hard');
    Array.from(document.getElementById('quizOptions').children).forEach(el => {{ if (el.textContent === q.correct) el.className = 'good'; }});
  }}
  saveProgress();
}}

populateCategories();
updateStats();
applyFilters();

const byId = id => document.getElementById(id);
byId('searchInput').addEventListener('input', e => {{ state.search = e.target.value; applyFilters(); }});
byId('categorySelect').addEventListener('change', e => {{ state.category = e.target.value; applyFilters(); }});
byId('shuffleBtn').onclick = shuffleFiltered;
byId('resetFiltersBtn').onclick = () => {{ state.search=''; state.category='all'; byId('searchInput').value=''; byId('categorySelect').value='all'; applyFilters(); }};
byId('resetProgressBtn').onclick = () => {{ if (confirm('Reset all saved progress?')) {{ localStorage.removeItem(STORAGE_KEY); state.progress = loadProgress(); applyFilters(); }} }};
byId('modeStudy').onclick = () => {{ state.mode='study'; applyFilters(); }};
byId('modeQuiz').onclick = () => {{ state.mode='quiz'; state.quiz=null; render(); }};
byId('modeReview').onclick = () => {{ state.mode='review'; applyFilters(); }};
byId('nextBtn').onclick = nextCard;
byId('prevBtn').onclick = prevCard;
byId('markSeenBtn').onclick = () => mark('seen');
byId('markHardBtn').onclick = () => mark('hard');
byId('markMasteredBtn').onclick = () => mark('mastered');
byId('speakEnBtn').onclick = () => {{ const c=currentCard(); if (c) speak(c.english,'en-US'); }};
byId('speakRuBtn').onclick = () => {{ const c=currentCard(); if (c) speak(c.russian,'ru-RU'); }};
byId('quizNextBtn').onclick = () => {{ state.quiz = null; renderQuiz(); }};
byId('quizSkipBtn').onclick = () => {{ state.quiz = null; renderQuiz(); }};
window.addEventListener('keydown', e => {{
  if (state.mode === 'quiz') return;
  if (e.key === 'ArrowRight') nextCard();
  if (e.key === 'ArrowLeft') prevCard();
}});
if ('speechSynthesis' in window) speechSynthesis.onvoiceschanged = () => {{}};
</script>
</body>
</html>'''

manifest = '''{
  "name": "Russian Flashcards V2",
  "short_name": "RuCards V2",
  "start_url": "./index.html",
  "display": "standalone",
  "background_color": "#07111f",
  "theme_color": "#0f172a",
  "icons": [
    {
      "src": "icon.svg",
      "sizes": "any",
      "type": "image/svg+xml",
      "purpose": "any"
    }
  ]
}'''

icon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
<stop offset="0%" stop-color="#7c3aed"/>
<stop offset="100%" stop-color="#22c55e"/>
</linearGradient>
</defs>
<rect width="512" height="512" rx="96" fill="#07111f"/>
<rect x="44" y="44" width="424" height="424" rx="72" fill="url(#g)" opacity="0.22"/>
<rect x="96" y="112" width="320" height="224" rx="36" fill="#e5eefc" opacity="0.94"/>
<rect x="122" y="146" width="130" height="26" rx="13" fill="#7c3aed"/>
<rect x="122" y="192" width="212" height="22" rx="11" fill="#94a3b8"/>
<rect x="122" y="234" width="160" height="22" rx="11" fill="#94a3b8"/>
<circle cx="365" cy="369" r="52" fill="#22c55e"/>
<path d="M340 369l18 18 34-42" fill="none" stroke="#07111f" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

readme = '''# Russian Flashcards V2

## What this is
A mobile-first static flashcard site built from your 249 Russian study cards.

## Features
- Study mode
- Quiz mode
- Review Hard mode
- Search and category filters
- Saved progress with localStorage
- Tap-to-speak English and Russian
- PWA manifest for easy install when hosted

## Best way to use on phone
Host this folder online using one of these:
- Vercel
- Netlify Drop
- GitHub Pages

Then open the live URL on your phone.

## Local file warning
iPhone can behave badly with local HTML files from the Files app. That is an iOS limitation, not a broken site.
'''

p = Path('/mnt/data/russian_flashcards_v2')
(p/'index.html').write_text(html, encoding='utf-8')
(p/'manifest.json').write_text(manifest, encoding='utf-8')
(p/'icon.svg').write_text(icon, encoding='utf-8')
(p/'README.txt').write_text(readme, encoding='utf-8')
print(f'wrote {len(cards)} cards')
