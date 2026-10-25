"""
Chinese (Simplified, Singapore) pages: /zh/ and /zh/emergency-locksmith/
Targets searches such as 锁匠, 开锁, 新加坡锁匠, 紧急开锁.

FILL: a native Chinese speaker must review all text on these pages before launch.
"""

ZH_NAMES = {
    "emergency-locksmith/": "紧急开锁",
    "digital-lock-opening/": "电子锁开锁",
    "digital-lock-installation/": "电子锁安装",
    "safe-opening/": "保险箱开锁",
    "car-locksmith/": "汽车开锁",
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
    rows = "".join(f'<tr><td><a href="~/{p}">{label}</a></td><td>{v}</td></tr>' for label, p, v in ZH_PRICES)
    return ('<div class="price-wrap"><table class="price-table"><thead><tr><th scope="col">服务</th><th scope="col">价格</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>')


HOME_FAQS = [
    ("你们真的24小时服务吗？", "是的。Uncle Thomas Locksmith 全年无休，每天24小时提供服务，包括周末和公共假期，覆盖新加坡全岛。"),
    ("开锁要多少钱？", "白天（上午9点至傍晚6点）开锁 S$80 起，非办公时间、周末及公共假期 S$120 起。电子锁开锁 S$150 起，汽车开锁 S$100 起。开工前一定先确认价格。"),
    ("开门前会核对身份吗？", "会。" + ID_ZH),
    ("会不会弄坏我的门？", "我们尽可能使用无损方法开锁，大多数情况下不会损坏门锁。如果无法无损开锁，会先向您说明方案和价格，经您同意才进行。"),
    ("你们配钥匙或修锁吗？", "不提供。我们专门开门锁、电子锁和保险箱，以及换锁和安装新锁。坏掉的锁我们会直接更换，而不是修理。"),
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

    svc_cards = "".join(
        f'<a class="card" href="~/{p}"><h3>{n}</h3><span class="more">了解更多（英文）→</span></a>'
        for p, n in ZH_NAMES.items())

    # ------------------------------------------------------------ /zh/
    title = "新加坡锁匠 24小时开锁 | 紧急开锁 S$80起 | Uncle Thomas"
    desc = ("被锁在门外？Uncle Thomas 自1998年起提供新加坡24小时紧急开锁服务：组屋、公寓、电子锁、保险箱和汽车开锁，"
            "全岛服务，S$80起。电话 9224 9224。")
    body = f"""{REVIEW_NOTE}
<section class="hero">
  <div class="container hero-inner">
    <div>
      <p class="eyebrow">🔑 新加坡锁匠"师傅" · 自{C.FOUNDED}年</p>
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
    <p class="note">我们专门开锁、换锁和安装新锁，<strong>不</strong>提供配钥匙或修锁服务。</p>
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
<li><strong>电子锁打不开？</strong>电池没电、忘记密码或键盘故障 — 请看<a href="~/digital-lock-opening/">电子锁开锁</a>（英文）。</li>
<li><strong>钥匙锁在车里？</strong>请看<a href="~/car-locksmith/">汽车开锁</a>（英文）。</li>
</ul>

<h2>无损开锁优先</h2>
<p>Uncle Thomas 入行{C.YEARS}年以上，大多数机械锁和电子锁都能在不钻孔、不撬门的情况下打开。如果锁已严重磨损或损坏，无法无损打开，我们会<em>先</em>向您说明方案和价格。如果需要换锁，可以当场<a href="~/lock-replacement/">更换</a>，{WARRANTY_ZH}</p>

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
