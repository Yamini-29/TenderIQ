import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/evaluate"

st.set_page_config(page_title="TenderIQ", layout="wide")

st.title("📊 TenderIQ - AI Tender Evaluation System")

st.markdown("""
### 🧠 Features:
- AI-based criteria extraction  
- Explainable decision-making  
- Confidence-aware evaluation  
- Human-in-the-loop ready  
""")

# --- INPUT SECTION ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Tender Document")
    tender_text = st.text_area(
        "Paste Tender Text",
        height=200,
        placeholder="Enter tender criteria..."
    )

with col2:
    st.subheader("🏢 Bidder Document")
    bidder_text = st.text_area(
        "Paste Bidder Details",
        height=200,
        placeholder="Enter bidder information..."
    )

# --- BUTTON ---
if st.button("🚀 Evaluate Bidder"):

    if not tender_text or not bidder_text:
        st.warning("Please enter both tender and bidder text.")
    else:
        with st.spinner("Analyzing documents..."):

            try:
                response = requests.post(
                    API_URL,
                    params={
                        "tender_text": tender_text,
                        "bidder_text": bidder_text
                    }
                )

                data = response.json()

            except:
                st.error("⚠️ Backend error or invalid response")
                st.stop()

        st.success("Evaluation Complete!")

        # --- CRITERIA ---
        st.subheader("📋 Extracted Criteria")
        for c in data["criteria"]:
            st.markdown(f"• **{c['criterion']}** ({c['type']})")

        # --- RESULTS ---
        st.subheader("📊 Evaluation Results")

        for res in data["evaluation"]:

            if res["decision"] == "Eligible":
                st.success(f"✅ {res['criterion']}")
            elif res["decision"] == "Not Eligible":
                st.error(f"❌ {res['criterion']}")
            else:
                st.warning(f"⚠️ {res['criterion']}")

            st.markdown(f"**Decision:** `{res['decision']}`")
            st.markdown(f"**Confidence:** `{res['confidence']}`")
            st.markdown(f"**Reason:** {res['explanation']['reason']}")

            if res["decision"] == "Needs Review":
                st.info("👤 Requires human verification")

            st.markdown("---")

        # --- RAW OUTPUT (CORRECTLY PLACED) ---
        with st.expander("🔍 View Raw AI Output"):
            st.json(data)