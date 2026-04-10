# data/mock_data.py

MOCK_DEALS = [
    {
        "id": "m1", "airline": "海南航空", "title": "飞越北美 西雅图直飞复航 留学生专享额外行李", 
        "price": "4500", "ori_price": "8000", "sales": "已售 300+件", "img": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=800&q=80", "badge": "复航特惠", "tags": ["直飞北美", "留学生最爱"],
        "full_rules": "1. 留学生凭F1签证可额外申请一件免费托运行李。\n2. 退改签需提前7天。",
        "platforms": [
            {"name": "飞猪旅行", "price": 4500}, {"name": "携程旅行", "price": 4520},
            {"name": "同程旅行", "price": 4680}, {"name": "去哪儿", "price": 4550}, {"name": "海航官网", "price": 4510}
        ]
    },
    {
        "id": "m2", "airline": "四川航空", "title": "国内热门旅游地 胖达特惠 感受云端美食", 
        "price": "399", "ori_price": "900", "sales": "已售 1500+件", "img": "https://images.unsplash.com/photo-1550850839-8dc894ed385a?auto=format&fit=crop&w=800&q=80", "badge": "全网比价", "tags": ["老干妈", "美食航空"],
        "full_rules": "1. 经停成都机场。\n2. 包含20kg免费托运。",
        "platforms": [
            {"name": "飞猪旅行", "price": 399}, {"name": "携程旅行", "price": 415},
            {"name": "去哪儿", "price": 420}, {"name": "同程旅行", "price": 435}, {"name": "途牛旅游", "price": 450}
        ]
    },
    {
        "id": "m3", "airline": "澳门航空", "title": "买一送一 寻味澳门 周末双人往返套票", 
        "price": "600", "ori_price": "1400", "sales": "已售 800+件", "img": "https://images.unsplash.com/photo-1584286595398-a59f21d313f5?auto=format&fit=crop&w=800&q=80", "badge": "底价监控", "tags": ["往返特惠", "美食之旅"],
        "full_rules": "1. 需两人同时预订，展示为单人均价。\n2. 周五去周日回。",
        "platforms": [
            {"name": "携程旅行", "price": 600}, {"name": "飞猪旅行", "price": 630},
            {"name": "同程旅行", "price": 615}, {"name": "澳航官网", "price": 650}, {"name": "去哪儿", "price": 680}
        ]
    },
    {
        "id": "m4", "airline": "酷航 Scoot", "title": "新加坡转机 澳洲/巴厘岛特惠 体验波音787", 
        "price": "999", "ori_price": "2200", "sales": "已售 2100+件", "img": "https://images.unsplash.com/photo-1528702748617-c64d49f918af?auto=format&fit=crop&w=800&q=80", "badge": "性价比高", "tags": ["787宽体机", "转机优惠"],
        "full_rules": "1. 不含托运行李，需单独购买。\n2. 机上餐食和水需自费。",
        "platforms": [
            {"name": "去哪儿", "price": 999}, {"name": "酷航官网", "price": 1050},
            {"name": "飞猪旅行", "price": 1020}, {"name": "携程旅行", "price": 1100}, {"name": "同程旅行", "price": 1150}
        ]
    },
    {
        "id": "m5", "airline": "亚洲航空", "title": "东南亚全线 0元大促 往返曼谷/吉隆坡", 
        "price": "386", "ori_price": "1200", "sales": "热卖中", "img": "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?auto=format&fit=crop&w=800&q=80", "badge": "距结束12小时", "tags": ["曼谷/吉隆坡", "极简出行"],
        "full_rules": "1. 价格为税费，机票本身0元。\n2. 不含免费托运。",
        "platforms": [
            {"name": "亚航官网", "price": 386}, {"name": "飞猪旅行", "price": 420},
            {"name": "携程旅行", "price": 435}, {"name": "去哪儿", "price": 450}, {"name": "同程旅行", "price": 480}
        ]
    },
    {
        "id": "m6", "airline": "中国国际航空", "title": "欧洲航线 提前60天早鸟价 直飞巴黎/伦敦", 
        "price": "3800", "ori_price": "7500", "sales": "剩余 12 席", "img": "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?auto=format&fit=crop&w=800&q=80", "badge": "长期有效", "tags": ["直飞欧洲", "早鸟优惠"],
        "full_rules": "1. 必须提前至少60天出票。\n2. 退票手续费极高。",
        "platforms": [
            {"name": "同程旅行", "price": 3800}, {"name": "携程旅行", "price": 3850},
            {"name": "飞猪旅行", "price": 3880}, {"name": "去哪儿", "price": 3950}, {"name": "国航官网", "price": 4100}
        ]
    },
    {
        "id": "m7", "airline": "南方航空", "title": "畅游中国 2026版 季卡预售 周末无限飞", 
        "price": "3299", "ori_price": "8888", "sales": "已售 5000+件", "img": "https://images.unsplash.com/photo-1502224562085-639556652f33?auto=format&fit=crop&w=800&q=80", "badge": "全网爆款", "tags": ["无限次飞行", "出差党"],
        "full_rules": "1. 激活后90天内有效。\n2. 同一航线最多可飞2次往返。",
        "platforms": [
            {"name": "南航官网", "price": 3299}, {"name": "飞猪旅行", "price": 3299},
            {"name": "携程旅行", "price": 3350}, {"name": "同程旅行", "price": 3400}, {"name": "去哪儿", "price": 3450}
        ]
    },
    {
        "id": "m8", "airline": "全日空 ANA", "title": "双十一大促 中日往返超低价 跨年可用", 
        "price": "1499", "ori_price": "3500", "sales": "已售 400+件", "img": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=800&q=80", "badge": "最后1天", "tags": ["五星服务", "含2件行李"],
        "full_rules": "1. 包含两件23kg超大行李额。\n2. 樱花季部分日期可用，需尽早锁座。",
        "platforms": [
            {"name": "飞猪旅行", "price": 1499}, {"name": "全日空官网", "price": 1520},
            {"name": "携程旅行", "price": 1580}, {"name": "去哪儿", "price": 1650}, {"name": "同程旅行", "price": 1720}
        ]
    }
]