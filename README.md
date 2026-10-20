https://artificial-intelligence-in-banking-dashboard-5pqzxfvdbyniappec.streamlit.app/

# 🏦 AI & Financial Reporting in Nigerian Banks: Survey Dashboard

An interactive Streamlit dashboard exploring how Artificial Intelligence is changing financial reporting in Nigerian Deposit Money Banks: its accuracy, timeliness, reliability, compliance, and the challenges standing in the way.

*Proudly done by **Chioma's Art** 🦚🎭🎨*

## 🔗 Quick Links
* **Live Dashboard:** [View the Streamlit App]([https://artificial-intelligence-in-banking-dashboard-5pqzxfvdbyniappec.streamlit.app/
])
* **Dataset:** `filtered_survey.csv` (83 respondents, 9 columns)

---

## 🎯 The Big Question
Banks run on trust, and trust runs on financial reports. So when AI tools started entering Nigerian banks, one question mattered most: **is AI actually making financial reporting better, and what is still holding it back?**

I surveyed **83 banking professionals** using 25 five-point Likert questions (Strongly Disagree to Strongly Agree), grouped into five areas: Accuracy, Timeliness, Reliability, Challenges and Compliance.

## 📊 What the Dashboard Shows
| Tab | What you get |
|---|---|
| 📈 Overview | KPI cards, average score per area, response breakdown, radar profile, group comparison |
| 📊 Distributions | Histograms, box plots, demographic donuts |
| 🔗 Correlations | Heatmap (Pearson / Spearman) and scatter plots with trend lines |
| 🧩 Question level | Every question's response split and mean score |
| 🧪 Reliability | Cronbach's alpha for each scale, with auto-generated key findings |
| 🗂️ Data & Profile | Filtered data table, summary stats, CSV download, optional profiling report |

Sidebar slicers (gender, age, marital status, education) update every chart live.

## 🔍 Key Findings
| Area | Avg score (1-5) | % Agree | Cronbach's α |
|---|---|---|---|
| ⏱️ Timeliness | 4.13 | 82.1% | 0.84 |
| 🚧 Challenges | 4.12 | 83.0% | 0.71 |
| 🎯 Accuracy | 4.07 | 80.2% | 0.85 |
| 🔒 Reliability | 3.88 | 75.3% | 0.82 |
| 📜 Compliance | 3.88 | 72.3% | 0.87 |

* **Speed is AI's biggest win.** "AI helps generate reports faster than manual methods" was the highest-scoring question of all (4.45).
* **Trust and compliance lag behind.** The lowest-scoring question was whether AI produces information that faithfully represents economic events (3.67). IFRS 9 compliance (3.82) and tracking regulatory changes (3.83) are also near the bottom.
* **The barriers are real.** 83% of respondents agree there are serious challenges: poor data quality and legacy systems (86.7%), skills gaps (84.3%), cybersecurity and privacy (83.1%), unclear regulatory guidance (80.7%), high cost (75.9%).
* **Reliability and Compliance move together** (Spearman correlation 0.77), and so do Accuracy and Timeliness (0.70). Fix one and the other tends to follow.
* All five scales passed the reliability check (α of 0.71 or higher).
* Male respondents scored slightly higher in every area (differences not significance-tested).

## 💡 What Banks Should Do Next
1. **Keep a human in the loop for reliability.** Pair AI outputs with accountant and auditor review, and keep digital audit trails, so AI-produced statements can be verified and trusted.
2. **Treat compliance as a built-in feature.** Use AI to monitor regulatory changes (CBN, FRCN, IFRS 9) and flag reporting gaps before submission, not after.
3. **Fix the data foundation first.** Poor data quality and fragmented legacy systems were the #1 barrier. Clean, connected data comes before fancier models.
4. **Close the skills gap.** Train finance staff in AI literacy and data skills, and train IT staff in accounting basics, so both sides speak the same language.
5. **Lock down cybersecurity and data privacy** before scaling AI across reporting.
6. **Start small, prove it, then scale.** Pilot AI on one reporting process (such as month-end close), measure the results, then expand. This also softens the cost barrier.
7. **Push for clearer regulatory guidance.** Banks and regulators should work together on AI-in-reporting standards so nobody is guessing.
8. **Measure the impact.** Track close time, error rates, restatements and regulatory filing timeliness before and after AI adoption.

## 🗂️ Dataset
`filtered_survey.csv`: one row per respondent.

| Column | Description |
|---|---|
| Gender, Age, Marital status, Education | Respondent profile |
| Accuracy, Timeliness, Reliability, Challenges, Compliance | Average of 5 Likert questions (1 = Strongly Disagree, 5 = Strongly Agree) |

## 🚀 Run It Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
No upload needed, because the survey data is built into `app.py`.

## 🛠️ Built With
Python · Streamlit · Pandas · Altair · Plotly · Seaborn · Matplotlib

## ⚠️ Limitations
* Based on **perceptions** of 83 respondents, not measured bank performance data.
* The sample skews young (73.5% aged 18-25), single (85.5%) and HND/BSc-educated (73.5%), so it reflects mostly early-career voices.
* Findings are descriptive and show associations, not proof of cause and effect.

## 🔮 What's Next
* What-if simulator with interactive sliders
* Larger sample including senior management and auditors
* Regression analysis to find what drives compliance and reliability

---
*Proudly done by **Chioma's Art** 🦚🎭🎨*
Thank you.
