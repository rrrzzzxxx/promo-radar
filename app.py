import streamlit as st
import time
from config import PAGE_CONFIG, CUSTOM_CSS
from data.mock_data import MOCK_DEALS

# ==========================================
# 0. 初始化配置与状态
# ==========================================
st.set_page_config(**PAGE_CONFIG)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

if 'current_page' not in st.session_state: st.session_state.current_page = 'list'
if 'selected_deal' not in st.session_state: st.session_state.selected_deal = None
if 'search_query' not in st.session_state: st.session_state.search_query = ""

if 'api_key' not in st.session_state: st.session_state.api_key = ""
if 'base_url' not in st.session_state: st.session_state.base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
if 'model_name' not in st.session_state: st.session_state.model_name = "qwen-plus"

def navigate_to(page, deal=None):
    st.session_state.current_page = page
    if deal: 
        st.session_state.selected_deal = deal
        st.session_state.show_comparison = False 
        st.session_state.show_ai_result = False
    st.rerun()

# ==========================================
# 1. 真实 AI 调用逻辑
# ==========================================
@st.dialog("⚙️ 引擎配置 (接入大模型)")
def ai_settings_dialog():
    st.markdown("配置 API Key 即可激活真实的 AI 避坑与比价分析功能。")
    api_key = st.text_input("🔑 API Key", value=st.session_state.api_key, type="password")
    base_url = st.text_input("🌐 Base URL", value=st.session_state.base_url)
    model = st.text_input("🧠 模型名称", value=st.session_state.model_name)
    
    if st.button("保存配置", type="primary", use_container_width=True):
        st.session_state.api_key = api_key
        st.session_state.base_url = base_url
        st.session_state.model_name = model
        st.rerun()

def run_real_ai_analysis(item):
    platforms_str = "、".join([f"{p['name']}(￥{p['price']})" for p in item['platforms']])
    rules = item['full_rules']
    
    if not st.session_state.api_key:
        return f"⚠️ **未配置 API Key。** 请点击右上角「⚙️ AI配置」。\n\n*以下为示例分析：*\n当前发现最低价平台。但请注意隐藏条款限制。建议综合考虑税费和行李额度后下单。"
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=st.session_state.api_key, base_url=st.session_state.base_url)
        prompt = f"""
        你是一个资深的特价机票精算师。请分析产品【{item['title']}】。
        该产品的底层规则限制：{rules}。
        全网各平台实时报价：{platforms_str}。
        
        请给出客观的购票决策建议，包含以下两点：
        1. 价格差异与避坑分析（指出哪个平台最便宜，结合规则说明隐藏陷阱）。
        2. 综合购买建议。
        语气专业、客观。字数控制在150字左右。
        """
        response = client.chat.completions.create(
            model=st.session_state.model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ 调用失败：{str(e)}"

# ==========================================
# 2. 顶部导航 Header
# ==========================================
def render_header():
    st.write("") 
    col_logo, col_space, col_nav = st.columns([2, 5, 4.5], vertical_alignment="center")
    
    with col_logo:
        st.markdown("<div style='font-size:24px; font-weight:900; color:#ff5000; font-style:italic;'>✈️ PromoRadar</div>", unsafe_allow_html=True)
    with col_nav:
        c1, c2, c3 = st.columns(3)
        if c1.button("📑 我的订单", use_container_width=True): navigate_to('orders')
        if c2.button("🎧 帮助中心", use_container_width=True): navigate_to('help')
        if c3.button("⚙️ AI配置", use_container_width=True): ai_settings_dialog()

# ==========================================
# 3. 页面渲染模块
# ==========================================
def render_list_page(data=MOCK_DEALS, title=""):
    if st.session_state.current_page == 'list':
        st.markdown("""
        <div class="home-hero-banner">
            <div class="hero-title">发现世界，以不可思议的全网底价</div>
            <div class="hero-subtitle">聚合全网各大平台 S 级大促，彻底打破信息差</div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("search_form", border=False):
            sc1, sc2 = st.columns([5, 1])
            query = sc1.text_input("搜索", placeholder="🔍 想去哪里？搜一搜全网底价...", label_visibility="collapsed")
            submit = sc2.form_submit_button("全网搜", type="primary", use_container_width=True)
            if submit and query:
                st.session_state.search_query = query
                navigate_to('search')
    
    st.markdown(f"<h3 style='color:#333; margin-top:10px;'>{title if title else '🔥 今日全网底价榜单'}</h3>", unsafe_allow_html=True)
    cols = st.columns(4)
    for index, item in enumerate(data):
        with cols[index % 4]:
            tags_html = "".join([f"<span class='card-tag'>{tag}</span>" for tag in item['tags']])
            st.markdown(f"""
            <div class="ota-card" onclick="this.closest('.element-container').nextElementSibling.querySelector('button').click()">
                <div class="img-wrapper"><span class="badge-red">{item['badge']}</span><img src="{item['img']}"></div>
                <div class="card-info">
                    <div class="card-vendor">🏢 {item['airline']}</div>
                    <div class="card-title">{item['title']}</div>
                    <div class="card-tags">{tags_html}</div>
                    <div class="card-price-row">
                        <span class="card-currency">￥</span><span class="card-price">{item['price']}</span>
                        <span style="color:#ff416c; font-weight:bold; font-size:12px; margin-left:auto;">查看全网底价 ></span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("查看详情", key=f"btn_{item['id']}", use_container_width=True): 
                navigate_to('detail', item)

def render_search_page():
    # 增加返回首页按钮
    if st.button("⬅️ 返回首页"): navigate_to('list')
    query = st.session_state.search_query
    results = [item for item in MOCK_DEALS if query in item['title'] or query in item['airline']]
    st.info(f"为您找到关于 **“{query}”** 的比价结果 {len(results)} 条：")
    render_list_page(results, title="搜索结果")

def render_detail_page():
    item = st.session_state.selected_deal
    if st.button("⬅️ 返回列表"): navigate_to('list')
    
    st.markdown('<div class="detail-white-panel">', unsafe_allow_html=True)
    
    left_col, right_col = st.columns([1.1, 1])
    with left_col:
        st.markdown(f"<div class='detail-gallery'><img src='{item['img']}'></div>", unsafe_allow_html=True)

    with right_col:
        st.markdown(f"<div class='detail-title'>{item['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="price-banner">
            <div class="main-price-box"><span style="font-size:14px; opacity:0.9;">基准起步价</span><span class="cur">￥</span><span class="num">{item['price']}</span></div>
            <div>{item['sales']}</div>
        </div>
        """, unsafe_allow_html=True)

        btn1, btn2 = st.columns([1, 1])
        with btn1:
            if st.button("✨ AI 购票精算师", use_container_width=True):
                st.session_state.show_ai_result = not st.session_state.get('show_ai_result', False)
        with btn2:
            if st.button("👁️ 查看全网各平台底价", type="primary", use_container_width=True):
                st.session_state.show_comparison = True

        if st.session_state.get('show_ai_result', False):
            with st.spinner("AI 精算师正在对比全网报价与隐藏条款..."):
                result = run_real_ai_analysis(item)
                st.info(f"**🤖 购票决策建议：**\n\n{result}")

        if st.session_state.get('show_comparison', False):
            sorted_platforms = sorted(item['platforms'], key=lambda x: x['price'])
            st.markdown("<div class='compare-container'><div class='compare-header'><span>📊 全网实时比价排行榜</span></div>", unsafe_allow_html=True)
            for idx, plat in enumerate(sorted_platforms):
                rank = idx + 1
                r_cls = f"rank-{rank}" if rank <= 3 else ""
                tag = "<span class='lowest-tag'>🔥全网底价</span>" if rank == 1 else ""
                html = f"""<div class="compare-row">
<div class="compare-left"><div class="rank-badge {r_cls}">{rank}</div><div class="platform-name">{plat['name']}</div></div>
<div class="compare-right">{tag}<div class="compare-price">￥{plat['price']}</div><a href="#" class="go-btn">去购买</a></div>
</div>"""
                st.markdown(html, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["📝 产品图文详情", "✈️ 费用包含与航班信息", "🔄 退改签说明"])
    with tab1:
        st.markdown("### 🌟 行程亮点概览")
        st.write(f"本产品由 **{item['airline']}** 倾情提供。")
        c1, c2, c3 = st.columns(3)
        c1.info("✔️ 官方直营货源\n保证出票，拒绝假票")
        c2.info("✔️ 航协认证代理\n支持行程单开具")
        c3.info("✔️ 专属客服保障\n7x24小时为您护航")
        st.image(item['img'], use_container_width=True, caption="目的地风光剪影")
    with tab2:
        st.success("**费用包含：**\n- 对应航段的经济舱机票一张。\n- 机场建设费与燃油附加费（部分特惠票需另付）。")
        st.warning("**费用不含：**\n- 旅游意外险及航空延误险。\n- 目的地当地签证及住宿费用。")
    with tab3:
        st.write("特价机票（包含折扣幅度极大的机票）往往伴随着严格的退改限制，具体如下：")
        st.markdown("- **退票规则**：航班起飞前72小时外退票，收取票面价 40% 的手续费。")
        st.markdown("- **改签规则**：允许同航司同航线改签一次，需补齐实时舱位差价并支付 300元/次的改期费。")

# ==========================================
# 4. 充实订单页与帮助中心 (加入返回按钮)
# ==========================================
def render_orders_page():
    # 增加返回首页按钮
    if st.button("⬅️ 返回首页"): navigate_to('list')
    st.markdown("## 📑 我的特价订单")
    tab1, tab2, tab3 = st.tabs(["全部订单", "待出行", "退款/售后"])
    
    with tab1:
        st.markdown("""
        <div class="order-card">
            <div class="order-header">
                <span>2026-03-15 &nbsp;&nbsp; 订单号：884719203912</span>
                <span style="color:#10b981;">交易成功</span>
            </div>
            <div class="order-body">
                <div style="width:40px; height:40px; background:#ff5000; color:white; border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:20px; margin-right:20px;">国</div>
                <div style="flex-grow:1;">
                    <div style="font-size:15px; font-weight:bold; margin-bottom:6px;">中国国航 CA1501 北京-上海 (单程特价)</div>
                    <div style="color:#888; font-size:13px;">出行日期：2026-03-20 | 乘机人：李四</div>
                </div>
                <div style="width:120px; text-align:center; border-left:1px solid #eee;">
                    <div style="font-weight:900; font-size:18px;">￥450.00</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="order-card">
            <div class="order-header">
                <span>2026-04-09 &nbsp;&nbsp; 订单号：325301603048</span>
                <span style="color:#ff5000; font-weight:bold;">即将出行</span>
            </div>
            <div class="order-body">
                <div style="width:40px; height:40px; background:#3b82f6; color:white; border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:20px; margin-right:20px;">亚</div>
                <div style="flex-grow:1;">
                    <div style="font-size:15px; font-weight:bold; margin-bottom:6px;">亚洲航空 FD531 广州-曼谷 (往返特惠)</div>
                    <div style="color:#888; font-size:13px;">出行日期：2026-05-01 | 乘机人：王五</div>
                </div>
                <div style="width:120px; text-align:center; border-left:1px solid #eee;">
                    <div style="font-weight:900; font-size:18px;">￥880.00</div>
                    <button style="margin-top:10px; background:#ff5000; color:white; border:none; padding:4px 10px; border-radius:4px; cursor:pointer;">值机选座</button>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_help_page():
    # 增加返回首页按钮
    if st.button("⬅️ 返回首页"): navigate_to('list')
    st.markdown("## 🎧 帮助中心与客服支持")
    
    st.info("💡 购票前必看：为您整理的全网比价防坑指南。")
    
    with st.expander("🤔 为什么不同平台的同一航班价格会不一样？", expanded=True): 
        st.write("OTA（在线旅游平台）会根据自身的促销活动、代理商政策、搭售保险情况等动态调整价格。本平台通过爬虫技术，将这些隐藏在底层的价格实时抓取并展示给您，帮您打破信息垄断。")
        
    with st.expander("🤖 AI 购票精算师是如何给出建议的？"): 
        st.write("我们的 AI 接入了企业级的大语言模型（LLM）。当您点击分析时，AI 会同时读取该产品的「退改签条款」和「各大平台报价明细」。例如，它能识别出某平台虽然便宜了50元，但剥夺了您的免费托运额度，从而为您计算出真实的性价比并给出明确的购买建议。")
        
    with st.expander("💸 如果发生了退票，退款一般多久到账？"): 
        st.write("如果您在导购跳转后的平台成功取消了机票，款项通常将在 1-3 个工作日内极速原路退回您的支付账户。遇节假日可能会顺延。")
        
    st.markdown("---")
    st.markdown("### 📞 联系人工客服")
    st.code("客服热线: 400-888-Promo\n服务邮箱: support@promoradar.com\n工作时间: 全年 7x24 小时")

# ==========================================
# 5. 顶级路由分发
# ==========================================
render_header()
if st.session_state.current_page == 'list': render_list_page()
elif st.session_state.current_page == 'detail': render_detail_page()
elif st.session_state.current_page == 'search': render_search_page()
elif st.session_state.current_page == 'orders': render_orders_page()
elif st.session_state.current_page == 'help': render_help_page()