import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Recruix AI - ATS", page_icon="⚡", layout="wide")

# Sidebar Navigation
st.sidebar.title("⚡ Recruix AI")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "Navigation", 
    ["Dashboard", "AI Candidate Matching", "GCC Visa & Quotas", "Approvals"]
)

if menu == "Dashboard":
    st.title("Recruitment Overview")
    st.markdown("Al-Powered Talent Acquisition, Born in GCC")
    
    # Key Metrics (Top row)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Active Jobs", value="12", delta="+2 this week")
    with col2:
        st.metric(label="Candidates Managed", value="1,402", delta="+120 this week")
    with col3:
        st.metric(label="Visa Quota Alerts", value="3 Expiring", delta="Critical", delta_color="inverse")

    st.markdown("---")

    # AI Auto-Ranking Table
    st.subheader("Top AI-Ranked Candidates")
    
    # Mock Data for Candidates
    data = {
        "Candidate Name": ["Ahmed Hassan", "Sarah Malik", "John Doe", "Fatima Al Fasi", "Tariq Ali"],
        "Applied Role": ["Procurement Executive", "HR Manager", "Software Engineer", "Marketing Lead", "Finance Officer"],
        "AI Match Score": [97, 94, 88, 85, 78],
        "Status": ["Auto-Screened", "Interview Scheduled", "Pending", "Reviewed", "Rejected"]
    }
    df = pd.DataFrame(data)
    
    # Formatting the table inside Streamlit
    st.dataframe(
        df.style.background_gradient(subset=['AI Match Score'], cmap='Greens'),
        use_container_width=True,
        hide_index=True
    )

elif menu == "GCC Visa & Quotas":
    st.title("GCC Visa & Compliance Management")
    st.warning("⚠️ 3 Employee Visas expiring within the next 30 days.")
    
    st.subheader("Emiratization / Saudization Status")
    st.progress(65)
    st.caption("Current Quota Fulfillment: 65% (Target: 70%)")
    
    # Mock Visa Data
    visa_data = {
        "Employee": ["Mohammed Khan", "Arun Silva", "Jane Smith"],
        "Entity": ["Pioneer Cement Industries", "Group Company A", "Business Unit 2"],
        "Expiry Date": ["2026-05-15", "2026-05-20", "2026-06-02"],
        "Status": ["Critical", "Pending Renewal", "Valid"]
    }
    st.table(pd.DataFrame(visa_data))

elif menu == "AI Candidate Matching":
    st.title("Smart Parsing & Semantic Matching")
    st.info("Upload candidate resumes (PDF/DOCX) to automatically extract data and rank them against active jobs.")
    
    uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
    
    if uploaded_file is not None:
        st.success(f"Successfully processed {uploaded_file.name} using Recruix AI Brain!")
        st.write("Extracted Skills: **Supply Chain, Negotiation, SAP, Logistics**")
        st.metric(label="Match to Procurement Executive Role", value="96%")

elif menu == "Approvals":
    st.title("Workflow Engine")
    st.write("Pending Approvals from Hiring Managers will appear here.")
