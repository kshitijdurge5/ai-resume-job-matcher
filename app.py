import re
import streamlit as st
from portfolio_visuals import render_visuals
def extract_terms(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z][a-zA-Z+#.]{1,}", text.lower()))

def compare_resume(resume: str, job: str) -> dict:
    r, j = extract_terms(resume), extract_terms(job)
    matched = sorted(r & j)
    missing = sorted(j - r)
    return {"matched_terms": matched, "terms_to_review": missing, "note": "Keyword overlap is a rough aid, not a hiring score. Add only skills you can substantiate."}

st.set_page_config(page_title="Resume Job Matcher", page_icon="ðŸ“„")
render_visuals('07_resume_job_matcher')
st.title("Resume & Job Matcher")
resume = st.text_area("Paste resume text")
job = st.text_area("Paste job description")
if st.button("Compare"):
    if not resume.strip() or not job.strip():
        st.warning("Paste both texts.")
    else:
        r = compare_resume(resume, job)
        st.write("**Terms appearing in both**")
        st.write(", ".join(r["matched_terms"]) or "No shared terms detected.")
        st.write("**Job terms to review**")
        st.write(", ".join(r["terms_to_review"]) or "No unmatched terms detected.")
        st.info(r["note"])

