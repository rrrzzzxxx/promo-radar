# config.py

PAGE_CONFIG = {
    "page_title": "飞鸟特价雷达 | 全网比价",
    "page_icon": "✈️", 
    "layout": "wide",
    "initial_sidebar_state": "collapsed"
}

CUSTOM_CSS = """
<style>
    /* 基础重置 */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    [data-testid="collapsedControl"] {display: none;}
    
    .stApp { background-color: #f4f6f9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    /* 彻底修复顶部白边问题 */
    .block-container { padding-top: 1rem !important; padding-bottom: 2rem !important; max-width: 1200px !important;}
    [data-testid="column"] { padding: 0 10px !important; }

    /* 顶部导航区文字防换行 */
    div[data-testid="stButton"] button p { white-space: nowrap !important; font-size: 14px; }
    div[data-testid="stButton"] button { border-radius: 6px; font-weight: 600; }

    /* 首页顶部度假风 Hero Banner */
    .home-hero-banner {
        background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=2000&q=80') center/cover;
        border-radius: 16px; padding: 50px 40px; text-align: center; color: white; margin-bottom: 30px; box-shadow: 0 8px 20px rgba(0,0,0,0.08); margin-top: 10px;
    }
    .hero-title { font-size: 32px; font-weight: 900; margin-bottom: 15px; letter-spacing: 1px;}
    .hero-subtitle { font-size: 16px; opacity: 0.9; margin-bottom: 25px; font-weight: 300;}

    /* 列表卡片 */
    .ota-card { background: #fff; border-radius: 12px; overflow: hidden; margin-bottom: 10px; transition: transform 0.2s; border: 1px solid #ebeef5; cursor: pointer;}
    .ota-card:hover { transform: translateY(-4px); box-shadow: 0 10px 20px rgba(0,0,0,0.06); }
    .img-wrapper { position: relative; width: 100%; height: 160px; background: #eee;}
    .img-wrapper img { width: 100%; height: 100%; object-fit: cover; }
    .badge-red { position: absolute; top: 0; left: 0; background: linear-gradient(135deg, #ff4b2b, #ff416c); color: #fff; padding: 4px 10px; border-radius: 12px 0 12px 0; font-size: 11px; font-weight: bold;}
    .card-info { padding: 12px 15px; }
    .card-vendor { font-size: 12px; color: #888; margin-bottom: 4px;}
    .card-title { font-size: 15px; font-weight: 700; color: #222; line-height: 1.4; height: 42px; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; margin-bottom: 8px;}
    .card-tags { margin-bottom: 10px; display: flex; flex-wrap: wrap; gap: 4px;}
    .card-tag { background: #f0f4ff; color: #3b82f6; font-size: 11px; padding: 2px 6px; border-radius: 4px;}
    .card-price-row { display: flex; align-items: baseline; border-top: 1px dashed #eee; padding-top: 10px;}
    .card-currency { color: #ff5000; font-size: 13px; font-weight: bold;}
    .card-price { color: #ff5000; font-size: 22px; font-weight: 900; margin-right: 6px;}

    /* 详情页专属 */
    .detail-white-panel { background: #ffffff; border-radius: 16px; padding: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); border: 1px solid #ebeef5;}
    .detail-gallery img { width: 100%; border-radius: 12px; aspect-ratio: 16/9; object-fit: cover; margin-bottom: 20px;}
    .detail-title { font-size: 24px; font-weight: 800; color: #111; margin-bottom: 15px; line-height: 1.4;}
    .price-banner { background: linear-gradient(135deg, #ff7a00, #ff4d00); padding: 15px 20px; color: white; display: flex; justify-content: space-between; align-items: center; border-radius: 12px; margin-bottom: 20px; }
    .main-price-box { display: flex; align-items: baseline; gap: 4px;}
    .main-price-box .cur { font-size: 18px; font-weight: bold;}
    .main-price-box .num { font-size: 36px; font-weight: 900;}

    /* 核心比价模块 */
    .compare-container { background: #fafbfc; border: 1px solid #ebeef5; border-radius: 12px; padding: 15px; margin-top: 20px; }
    .compare-header { font-size: 16px; font-weight: bold; color: #333; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; padding-bottom: 10px;}
    .compare-row { display: flex; justify-content: space-between; align-items: center; padding: 12px 10px; border-bottom: 1px dashed #eee; transition: background 0.2s; border-radius: 8px;}
    .compare-row:hover { background: #f0f4ff; }
    .compare-left { display: flex; align-items: center; gap: 12px; }
    .rank-badge { width: 22px; height: 22px; background: #ddd; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 12px;}
    .rank-1 { background: linear-gradient(135deg, #ff4b2b, #ff416c); transform: scale(1.1);}
    .rank-2 { background: #ff9800; }
    .rank-3 { background: #ffc107; }
    .platform-name { font-weight: bold; color: #333; font-size: 14px;}
    .compare-right { display: flex; align-items: center; gap: 10px; }
    .compare-price { font-size: 20px; font-weight: 900; color: #ff5000; font-family: Tahoma, sans-serif;}
    .lowest-tag { background: #ffeaea; color: #ff416c; padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: bold; border: 1px solid #ff416c;}
    .go-btn { background: #ff5000; color: white; padding: 5px 12px; border-radius: 15px; font-size: 12px; font-weight: bold; text-decoration: none;}

    /* 订单页卡片 */
    .order-card { background: white; border: 1px solid #e5e5e5; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);}
    .order-header { background: #fafafa; padding: 12px 20px; border-bottom: 1px solid #f0f0f0; display: flex; justify-content: space-between; border-radius: 12px 12px 0 0; color: #555; font-size: 13px;}
    .order-body { padding: 20px; display: flex; align-items: center; }
</style>
"""