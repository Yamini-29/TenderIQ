import streamlit as st
import requests
import tempfile
import os
from services.agents.ocr_agent import run_ocr_agent

API_URL = "http://127.0.0.1:8000/evaluate"

st.set_page_config(page_title="TenderIQ", layout="wide")

st.title("📊 TenderIQ - AI Procurement Copilot")

# -------------------------------
# 🧠 OVERALL RESULT FUNCTION
# -------------------------------

def compute_overall_result(evaluation):
    decisions = [item["decision"] for item in evaluation]

    if "Not Eligible" in decisions:
        return "❌ Not Eligible"
    elif "Needs Review" in decisions:
        return "⚠️ Needs Review"
    else:
        return "✅ Eligible"


# -------------------------------
# FILE UPLOAD
# -------------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Upload Tender Document")
    tender_file = st.file_uploader(
        "Upload Tender",
        type=["pdf", "png", "jpg", "jpeg", "txt"]
    )

with col2:
    st.subheader("🏢 Upload Bidder Document")
    bidder_file = st.file_uploader(
        "Upload Bidder",
        type=["pdf", "png", "jpg", "jpeg", "txt"]
    )


# -------------------------------
# FILE PROCESSING
# -------------------------------

def process_file(uploaded_file):
    if uploaded_file is None:
        return ""

    ext = os.path.splitext(uploaded_file.name)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    return run_ocr_agent(temp_path)


# -------------------------------
# EVALUATE BUTTON
# -------------------------------

if st.button("🚀 Evaluate"):

    if not tender_file or not bidder_file:
        st.warning("Please upload both documents.")
        st.stop()

    with st.spinner("Processing..."):

        tender_text = process_file(tender_file)
        bidder_text = process_file(bidder_file)

        if len(tender_text.strip()) < 10 or len(bidder_text.strip()) < 10:
            st.error("❌ Failed to extract meaningful text.")
            st.stop()

        try:
            response = requests.post(
                API_URL,
                params={
                    "tender_text": tender_text,
                    "bidder_text": bidder_text
                }
            )

            if response.status_code != 200:
                st.error(response.text)
                st.stop()

            data = response.json()

        except Exception as e:
            st.error(f"Backend error: {str(e)}")
            st.stop()

    st.success("✅ Evaluation Complete!")

    # -------------------------------
    # 🏁 OVERALL RESULT (TOP PRIORITY)
    # -------------------------------

    overall = compute_overall_result(data["evaluation"])

    st.markdown("---")
    st.markdown("## 🏁 Overall Result")

    if "Eligible" in overall:
        st.success(overall)
    elif "Not Eligible" in overall:
        st.error(overall)
    else:
        st.warning(overall)

    st.markdown("---")

    # -------------------------------
    # EXTRACTED TEXT
    # -------------------------------

    with st.expander("🧾 Tender Text"):
        st.text(tender_text[:1500])

    with st.expander("🧾 Bidder Text"):
        st.text(bidder_text[:1500])

    # -------------------------------
    # CRITERIA
    # -------------------------------

    st.subheader("📋 Extracted Criteria")

    for c in data.get("criteria", []):
        st.markdown(f"• **{c.get('criterion')}** ({c.get('type')})")

    # -------------------------------
    # RESULTS + WOW FEATURE
    # -------------------------------

    st.subheader("📊 Evaluation Details")

    for res in data.get("evaluation", []):

        decision = res.get("decision")

        if decision == "Eligible":
            st.success(f"✅ {res['criterion']}")
        elif decision == "Not Eligible":
            st.error(f"❌ {res['criterion']}")
        else:
            st.warning(f"⚠️ {res['criterion']}")

        st.markdown(f"**Decision:** `{decision}`")

        explanation = res.get("explanation", {})

        # 🔥 WOW FEATURE (Evidence Panel)
        with st.expander("🔍 View Evidence"):
            st.markdown(f"**Extracted Value:** {explanation.get('value')}")
            st.markdown(f"**Required:** {explanation.get('required')}")
            st.markdown(f"**Reason:** {explanation.get('reason')}")
            st.markdown(f"**Confidence:** {res.get('confidence', 0)}")

        st.markdown("---")

    # -------------------------------
    # RISK SUMMARY
    # -------------------------------

    st.subheader("⚠️ Risk Summary")

    evaluations = data.get("evaluation", [])

    needs_review = sum(1 for r in evaluations if r["decision"] == "Needs Review")
    avg_conf = sum(r.get("confidence", 0) for r in evaluations) / len(evaluations)

    if needs_review > 0:
        st.warning(f"{needs_review} criteria require manual review")
    else:
        st.success("All criteria evaluated confidently")

    st.markdown(f"**Overall Confidence Score:** `{round(avg_conf, 2)}`")

    # -------------------------------
    # RAW OUTPUT
    # -------------------------------

    with st.expander("🔍 Raw Output"):
        st.json(data)