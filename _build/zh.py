"""
Chinese (Simplified, Singapore) pages: /zh/, /zh/emergency-locksmith/ and the ZH_PAGES at the bottom
Targets searches such as 锁匠, 开锁, 新加坡锁匠, 紧急开锁.

FILL: a native Chinese speaker must review all text on these pages before launch.
"""

ZH_NAMES = {
    "emergency-locksmith/": "紧急开锁",
    "digital-lock-opening/": "电子锁、智能锁开锁",
    "digital-lock-installation/": "电子锁安装",
    "safe-opening/": "保险箱开锁",
    "car-locksmith/": "汽车开锁、车钥匙复制",
    "lock-replacement/": "换锁（门锁 / 铁门锁）",
    "letterbox-lock-replacement/": "信箱锁更换",
    "commercial-locksmith/": "商业锁匠（办公室 / 店铺）",
}

ZH_PRICES = [
    ("组屋 / 办公室开锁（上午9点至傍晚6点）", "zh/emergency-locksmith/", "S$80 起"),
    ("非办公时间、周末及公共假期开锁", "zh/emergency-locksmith/", "S$120 起"),
    ("电子锁紧急开锁（所有品牌）", "digital-lock-opening/", "S$150 起"),
    ("电子锁安装（人工费）", "digital-lock-installation/", "S$120 起"),
    ("汽车开锁（无损开锁）", "car-locksmith/", "S$100 起"),
    ("大门 / 铁门换锁（含锁及安装）", "lock-replacement/", "S$100 起"),
    ("信箱锁更换", "letterbox-lock-replacement/", "S$60 起"),
    ("保险箱开锁", "safe-opening/", "按情况报价"),
]

REVIEW_NOTE = "<!-- FILL: 中文内容须由母语人士审核后才正式上线 (a native Chinese speaker must review this page before launch). -->"

ID_ZH = "为了您的安全，我们在开任何门、车或保险箱之前，都会先核对居住或拥有证明，例如附有地址的身份证、租约、水电账单或车辆登记文件。"
WARRANTY_ZH = "所有换锁及安装工作均享有保修，且保修没有期限。"


def price_table():
    rows = "".join(f'<tr><td><a href="~/{("zh/" + p) if p in ZH_PAGES else p}">{label}</a></td><td>{v}</td></tr>' for label, p, v in ZH_PRICES)
    return ('<div class="price-wrap"><table class="price-table"><thead><tr><th scope="col">服务</th><th scope="col">价格</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>')


HOME_FAQS = [
    ("你们真的24小时服务吗？", "是的。Uncle Thomas Locksmith 全年无休，每天24小时提供服务，包括周末和公共假期，覆盖新加坡全岛。"),
    ("开锁要多少钱？", "白天（上午9点至傍晚6点）开锁 S$80 起，非办公时间、周末及公共假期 S$120 起。电子锁开锁 S$150 起，汽车开锁 S$100 起。开工前一定先确认价格。"),
    ("开门前会核对身份吗？", "会。" + ID_ZH),
    ("会不会弄坏我的门？", "我们尽可能使用无损方法开锁，大多数情况下不会损坏门锁。如果无法无损开锁，会先向您说明方案和价格，经您同意才进行。"),
    ("你们配钥匙或修锁吗？", "不提供配钥匙和修锁服务，唯一例外是汽车遥控钥匙（车钥匙）复制。我们专门开门锁、电子锁/智能锁、保险箱和汽车，以及换锁和安装新锁。坏掉的锁我们会直接更换，而不是修理。"),
]

EMERGENCY_FAQS = [
    ("锁匠多久能到？", "接到电话我们立即出发，全天24小时。到达时间视您的位置和交通而定，我们会在电话中给您一个诚实的预计时间。"),
    ("开门前需要出示什么证明？", "需要证明您住在那里，例如附有地址的身份证、租约或水电账单。如果证件在屋内，请告诉我们，开门后可以当面核对。"),
    ("晚上开锁会贵一些吗？", "白天（上午9点至傍晚6点）开锁 S$80 起，非办公时间、周末及公共假期 S$120 起。开工前一定先确认价格。"),
    ("租客可以叫锁匠开门吗？", "可以，只要能证明您住在那里，例如出示租约或寄到该地址、写有您名字的信件。"),
]


def build(x):
    C = x["C"]
    cta, band, faq_html = x["cta_buttons"], x["cta_band"], x["faq_html"]

    zh_has = set(ZH_PAGES) | {"emergency-locksmith/"}
    svc_cards = "".join(
        (f'<a class="card" href="~/zh/{p}"><h3>{n}</h3><span class="more">了解更多 →</span></a>' if p in zh_has else
         f'<a class="card" href="~/{p}"><h3>{n}</h3><span class="more">了解更多（英文）→</span></a>')
        for p, n in ZH_NAMES.items())

    # ------------------------------------------------------------ /zh/
    title = "新加坡锁匠 24小时开锁 | 紧急开锁 S$80起 | Uncle Thomas"
    desc = ("被锁在门外？Uncle Thomas 自1998年起提供新加坡24小时紧急开锁服务：组屋、公寓、电子锁、保险箱和汽车开锁，"
            "全岛服务，S$80起。电话 9224 9224。")
    body = f"""{REVIEW_NOTE}
<section class="hero">
  <div class="container hero-inner">
    <div>
      <p class="eyebrow">新加坡锁匠"师傅" · 自{C.FOUNDED}年</p>
      <h1>新加坡24小时锁匠 — 被锁在门外？<span class="hl">Uncle Thomas</span> 马上到</h1>
      <p class="hero-sub">紧急开锁、电子锁、保险箱和汽车开锁 — 尽可能无损开锁，覆盖新加坡全岛。开工前先报价，<strong>S$80 起</strong>。</p>
      {cta(lang="zh")}
      <ul class="badges"><li>24小时，包括公共假期</li><li>全岛服务</li><li>美国受训保险箱技师</li><li>核对身份</li><li>保修无期限</li></ul>
    </div>
    <div class="hero-art"><picture><source srcset="~/assets/img/logo-320.webp 320w, ~/assets/img/logo-640.webp 640w" sizes="340px" type="image/webp">
      <img src="~/assets/img/logo-640.jpg" alt="Uncle Thomas 锁匠吉祥物手拿钥匙" width="340" height="340" fetchpriority="high"></picture></div>
  </div>
</section>

<section class="trust" aria-label="重点">
  <div class="container trust-inner">
    <div class="trust-item"><strong>自{C.FOUNDED}年</strong><span>{C.YEARS}年以上经验</span></div>
    <div class="trust-item"><strong>24小时</strong><span>夜间、周末、公共假期</span></div>
    <div class="trust-item"><strong>全岛服务</strong><span>新加坡每个地区</span></div>
    <div class="trust-item"><strong>S$80 起</strong><span>开工前先确认价格</span></div>
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <h2 class="section-title">我们的开锁服务</h2>
    <p class="section-lead">组屋、公寓、有地住宅、办公室和店铺 — 门锁、电子锁、保险箱和汽车。</p>
    <div class="grid g4">{svc_cards}</div>
    <p class="note">我们专门开锁、换锁和安装新锁，<strong>不</strong>提供配钥匙或修锁服务（汽车遥控钥匙复制除外）。</p>
  </div>
</section>

<section class="section section-alt" id="how">
  <div class="container">
    <h2 class="section-title">服务流程</h2>
    <p class="section-lead">没有意外收费 — 只有准时到达、帮您开门的锁匠。</p>
    <div class="grid g4 steps">
      <div class="card step"><h3>致电或 WhatsApp</h3><p>致电 {C.PHONE}，或用 WhatsApp 发送锁的照片和您的位置。</p></div>
      <div class="card step"><h3>先报价</h3><p>出发前先告诉您价格。</p></div>
      <div class="card step"><h3>立即出发</h3><p>Uncle Thomas 或他的团队马上出发，24小时服务。</p></div>
      <div class="card step"><h3>核对身份后开锁</h3><p>确认是您的住所、车辆或保险箱后，尽可能无损开锁。</p></div>
    </div>
  </div>
</section>

<section class="section" id="pricing">
  <div class="container narrow">
    <h2 class="section-title">开锁价格</h2>
    <p class="section-lead">清楚的起价，开工前确认最终价格。</p>
    {price_table()}
    <p class="price-foot">价格视锁的种类和地点而定。WhatsApp 锁的照片至 {C.PHONE} 即可获得准确报价。</p>
  </div>
</section>

<section class="section shifu" id="shifu">
  <div class="container">
    <h2 class="section-title">由新加坡锁匠"师傅"带领</h2>
    <p class="section-lead">Uncle Thomas 于{C.FOUNDED}年跟随舅舅当学徒入行。如今，同行都称他为"师傅" — 遇到难题时大家都会找他。</p>
    <div class="shifu-grid">
      <div class="shifu-item"><strong>自{C.FOUNDED}年</strong><p>以传统方式学艺，一把锁、一扇门慢慢累积经验。</p></div>
      <div class="shifu-item"><strong>美国受训保险箱技师</strong><p>曾在美国接受一年保险箱开锁专业训练。</p></div>
      <div class="shifu-item"><strong>船上与海外经验</strong><p>曾在船只和邮轮上，以及泰国、马来西亚、中国和香港为客户开保险箱。</p></div>
      <div class="shifu-item"><strong>电子锁专家</strong><p>自创无损开启故障电子锁的方法。</p></div>
    </div>
    <div class="cta-row center"><a href="~/about/" class="btn btn-light">阅读 Uncle Thomas 的故事（英文）</a></div>
  </div>
</section>

<section class="section" id="faq">
  <div class="container narrow">{faq_html(HOME_FAQS, "常见问题")}</div>
</section>
{band(lang="zh")}
"""
    crumbs = [("首页", "zh/")]
    nodes = x["page_schema"]("zh/", title, desc, crumbs, faqs=HOME_FAQS, lang="zh-SG")
    nodes[0]["inLanguage"] = "zh-SG"
    x["render"]("zh/", title, desc, body, nodes, priority="0.8", lang="zh",
                alternates={"en-SG": "", "zh-SG": "zh/"})

    # ------------------------------------------------------------ /zh/emergency-locksmith/
    path = "zh/emergency-locksmith/"
    title = "紧急开锁 新加坡24小时 | 组屋公寓开锁 S$80起 | Uncle Thomas"
    desc = ("被锁在门外？Uncle Thomas 提供新加坡24小时紧急开锁服务，组屋、公寓、有地住宅和办公室，尽可能无损开锁。"
            "S$80起，电话 9224 9224。")
    crumbs = [("首页", "zh/"), ("紧急开锁", path)]
    body = (REVIEW_NOTE + x["page_hero"](crumbs, "新加坡24小时紧急开锁",
            "被锁在门外？无论白天黑夜、周末或公共假期，请致电 Uncle Thomas。接到电话立即出发，尽可能无损开锁。",
            ["白天 S$80 起", "24小时全岛服务", "核对身份，保障安全"], lang="zh") +
            f'''<section class="section"><div class="container narrow prose">
<h2>被锁在门外？致电后的流程</h2>
<ol>
<li><strong>致电或 WhatsApp {C.PHONE}。</strong>告诉我们您的地址和锁的种类。用 WhatsApp 发送锁的照片，能帮助我们带对工具。</li>
<li><strong>先报价。</strong>出发前先告诉您价格，到门口不会有意外收费。</li>
<li><strong>立即出发。</strong>Uncle Thomas 或他的团队马上前往新加坡任何地点。</li>
<li><strong>核对身份后开锁。</strong>确认您住在那里后，尽可能用无损方法开锁。</li>
</ol>

<h2>我们每天处理的开锁情况</h2>
<ul>
<li><strong>组屋</strong> — 大门、铁门、房门，以及从里面反锁的厕所门。</li>
<li><strong>公寓</strong> — 大门、门闩和电子锁。</li>
<li><strong>有地住宅</strong> — 大门、铁门和后门。</li>
<li><strong>办公室和店铺</strong> — 办公室门、玻璃门、柜子和铁卷门。</li>
<li><strong>电子锁或智能锁打不开？</strong>电池没电、忘记密码或键盘故障 — 请看<a href="~/zh/digital-lock-opening/">电子锁、智能锁开锁</a>。</li>
<li><strong>钥匙锁在车里？</strong>请看<a href="~/zh/car-locksmith/">汽车开锁</a>。</li>
</ul>

<h2>无损开锁优先</h2>
<p>Uncle Thomas 入行{C.YEARS}年以上，大多数机械锁和电子锁都能在不钻孔、不撬门的情况下打开。如果锁已严重磨损或损坏，无法无损打开，我们会<em>先</em>向您说明方案和价格。如果需要换锁，可以当场<a href="~/zh/lock-replacement/">更换</a>，{WARRANTY_ZH}</p>

<div class="callout"><p><strong>为什么要核对身份：</strong>{ID_ZH}这是为了保护您 — 不核对身份就随便开门的锁匠，对大家都是风险。</p></div>

<h2>新加坡紧急开锁要多少钱？</h2>
<p>上午9点至傍晚6点开锁 <strong>S$80 起</strong>，非办公时间、周末及公共假期 <strong>S$120 起</strong>。最终价格视锁的种类以及是否需要更换零件而定，开工前一定先和您确认。完整价格请看<a href="~/zh/#pricing">价格表</a>。</p>

<h2>全岛服务，24小时</h2>
<p>我们服务新加坡每个地区，从兀兰到淡滨尼、从裕廊到大巴窑。请看<a href="~/areas/">服务地区</a>（英文）。</p>

<h2>等待时可以做什么</h2>
<ul>
<li>如果安全，请留在门口附近，方便锁匠找到您。</li>
<li>保持手机有电。</li>
<li>准备好能证明住址的文件。</li>
<li>请不要强行撬门 — 这往往会把简单的开锁变成需要换锁。</li>
<li>如果屋内有小孩、老人或病人可能有危险，请先拨打 995。</li>
</ul>
</div></section>
<section class="section section-alt"><div class="container narrow">{faq_html(EMERGENCY_FAQS, "常见问题")}</div></section>''' +
            band(lang="zh"))
    svc = {"@type": "Service", "@id": C.SITE + "/" + path + "#service", "name": "紧急开锁 — 新加坡",
           "serviceType": "Emergency locksmith", "description": desc, "provider": {"@id": x["BUSINESS_ID"]},
           "areaServed": {"@type": "Country", "name": "Singapore"}, "url": C.SITE + "/" + path, "inLanguage": "zh-SG",
           "offers": {"@type": "Offer", "priceCurrency": "SGD",
                      "priceSpecification": {"@type": "PriceSpecification", "minPrice": 80, "priceCurrency": "SGD"}}}
    nodes = x["page_schema"](path, title, desc, crumbs, faqs=EMERGENCY_FAQS, extra=[svc], lang="zh-SG")
    x["render"](path, title, desc, body, nodes, priority="0.7", lang="zh",
                alternates={"en-SG": "emergency-locksmith/", "zh-SG": path})


# ------------------------------------------------------------------ more Chinese service pages
# FILL: native Chinese speaker review. Added 27 Oct 2026.
ZH_PAGES = {
"digital-lock-opening/": dict(
 title="电子锁开锁 智能锁开锁 新加坡24小时 | 所有品牌 S$150起",
 desc="电子锁或智能锁打不开？电池没电、忘记密码、键盘故障或App离线，Uncle Thomas 24小时为您开锁，所有品牌，S$150起。电话 9224 9224。",
 h1="电子锁、智能锁打不开？24小时开锁",
 sub="电池没电、忘记密码、指纹不认、键盘不亮或智能锁App连不上 — Uncle Thomas 自创无损开启故障电子锁和智能锁的方法，所有品牌都能开。",
 badges=["所有品牌", "S$150 起", "24小时全岛"],
 body="""
<h2>常见的电子锁和智能锁问题</h2>
<ul>
<li><strong>电池没电</strong>，紧急供电也没用。</li>
<li><strong>忘记密码</strong>或指纹认不出来。</li>
<li><strong>键盘不亮或没反应</strong> — 常见于下雨或走廊冲洗之后。</li>
<li><strong>密码正确但锁打不开</strong>，马达不转。</li>
<li><strong>智能锁App离线</strong>，或手机锁在屋里。</li>
<li><strong>后备钥匙不见了。</strong></li>
</ul>
<h2>所有品牌都能开</h2>
<p>包括 Samsung、Yale、Philips、Igloohome、Kaadas、Solity、Gateman、Häfele、Aqara、小米（Xiaomi）、联想（Lenovo）等。组屋、公寓、有地住宅和办公室的大门锁、铁门锁都可以。</p>
<h2>我们不修锁</h2>
<p>我们先帮您开锁。如果锁已经坏了，可以当场为您<a href="~/zh/lock-replacement/">换新锁</a>，{WARRANTY}</p>
<h2>价格</h2>
<p>电子锁、智能锁紧急开锁 <strong>S$150 起</strong>，视品牌、型号和故障而定。WhatsApp 锁的照片（正面和里面）至 {PHONE}，出发前先给您确定价格。</p>
<div class="callout"><p><strong>安全第一：</strong>{ID}</p></div>
""",
 faqs=[("你们能开哪些品牌的电子锁？", "所有品牌，包括 Samsung、Yale、Philips、Igloohome、Kaadas、Solity、Gateman、Häfele、Aqara、小米和联想等。"),
       ("电子锁和智能锁有什么不同？", "智能锁就是可以连接App、Wi-Fi或智能家居的电子锁。两者都靠电池，被锁在门外的情况也一样，我们都能开。"),
       ("开电子锁会弄坏锁吗？", "大多数情况下不会。Uncle Thomas 有自己的无损开锁方法。如果锁完全坏了，我们会先说明方案和价格。"),
       ("电子锁开锁要多少钱？", "S$150 起。WhatsApp 锁的照片给我们，出发前先确定价格。")],
 svc="Digital lock and smart lock opening", minp=150),
"safe-opening/": dict(
 title="保险箱开锁 新加坡 | 美国受训保险箱技师 | Uncle Thomas",
 desc="忘记保险箱密码或钥匙不见了？Uncle Thomas 是在美国受训的保险箱技师，密码锁、电子密码锁、旧式保险箱都能开。电话 9224 9224。",
 h1="新加坡保险箱开锁 — 美国受训保险箱技师",
 sub="忘记密码、钥匙不见、电池没电或保险箱卡住 — Uncle Thomas 曾在美国接受保险箱专业训练，为跨国公司、船只和海外客户开过保险箱。",
 badges=["美国受训", "家用与商用保险箱", "低调处理"],
 body="""
<h2>我们能开的保险箱</h2>
<ul>
<li><strong>家用保险箱</strong> — 电子密码、钥匙和机械密码转盘。</li>
<li><strong>酒店式、衣柜保险箱。</strong></li>
<li><strong>办公室和商用保险箱</strong> — 现金箱、文件保险柜。</li>
<li><strong>旧式机械密码保险箱</strong>、保险库门和门闩。</li>
<li><strong>船上的保险箱。</strong></li>
</ul>
<h2>保险箱品牌</h2>
<p>所有品牌，包括 Bumil、Chubb、Glory、Uchida、Eagle、Phoenix、Sentry、Yale、Lion、Diplomat 等。</p>
<h2>拥有证明</h2>
<p>开任何保险箱之前，我们会确认保险箱属于您或您的公司，例如购买收据、公司授权或保险箱所在地的住址证明。所有工作都会低调处理。</p>
<h2>价格</h2>
<p>保险箱开锁<strong>按情况报价</strong>，视品牌、大小和锁的种类而定。WhatsApp 保险箱的照片（正面、键盘或转盘、品牌标签）至 {PHONE}，出发前先给您报价。</p>
""",
 faqs=[("能不弄坏保险箱就打开吗？", "很多情况下可以，这正是保险箱技师的专业。方法视保险箱而定，开工前会先说明方法和价格。"),
       ("忘记保险箱密码怎么办？", "先试试厂家的重设方法。如果不行，WhatsApp 保险箱的照片给我们报价。"),
       ("你们帮公司开保险箱吗？", "会。办公室、店铺和船只都可以，但需要公司的授权。"),
       ("保险箱开锁要多少钱？", "按情况报价。WhatsApp 照片至 {PHONE} 即可获得报价。")],
 svc="Safe opening", minp=None),
"car-locksmith/": dict(
 title="汽车开锁 车钥匙复制 新加坡24小时 | 所有品牌 | Uncle Thomas",
 desc="钥匙锁在车里，或想复制一把汽车遥控钥匙？Uncle Thomas 无损汽车开锁，并为所有主要品牌复制车钥匙，24小时全岛服务。电话 9224 9224。",
 h1="汽车开锁和车钥匙复制",
 sub="钥匙锁在车里、遥控钥匙没反应，或只剩最后一把钥匙？Uncle Thomas 无损打开所有主要品牌的汽车，也能复制汽车遥控钥匙，让您多一把后备钥匙。",
 badges=["开锁 S$100 起", "所有主要品牌", "24小时全岛"],
 body="""
<h2>1. 汽车开锁</h2>
<ul>
<li>钥匙锁在车里或后车厢。</li>
<li>遥控钥匙没电，车门打不开。</li>
<li>在停车场、油站或路边被锁在车外 — 新加坡任何地方。</li>
</ul>
<p>我们用专业的汽车开锁工具，不会弄坏车漆、胶条或车窗。</p>
<h2>2. 车钥匙复制（遥控钥匙）</h2>
<p>只剩一把钥匙？我们可以复制汽车遥控钥匙和智能钥匙，让您有一把可以用的后备钥匙。这是我们唯一复制的钥匙 — 我们不配家里的钥匙。</p>
<p>WhatsApp 您的车牌子、型号、年份和钥匙照片（正反面）至 {PHONE}，我们会先确认能否复制以及价格。</p>
<h2>汽车品牌</h2>
<p>所有主要品牌，包括丰田（Toyota）、本田（Honda）、奔驰（Mercedes-Benz）、宝马（BMW）、奥迪（Audi）、大众（Volkswagen）、马自达（Mazda）、雷克萨斯（Lexus）、路虎（Land Rover）、现代（Hyundai）、起亚（Kia）、日产（Nissan）、保时捷（Porsche）、沃尔沃（Volvo）、三菱（Mitsubishi）和斯巴鲁（Subaru）等。不确定您的车型？请致电或 WhatsApp 询问。</p>
<div class="callout"><p><strong>拥有证明：</strong>开车门或复制钥匙之前，我们会确认车辆属于您，例如身份证和车辆登记文件（log card）。</p></div>
<h2>价格</h2>
<p>汽车开锁 <strong>S$100 起</strong>。车钥匙复制视品牌、型号和钥匙种类报价。</p>
""",
 faqs=[("开车门会弄坏我的车吗？", "不会。我们用专业的无损开锁工具，不会弄坏车漆、胶条或车窗。"),
       ("你们能复制汽车遥控钥匙吗？", "可以。我们为所有主要品牌复制汽车遥控钥匙和智能钥匙。请发送车型、年份和钥匙照片报价。"),
       ("你们也配家里的钥匙吗？", "不配。汽车遥控钥匙是我们唯一复制的钥匙。"),
       ("汽车开锁要多少钱？", "S$100 起，出发前先确认价格。")],
 svc="Car locksmith: unlocking and key fob cloning", minp=100),
"lock-replacement/": dict(
 title="换锁 新加坡 | 组屋大门锁、铁门锁更换 S$100起 | Uncle Thomas",
 desc="需要换锁？组屋大门锁、铁门锁、房门和厕所门锁更换，全岛服务，S$100起（含锁及安装），保修无期限。电话 9224 9224。",
 h1="新加坡换锁 — 大门锁和铁门锁",
 sub="钥匙不见了、刚搬新家，或锁已经旧了？Uncle Thomas 用优质的锁为您更换大门锁、铁门锁和房门锁，每次换锁都享有无期限保修。",
 badges=["S$100 起", "保修无期限", "当场更换"],
 body="""
<h2>什么时候应该换锁</h2>
<ul>
<li><strong>刚搬进新家</strong> — 您不知道还有多少旧钥匙在外面。</li>
<li><strong>钥匙不见或被偷。</strong></li>
<li><strong>租客或女佣搬走了。</strong></li>
<li><strong>锁很紧、松动或卡住</strong> — 旧锁随时可能把您锁在门外。</li>
<li><strong>家里被闯空门之后。</strong></li>
<li><strong>升级保安</strong> — 或改装<a href="~/digital-lock-installation/">电子锁或智能锁</a>（英文）。</li>
</ul>
<h2>我们更换的锁</h2>
<ul>
<li>组屋大门锁 — 插芯锁、锁芯、门闩和把手。</li>
<li>组屋铁门锁 — 钩锁、挂锁和铁门锁组。</li>
<li>房门、厕所门锁和门把。</li>
<li>公寓、有地住宅和办公室门锁。</li>
<li><a href="~/letterbox-lock-replacement/">信箱锁</a>（英文）。</li>
</ul>
<h2>保修</h2>
<p>{WARRANTY}</p>
<h2>价格</h2>
<p>大门或铁门换锁 <strong>S$100 起</strong>，包括新锁和安装。WhatsApp 锁的照片至 {PHONE}，即可获得准确报价。</p>
""",
 faqs=[("搬新家应该换锁吗？", "应该。之前的屋主、租客或装修师傅可能还有钥匙。"),
       ("你们修锁吗？", "不修。我们为您换上新锁，比修理更可靠，并享有无期限保修。"),
       ("被锁在门外，可以顺便换锁吗？", "可以。我们先开门，如有需要，同一次上门就能换锁。"),
       ("换锁要多少钱？", "大门或铁门换锁 S$100 起，包括新锁和安装，开工前先确认价格。")],
 svc="Lock change and replacement", minp=100),
}


def build_more(x):
    C = x["C"]
    for en_path, d in ZH_PAGES.items():
        path = "zh/" + en_path
        crumbs = [("首页", "zh/"), (ZH_NAMES[en_path].split("（")[0], path)]
        body_html = (d["body"].replace("{PHONE}", C.PHONE).replace("{WARRANTY}", WARRANTY_ZH).replace("{ID}", ID_ZH))
        faqs = [(q, a.replace("{PHONE}", C.PHONE)) for q, a in d["faqs"]]
        body = (REVIEW_NOTE + x["page_hero"](crumbs, d["h1"], d["sub"], d["badges"], lang="zh") +
                f'<section class="section"><div class="container narrow prose">{body_html}'
                f'<p>其他服务：' + " · ".join(f'<a href="~/zh/{p}">{ZH_NAMES[p].split("（")[0]}</a>' for p in ZH_PAGES if p != en_path) +
                ' · <a href="~/zh/emergency-locksmith/">紧急开锁</a></p></div></section>'
                f'<section class="section section-alt"><div class="container narrow">{x["faq_html"](faqs, "常见问题")}</div></section>' +
                x["cta_band"](lang="zh"))
        svc = {"@type": "Service", "@id": C.SITE + "/" + path + "#service", "name": d["h1"],
               "serviceType": d["svc"], "description": d["desc"], "provider": {"@id": x["BUSINESS_ID"]},
               "areaServed": {"@type": "Country", "name": "Singapore"}, "url": C.SITE + "/" + path, "inLanguage": "zh-SG"}
        if d["minp"]:
            svc["offers"] = {"@type": "Offer", "priceCurrency": "SGD",
                             "priceSpecification": {"@type": "PriceSpecification", "minPrice": d["minp"], "priceCurrency": "SGD"}}
        nodes = x["page_schema"](path, d["title"], d["desc"], crumbs, faqs=faqs, extra=[svc], lang="zh-SG")
        x["render"](path, d["title"], d["desc"], body, nodes, priority="0.6", lang="zh",
                    alternates={"en-SG": en_path, "zh-SG": path})
