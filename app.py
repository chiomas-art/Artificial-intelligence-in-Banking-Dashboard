import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import streamlit as st
from matplotlib.colors import LinearSegmentedColormap

# ---------------------------------------------------------------- THEME
GREEN, DARK_GREEN, ORANGE, BLACK, WHITE, GREY = (
    "#1B8A3C", "#0F5C27", "#FF8C00", "#111111", "#FFFFFF", "#E5E7EB")
LIKERT_ORDER = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
LIKERT_MAP = {k.lower(): i + 1 for i, k in enumerate(LIKERT_ORDER)}
LIKERT_COLORS = ["#C2410C", "#FDBA74", "#D1D5DB", "#6EE7A0", "#15803D"]
GROUPS = {"Accuracy": range(6, 11), "Timeliness": range(12, 17),
          "Reliability": range(17, 22), "Challenges": range(23, 28),
          "Compliance": range(28, 33)}
DEMOS = ["Gender", "Age", "Marital status", "Education"]
PALETTE = [GREEN, ORANGE, BLACK, "#7CCB92", "#FFC266"]
GREEN_ORANGE = LinearSegmentedColormap.from_list("go", [ORANGE, WHITE, GREEN])


# ---------------------------------------------------------------- DATA
# The survey (83 respondents) is built into this file, so no CSV or upload is needed.
# Each row = gender, age, marital status, education, then 25 answers (1-5, 0 = blank).
ROWS = [
    "F0SW5555555555444444444444445",
    "F0MH5555545555554353513345255",
    "M0SH5544455454445445445444454",
    "F1SH4433455444345553545434443",
    "F0SH4433344343344343454533343",
    "M0SW4443445344444544453445444",
    "F0SH5555544444434444453444344",
    "F0SH5444445545445443454444304",
    "M0SH4533444424444444443345555",
    "F1SH4543335403234222444222332",
    "M0SW4444444444444444444444444",
    "F0SH5544535242444555544445544",
    "F0NW4454435454334445445344444",
    "F0SH3424455344235445545434343",
    "M0SW5555445455545554535454554",
    "M0SW5534545545435545443553445",
    "F0SH3344432233233433344334333",
    "F0SH3323334444334435555403333",
    "M1SC5444545454343434544434444",
    "F0SW4444445444444443443344444",
    "F0SH4443444444434455544444344",
    "M0SW4434333443444335343433333",
    "F2MH5555555555555555555555555",
    "F0SW5454434543433443234334343",
    "M0SH5544444455445454345445445",
    "M0SW5555555555555545555555555",
    "F0SH5455455455551552555555554",
    "M1SH4434045433434033430322343",
    "M1SH3444455554534435255435343",
    "F0SW4223414444435253145424341",
    "M0SH5534444333323544535524434",
    "F0SH4243444442334444550044444",
    "F0SH4555535455443444434444343",
    "F0SH4334434444334434434434443",
    "M0SH4444434444334444344444444",
    "M1SH4445555555444454444445555",
    "F0SW5434425333433543432333333",
    "M1SH4445544454454444435445444",
    "M1SH4553545555355445455454554",
    "F0SH5555555555555555555555555",
    "F0SH3454455554434445354455434",
    "F0SW4434354344253333355543335",
    "M0SH3333333333333333333333333",
    "F0SH4423444444344544455555455",
    "F0SH4443443444443354444443344",
    "M0SH3343434343334445544433333",
    "F0SH3434444444444444444444444",
    "F0SH4444535544334444244425343",
    "M0SH4444444444444444444444433",
    "M3MH5544555454445445444444444",
    "M0SH5544555454445445445444444",
    "M1SH5544555454445445445544444",
    "M0SC4444444444444444444444444",
    "F0SH3343444432444444554434334",
    "F0SH4544245534245354554532432",
    "F0SH4444445543444443544443433",
    "M0SH3334334343344444443444444",
    "M0SH4434455544445345445444453",
    "M0SH3444445554443443454544344",
    "M1SH4444444444444444444444444",
    "M1SH5434455555445544455544454",
    "F0SH5445544555455545455554454",
    "F0SH5434334443434444444000000",
    "M2MH5545455454244444454245434",
    "M3MH5544555454445445445444444",
    "F2SH5544555454445445445444444",
    "F2SH5544555454445445445444444",
    "F0MH5544444444444445544455544",
    "M3MH5555555454455445455444555",
    "F0SH5455545555455555554555555",
    "F0SH4454455544444504544444444",
    "M1SH5544554554345444555554455",
    "M0MH3214244443222122555432321",
    "F1MH4334433244332222554544445",
    "F0SC5544555454455555444455455",
    "F0SW5533355334112245555452433",
    "F2MC5544555454445445445444444",
    "M0SW4445544444332235555433333",
    "F0SC1121212211222121221121212",
    "F0SW4554445445555555454354545",
    "M3MH5454554545554555555444545",
    "F0SW3334333333424333353333334",
    "M0SH4545445433544544545455454",
]
QUESTION_TEXT = [
    "AI tools have improved the accuracy of financial data processing in my bank.",
    "The adoption of AI has significantly reduced human errors in our financial reporting process.",
    "AI-based systems produce financial statements that are free from material misstatements.",
    "AI has enhanced our bank's compliance with IFRS accuracy requirements.",
    "AI has strengthened our internal control environment, reducing the risk of financial misreporting.",
    "Robotic Process Automation (RPA) has reduced the time required for month-end and year-end financial closing.",
    "AI tools enable my bank to generate financial reports faster compared to traditional manual methods.",
    "The use of AI has improved my bank's ability to meet statutory reporting deadlines (CBN, FRCN).",
    "AI facilitates real-time monitoring and reporting of financial data in my bank.",
    "AI adoption has enabled timely submission of regulatory returns to the CBN and NDIC.",
    "AI systems produce financial information that faithfully represents actual economic events in my bank.",
    "NLP tools have improved the clarity and consistency of narrative disclosures in our annual reports.",
    "AI has enhanced the verifiability of financial statements through detailed digital audit trails.",
    "The use of AI has reduced management bias or manipulation in reported financial figures.",
    "AI adoption has enhanced stakeholder confidence in the transparency of our financial reporting.",
    "High implementation and maintenance costs are a major barrier to AI adoption for financial reporting in my bank.",
    "There is a significant skills gap among staff in understanding and effectively using AI tools.",
    "Poor data quality and fragmented legacy systems limit the effectiveness of AI in financial reporting.",
    "Cybersecurity threats and data privacy concerns hinder full AI integration in financial reporting.",
    "The lack of clear regulatory guidance from CBN and FRCN on AI use in reporting creates uncertainty.",
    "AI tools help my bank comply with CBN and FRCN financial reporting requirements effectively.",
    "AI supports accurate computation and disclosure of capital adequacy ratios and prudential returns.",
    "The use of AI has improved our bank's compliance with IFRS standards, particularly IFRS 9.",
    "AI-driven monitoring systems detect and flag regulatory compliance gaps in financial reports promptly.",
    "My bank uses AI tools to track and respond to changes in financial reporting regulations.",
]
GENDER = {"F": "Female", "M": "Male"}
AGE = {"0": "18-25 years", "1": "26-35 years", "2": "36-45 years", "3": "46 and above"}
MARITAL = {"S": "Single", "M": "Married", "N": "Not stated"}
EDU = {"H": "HND/Bsc", "W": "WAEC/GCE", "C": "NCE/ND"}


@st.cache_data
def load_data():
    demo = pd.DataFrame({
        "Gender": [GENDER[r[0]] for r in ROWS],
        "Age": [AGE[r[1]] for r in ROWS],
        "Marital status": [MARITAL[r[2]] for r in ROWS],
        "Education": [EDU[r[3]] for r in ROWS]})
    labels = [f"{name} Q{n}" for name in GROUPS for n in range(1, 6)]
    items = pd.DataFrame([[int(ch) for ch in r[4:]] for r in ROWS], columns=labels)
    items = items.replace(0, np.nan)
    questions = dict(zip(labels, QUESTION_TEXT))
    scores = pd.DataFrame({name: items[[f"{name} Q{n}" for n in range(1, 6)]].mean(axis=1)
                           for name in GROUPS})
    return pd.concat([demo, scores], axis=1), items, questions


def cronbach_alpha(frame: pd.DataFrame):
    frame = frame.dropna()
    k = frame.shape[1]
    if len(frame) < 3 or k < 2:
        return np.nan
    return k / (k - 1) * (1 - frame.var(ddof=1).sum() / frame.sum(axis=1).var(ddof=1))


def alpha_label(a):
    if np.isnan(a):
        return "n/a"
    return ("Excellent" if a >= .9 else "Good" if a >= .8 else
            "Acceptable" if a >= .7 else "Questionable" if a >= .6 else "Poor")


# ---------------------------------------------------------------- PAGE
st.set_page_config(page_title="AI & Financial Reporting Dashboard",
                   page_icon="📊", layout="wide")
st.markdown(f"""
<style>
.stApp {{ background:{WHITE}; color:{BLACK}; }}
h1,h2,h3,h4 {{ color:{BLACK}; }}
[data-testid="stSidebar"] {{ background:#F1FAF4; border-right:4px solid {GREEN}; }}
.hero {{ background:linear-gradient(120deg,{BLACK} 0%,#1f2a22 65%,{DARK_GREEN} 100%);
        padding:28px 34px; border-radius:16px; border-bottom:6px solid {ORANGE};
        margin-bottom:18px; }}
.hero h1 {{ color:{WHITE}; margin:0; font-size:2rem; }}
.hero p {{ color:#d6d6d6; margin:6px 0 0 0; }}
.kpi {{ background:{WHITE}; border:1px solid {GREY}; border-left:7px solid {GREEN};
       border-radius:12px; padding:14px 18px; box-shadow:0 2px 8px rgba(0,0,0,.06); }}
.kpi.orange {{ border-left-color:{ORANGE}; }}
.kpi.black {{ border-left-color:{BLACK}; }}
.kpi .v {{ font-size:1.8rem; font-weight:800; color:{BLACK}; line-height:1.1; }}
.kpi .l {{ font-size:.82rem; color:#555; text-transform:uppercase; letter-spacing:.04em; }}
.stTabs [data-baseweb="tab"] {{ font-weight:700; }}
.stTabs [aria-selected="true"] {{ color:{ORANGE} !important; }}
.stTabs [data-baseweb="tab-highlight"] {{ background-color:{ORANGE}; }}
.note {{ background:#FFF6E8; border-left:5px solid {ORANGE}; padding:10px 14px;
        border-radius:8px; margin:6px 0; color:{BLACK}; }}
.good {{ background:#EAF7EE; border-left:5px solid {GREEN}; padding:10px 14px;
        border-radius:8px; margin:6px 0; color:{BLACK}; }}
</style>
<div class="hero"><h1>📊 AI and Financial Reporting in Nigerian Deposit Money Banks</h1>
<p>Interactive survey dashboard: accuracy, timeliness, reliability, challenges and compliance</p></div>
""", unsafe_allow_html=True)


def kpi(col, label, value, style=""):
    col.markdown(f'<div class="kpi {style}"><div class="l">{label}</div>'
                 f'<div class="v">{value}</div></div>', unsafe_allow_html=True)


def style_alt(chart, height=320):
    return (chart.properties(height=height)
            .configure_axis(labelColor=BLACK, titleColor=BLACK, gridColor="#EEEEEE")
            .configure_legend(labelColor=BLACK, titleColor=BLACK)
            .configure_view(strokeWidth=0))


# ---------------------------------------------------------------- SIDEBAR
st.sidebar.success("Survey data is built in. Nothing to upload.")
full, items_full, questions = load_data()

st.sidebar.header("🔎 Filter Data")
mask = pd.Series(True, index=full.index)
for d in DEMOS:
    opts = sorted(full[d].unique())
    pick = st.sidebar.multiselect(d, opts, default=opts)
    mask &= full[d].isin(pick)
data, items = full[mask], items_full[mask]
if data.empty:
    st.warning("No respondents match these filters. Select more options in the sidebar.")
    st.stop()

st.sidebar.download_button("⬇️ Download filtered CSV", data.to_csv(index=False).encode(),
                           "filtered_survey.csv", "text/csv")

CONSTRUCTS = list(GROUPS)
means = data[CONSTRUCTS].mean()
agree_pct = {c: (items[[f"{c} Q{n}" for n in range(1, 6)]].stack() >= 4).mean() * 100
             for c in CONSTRUCTS}

# ---------------------------------------------------------------- KPIs
benefit = data[["Accuracy", "Timeliness", "Reliability", "Compliance"]].mean(axis=1).mean()
k1, k2, k3, k4 = st.columns(4)
kpi(k1, "Respondents", f"{len(data)}")
kpi(k2, "Overall AI benefit score", f"{benefit:.2f} / 5", "orange")
kpi(k3, "Highest rated area", means.idxmax(), "")
kpi(k4, "Lowest rated area", means.idxmin(), "black")
st.write("")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ["📈 Overview", "📊 Distributions", "🔗 Correlations", "🧩 Question level",
     "🧪 Reliability", "🗂️ Data & Profile"])

# ---------------------------------------------------------------- TAB 1
with tab1:
    c1, c2 = st.columns(2)
    mdf = means.rename("Mean").reset_index().rename(columns={"index": "Construct"})
    bars = alt.Chart(mdf).mark_bar(cornerRadiusTopRight=8, cornerRadiusBottomRight=8).encode(
        x=alt.X("Mean:Q", scale=alt.Scale(domain=[1, 5]), title="Mean score (1-5)"),
        y=alt.Y("Construct:N", sort="-x", title=None),
        color=alt.Color("Mean:Q", scale=alt.Scale(range=[ORANGE, GREEN]), legend=None),
        tooltip=["Construct", alt.Tooltip("Mean:Q", format=".2f")])
    labels = bars.mark_text(align="left", dx=5, color=BLACK, fontWeight="bold").encode(
        text=alt.Text("Mean:Q", format=".2f"))
    with c1:
        st.subheader("Average score per construct")
        st.altair_chart(style_alt(bars + labels), use_container_width=True)

    long = []
    for c in CONSTRUCTS:
        vals = items[[f"{c} Q{n}" for n in range(1, 6)]].stack().astype(int)
        cnt = vals.value_counts(normalize=True).reindex(range(1, 6), fill_value=0) * 100
        for lvl, p in zip(LIKERT_ORDER, cnt):
            long.append({"Construct": c, "Response": lvl, "Percent": p})
    long = pd.DataFrame(long)
    stacked = alt.Chart(long).mark_bar().encode(
        y=alt.Y("Construct:N", title=None, sort=CONSTRUCTS),
        x=alt.X("Percent:Q", stack="normalize", title="Share of responses",
                axis=alt.Axis(format="%")),
        color=alt.Color("Response:N", sort=LIKERT_ORDER,
                        scale=alt.Scale(domain=LIKERT_ORDER, range=LIKERT_COLORS)),
        order=alt.Order("Response:N"),
        tooltip=["Construct", "Response", alt.Tooltip("Percent:Q", format=".1f")])
    with c2:
        st.subheader("How people responded")
        st.altair_chart(style_alt(stacked), use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        st.subheader("Radar profile")
        fig = go.Figure()
        for i, (lab, grp) in enumerate(data.groupby("Gender")):
            m = grp[CONSTRUCTS].mean()
            fig.add_trace(go.Scatterpolar(
                r=list(m) + [m.iloc[0]], theta=CONSTRUCTS + [CONSTRUCTS[0]],
                fill="toself", name=lab, line_color=PALETTE[i % 5], opacity=.65))
        fig.update_layout(polar=dict(radialaxis=dict(range=[1, 5])), height=360,
                          margin=dict(t=20, b=20), paper_bgcolor=WHITE,
                          legend=dict(orientation="h"))
        st.plotly_chart(fig, use_container_width=True)
    with c4:
        st.subheader("Compare groups")
        demo_pick = st.selectbox("Group by", DEMOS, key="grp_by")
        g = (data.groupby(demo_pick)[CONSTRUCTS].mean().reset_index()
             .melt(id_vars=demo_pick, var_name="Construct", value_name="Mean"))
        grouped = alt.Chart(g).mark_bar(cornerRadiusTopLeft=4, cornerRadiusTopRight=4).encode(
            x=alt.X("Construct:N", title=None, sort=CONSTRUCTS),
            xOffset=alt.XOffset(f"{demo_pick}:N"),
            y=alt.Y("Mean:Q", scale=alt.Scale(domain=[1, 5])),
            color=alt.Color(f"{demo_pick}:N", scale=alt.Scale(range=PALETTE)),
            tooltip=[demo_pick, "Construct", alt.Tooltip("Mean:Q", format=".2f")])
        st.altair_chart(style_alt(grouped, 330), use_container_width=True)

# ---------------------------------------------------------------- TAB 2
with tab2:
    pick = st.selectbox("Choose a construct", CONSTRUCTS, key="dist_pick")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader(f"Histogram: {pick}")
        hist = alt.Chart(data.dropna(subset=[pick])).mark_bar(
            color=GREEN, stroke=WHITE, cornerRadiusTopLeft=4, cornerRadiusTopRight=4).encode(
            x=alt.X(f"{pick}:Q", bin=alt.Bin(maxbins=10), title=f"{pick} score"),
            y=alt.Y("count()", title="Respondents"),
            tooltip=["count()"])
        rule = alt.Chart(pd.DataFrame({"m": [data[pick].mean()]})).mark_rule(
            color=ORANGE, strokeWidth=3, strokeDash=[6, 4]).encode(x="m:Q")
        st.altair_chart(style_alt(hist + rule), use_container_width=True)
        st.caption("Orange dashed line = mean")
    with c2:
        st.subheader(f"Box plot by group: {pick}")
        by = st.selectbox("Split by", DEMOS, key="box_by")
        fig = px.box(data, x=by, y=pick, color=by, points="all",
                     color_discrete_sequence=PALETTE)
        fig.update_layout(height=360, showlegend=False, paper_bgcolor=WHITE,
                          plot_bgcolor=WHITE, margin=dict(t=20))
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Who answered the survey?")
    cols = st.columns(4)
    for col, d in zip(cols, DEMOS):
        counts = data[d].value_counts().reset_index()
        counts.columns = [d, "Count"]
        fig = px.pie(counts, names=d, values="Count", hole=.55, title=d,
                     color_discrete_sequence=PALETTE)
        fig.update_layout(height=290, margin=dict(t=40, b=0, l=0, r=0),
                          legend=dict(orientation="h", y=-0.1), paper_bgcolor=WHITE)
        col.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------- TAB 3
with tab3:
    method = st.radio("Correlation method", ["pearson", "spearman"], horizontal=True)
    corr = data[CONSTRUCTS].corr(method=method)
    c1, c2 = st.columns([1.1, 1])
    with c1:
        st.subheader("Correlation heatmap")
        fig, ax = plt.subplots(figsize=(6.2, 5))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap=GREEN_ORANGE, vmin=-1, vmax=1,
                    linewidths=2, linecolor=WHITE, square=True,
                    cbar_kws={"shrink": .8}, annot_kws={"fontsize": 11, "color": BLACK}, ax=ax)
        ax.set_title(f"{method.title()} correlation between constructs", color=BLACK)
        plt.xticks(rotation=35, ha="right")
        st.pyplot(fig)
        plt.close(fig)
    with c2:
        st.subheader("Scatter + trend line")
        xa = st.selectbox("X axis", CONSTRUCTS, index=0, key="sx")
        ya = st.selectbox("Y axis", CONSTRUCTS, index=1, key="sy")
        sdf = data.dropna(subset=[xa, ya]).copy()
        sdf["jx"] = sdf[xa] + np.random.default_rng(1).normal(0, .03, len(sdf))
        sdf["jy"] = sdf[ya] + np.random.default_rng(2).normal(0, .03, len(sdf))
        pts = alt.Chart(sdf).mark_circle(size=90, color=ORANGE, opacity=.65,
                                         stroke=BLACK, strokeWidth=.5).encode(
            x=alt.X("jx:Q", title=xa, scale=alt.Scale(domain=[1, 5.2])),
            y=alt.Y("jy:Q", title=ya, scale=alt.Scale(domain=[1, 5.2])),
            tooltip=["Gender", "Age", xa, ya])
        line = pts.transform_regression("jx", "jy").mark_line(color=GREEN, strokeWidth=4)
        st.altair_chart(style_alt(pts + line, 360), use_container_width=True)
        r = sdf[xa].corr(sdf[ya])
        strength = "strong" if abs(r) >= .6 else "moderate" if abs(r) >= .3 else "weak"
        st.markdown(f'<div class="good"><b>r = {r:.2f}</b> ({strength} '
                    f'{"positive" if r >= 0 else "negative"} relationship)</div>',
                    unsafe_allow_html=True)

# ---------------------------------------------------------------- TAB 4
with tab4:
    pick = st.selectbox("Construct", CONSTRUCTS, key="q_pick")
    rows = []
    for n in range(1, 6):
        key = f"{pick} Q{n}"
        vc = items[key].dropna().astype(int).value_counts(normalize=True)
        vc = vc.reindex(range(1, 6), fill_value=0) * 100
        for lvl, p in zip(LIKERT_ORDER, vc):
            rows.append({"Question": f"Q{n}: {questions[key][:70]}", "Response": lvl, "Percent": p})
    qdf = pd.DataFrame(rows)
    fig = px.bar(qdf, y="Question", x="Percent", color="Response", orientation="h",
                 category_orders={"Response": LIKERT_ORDER},
                 color_discrete_map=dict(zip(LIKERT_ORDER, LIKERT_COLORS)))
    fig.update_layout(barmode="stack", height=440, paper_bgcolor=WHITE, plot_bgcolor=WHITE,
                      yaxis=dict(autorange="reversed", title=None),
                      xaxis=dict(title="% of respondents"), legend=dict(orientation="h", y=-0.2))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Mean score for every question")
    qm = items.mean().rename("Mean").reset_index().rename(columns={"index": "Item"})
    qm["Construct"] = qm["Item"].str.split(" Q").str[0]
    qm["Question"] = qm["Item"].map(questions)
    qchart = alt.Chart(qm).mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3).encode(
        x=alt.X("Item:N", sort=None, title=None, axis=alt.Axis(labelAngle=-60)),
        y=alt.Y("Mean:Q", scale=alt.Scale(domain=[1, 5])),
        color=alt.Color("Construct:N", scale=alt.Scale(range=PALETTE)),
        tooltip=["Item", "Question", alt.Tooltip("Mean:Q", format=".2f")])
    st.altair_chart(style_alt(qchart, 340), use_container_width=True)

# ---------------------------------------------------------------- TAB 5
with tab5:
    st.subheader("Cronbach's alpha (scale reliability)")
    ar = pd.DataFrame({
        "Construct": CONSTRUCTS,
        "Alpha": [cronbach_alpha(items[[f"{c} Q{n}" for n in range(1, 6)]]) for c in CONSTRUCTS],
        "Mean": [means[c] for c in CONSTRUCTS],
        "Std dev": [data[c].std() for c in CONSTRUCTS],
        "% Agree / Strongly agree": [agree_pct[c] for c in CONSTRUCTS]})
    ar["Interpretation"] = ar["Alpha"].map(alpha_label)
    c1, c2 = st.columns([1.2, 1])
    with c1:
        st.dataframe(ar.style.format({"Alpha": "{:.3f}", "Mean": "{:.2f}", "Std dev": "{:.2f}",
                                      "% Agree / Strongly agree": "{:.1f}%"}),
                     use_container_width=True, hide_index=True)
        st.caption("Rule of thumb: 0.7 or higher is acceptable for survey scales.")
    with c2:
        ach = alt.Chart(ar).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
            x=alt.X("Construct:N", sort=CONSTRUCTS, title=None),
            y=alt.Y("Alpha:Q", scale=alt.Scale(domain=[0, 1])),
            color=alt.Color("Alpha:Q", scale=alt.Scale(range=[ORANGE, GREEN]), legend=None),
            tooltip=["Construct", alt.Tooltip("Alpha:Q", format=".3f")])
        thr = alt.Chart(pd.DataFrame({"t": [0.7]})).mark_rule(
            color=BLACK, strokeDash=[6, 4], strokeWidth=2).encode(y="t:Q")
        st.altair_chart(style_alt(ach + thr, 300), use_container_width=True)

    best, worst = ar.loc[ar["Mean"].idxmax()], ar.loc[ar["Mean"].idxmin()]
    st.markdown(f'<div class="good"><b>Key finding:</b> respondents rate <b>{best["Construct"]}</b> '
                f'highest (mean {best["Mean"]:.2f}, {best["% Agree / Strongly agree"]:.0f}% agree).</div>'
                f'<div class="note"><b>Lowest area:</b> <b>{worst["Construct"]}</b> '
                f'(mean {worst["Mean"]:.2f}, {worst["% Agree / Strongly agree"]:.0f}% agree).</div>',
                unsafe_allow_html=True)

# ---------------------------------------------------------------- TAB 6
with tab6:
    st.subheader("Filtered data")
    st.dataframe(data.round(2), use_container_width=True, hide_index=True)
    st.subheader("Summary statistics")
    st.dataframe(data[CONSTRUCTS].describe().round(2).T, use_container_width=True)
    st.subheader("Missing values")
    miss = data.isna().sum().rename("Missing").to_frame()
    st.dataframe(miss[miss["Missing"] > 0] if miss["Missing"].sum() else
                 pd.DataFrame({"Missing": ["None"]}), use_container_width=True)

    if st.checkbox("Generate full data profiling report (slow, optional)"):
        try:
            from ydata_profiling import ProfileReport
            import streamlit.components.v1 as components
            with st.spinner("Building report..."):
                rep = ProfileReport(data, minimal=True, title="Survey Profile")
                components.html(rep.to_html(), height=800, scrolling=True)
        except Exception as e:
            st.error("ydata-profiling is not installed or not supported on this Python version. "
                     "Run: pip install ydata-profiling")
            st.caption(str(e))

st.caption("Built with Streamlit, Altair, Plotly, Seaborn and Matplotlib.")