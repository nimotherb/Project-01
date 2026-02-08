import streamlit as st

# ==========================================
# 🛠️ 系統基礎設定與 CSS
# ==========================================
st.set_page_config(page_title='Project 靈驗', page_icon='⛩️', layout='wide')

st.markdown("""
<style>
    .stApp {background-color: #0E1117; color: #00FF41; font-family: 'Courier New';}
    [data-testid="stSidebar"] {background-color: #161B22;}
    h1, h2, h3 {color: #E0E0E0 !important; text-shadow: 0 0 10px #00FF41;}
    div[data-testid="stMetricValue"] {color: #00FF41;}
    /* 讓圖片容器自動適應 */
    img { max-width: 100%; height: auto; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🎛️ 側邊欄：環境參數模擬
# ==========================================
st.sidebar.title('🎛️ 環境參數模擬')
rainfall = st.sidebar.slider('🌧️ 降雨量 (mm)', 0, 500, 20)
wind = st.sidebar.slider('💨 風速 (m/s)', 0, 60, 5)
pest = st.sidebar.slider('🐛 病蟲害指數', 0, 10, 1)

# ==========================================
# 🧠 核心邏輯：風險運算
# ==========================================
# 簡單的加權算法
risk_score = (rainfall * 0.2) + (wind * 0.5) + (pest * 10)
# 限制最高分為 100
if risk_score > 100: 
    risk_score = 100

# ==========================================
# 🖥️ 主畫面：戰情中心
# ==========================================
st.title('⛩️ Project 靈驗：天巡者戰情中心')

# 顯示關鍵指標
col1, col2, col3 = st.columns(3)
col1.metric("🌧️ 降雨", f"{rainfall}")
col2.metric("💨 風速", f"{wind}")
col3.metric("⚡ 風險", f"{int(risk_score)}")

st.divider()

# 根據風險分數顯示不同狀態
if risk_score < 60:
    st.success('✅ M.O. 系統狀態：ONLINE (安全)')
    # 安全狀態：顯示熱茶 (代表歲月靜好)
    st.image("https://img.icons8.com/color/96/tea.png", width=100)
    st.caption("目前環境穩定，適合農耕與巡視。")
else:
    st.error('🚨 警告：天巡者防禦系統啟動！')
    # 危險狀態：顯示無人機 (代表出動防禦)
    st.image("https://img.icons8.com/color/96/drone.png", width=100)
    st.caption("偵測到極端氣候或蟲害，無人機已自動起飛執行任務。")
