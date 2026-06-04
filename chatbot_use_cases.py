import streamlit as st

st.set_page_config(
    page_title='AI Chatbot - Use Cases',
    page_icon='💬',
    layout='wide',
)

st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1a1a1a;
        margin-bottom: 4px;
    }
    .main-subtitle {
        font-size: 1rem;
        color: #666;
        margin-bottom: 32px;
    }
    .card {
        background: #fff;
        border-radius: 10px;
        padding: 24px 20px 20px 20px;
        min-height: 420px;
        box-shadow: 0 1px 6px rgba(0,0,0,0.07);
    }
    .card-header-blue  { border-top: 5px solid #3B82F6; }
    .card-header-purple { border-top: 5px solid #8B5CF6; }
    .card-header-orange { border-top: 5px solid #F97316; }

    .use-case-label-blue   { color: #3B82F6; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; }
    .use-case-label-purple { color: #8B5CF6; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; }
    .use-case-label-orange { color: #F97316; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; }

    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1a1a1a;
        margin: 4px 0 16px 0;
    }
    .divider { border: none; border-top: 1px solid #e5e7eb; margin: 0 0 16px 0; }
    .query-bubble {
        background: #EFF6FF;
        border-radius: 8px;
        padding: 12px 14px;
        margin-bottom: 10px;
        font-size: 0.92rem;
        color: #1e3a5f;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">AI Chatbot - Use Cases</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Natural language queries store leaders and associates can ask, no training required</div>', unsafe_allow_html=True)

use_cases = [
    {
        "color": "blue",
        "label": "USE CASE 1",
        "title": "Myself — Intro Script Builder",
        "queries": [
            "Pull my district's store count, state count, and last year's contribution dollars to build my DM intro.",
            "Generate my GM intro paragraph using my store name, sales, and contribution for last year.",
        ],
    },
    {
        "color": "purple",
        "label": "USE CASE 2",
        "title": "My Customer — Profile & Medallia",
        "queries": [
            "Show me my store's repeat customer %, household income %, and average customer age from MyInsights.",
            "Find my top-rated Medallia customer comment from the last 30 days and my 2 highest Medallia scores.",
        ],
    },
    {
        "color": "orange",
        "label": "USE CASE 3",
        "title": "My Business — QTD & Four C's",
        "queries": [
            "What is my QTD budget gap and how many extra transactions per day do I need to close it by end of quarter?",
            "Summarize my Comp, Conversion, Card, and Customer metrics vs. plan with wins and opportunities for each C.",
        ],
    },
]

cols = st.columns(3, gap="medium")

for col, uc in zip(cols, use_cases):
    c = uc["color"]
    with col:
        queries_html = "".join(
            f'<div class="query-bubble">{q}</div>' for q in uc["queries"]
        )
        st.markdown(f"""
        <div class="card card-header-{c}">
            <div class="use-case-label-{c}">{uc["label"]}</div>
            <div class="card-title">{uc["title"]}</div>
            <hr class="divider">
            {queries_html}
        </div>
        """, unsafe_allow_html=True)
