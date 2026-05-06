import streamlit as st
import pandas as pd
import time
import random

# Page Configuration
st.set_page_config(page_title="Recruix AI - ATS Platform", page_icon="⚡", layout="wide")

# Custom CSS for better UI
st.markdown("""
    <style>
    .big-font { font-size: 24px !important; font-weight: bold; color: #1E3A8A; }
    .score-high { color: #16A34A; font-weight: bold; font-size: 28px; }
    .score-med { color: #D97706; font-weight: bold; font-size: 28px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("⚡ Recruix AI")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "Navigation", 
    ["Dashboard", "AI CV Screening", "GCC Visa & Quotas"]
)

# ---------------------------------------------------------
# PAGE 1: DASHBOARD
# ---------------------------------------------------------
if menu == "Dashboard":
    st.title("Recruitment Overview")
    st.markdown("The Only GCC-Native, AI-First ATS Platform")
    
    # Key Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Active Jobs", value="12", delta="+2 this week")
    col2.metric(label="Candidates Managed", value="1,402", delta="+120 this week")
    col3.metric(label="Visa Quota Alerts", value="3 Expiring", delta="- Critical", delta_color="inverse")

    st.markdown("---")

    # AI Auto-Ranking Table
    st.subheader("Top AI-Ranked Candidates")
    
    data = {
        "Candidate Name": ["Ahmed Hassan", "Sarah Malik", "John Doe", "Fatima Al Fasi", "Tariq Ali"],
        "Applied Role": ["Procurement Executive", "HR Manager", "Software Engineer", "Marketing Lead", "Finance Officer"],
        "AI Match Score": [97, 94, 88, 85, 78],
        "Status": ["Auto-Screened", "Interview Scheduled", "Pending", "Reviewed", "Rejected"]
    }
    df = pd.DataFrame(data)
    
    # Render table with color gradients for the score
    st.dataframe(
        df.style.background_gradient(subset=['AI Match Score'], cmap='Greens'),
        use_container_width=True,
        hide_index=True
    )

# ---------------------------------------------------------
# PAGE 2: AI CV SCREENING (Smart Parsing & Matching)
# ---------------------------------------------------------
elif menu == "AI CV Screening":
    st.title("🧠 AI Candidate Screening Simulator")
    st.markdown("Test the **Smart Parsing** and **Semantic Matching** capabilities.")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Job Requirements")
        job_req = st.text_area(
            "Enter Target Skills & Requirements:",
            value="Talent Management, Payroll, UAE Labor Law, Employee Relations",
            height=150
        )
        
    with col2:
        st.subheader("2. Candidate CV Content")
        cv_content = st.text_area(
            "Paste Candidate's CV Text here:",
            value="8 years of Human Resources Administration. Handled Compensation and Benefits management. Expert in Dubai Labor Law compliance and full-cycle Recruiting.",
            height=150
        )

    if st.button("🚀 Run AI Analysis", type="primary"):
        with st.spinner('Recruix AI Brain is processing...'):
            # Simulate processing time
            time.sleep(2)
            
            st.markdown("---")
            st.subheader("📊 AI Analysis Results")
            
            res_col1, res_col2, res_col3 = st.columns([1.5, 2, 1])
            
            with res_col1:
                st.markdown("**🔍 Smart Parsing (Extracted from CV)**")
                st.success("✓ HR Administration")
                st.success("✓ Compensation & Benefits")
                st.success("✓ Dubai Labor Law")
                st.success("✓ Recruiting")
                
            with res_col2:
                st.markdown("**🧠 Semantic Matching Engine**")
                st.info("🔄 'HR Administration' ➔ Matches 'Talent Management'")
                st.info("🔄 'Compensation & Benefits' ➔ Matches 'Payroll'")
                st.info("🔄 'Dubai Labor Law' ➔ Matches 'UAE Labor Law'")
                st.info("🔄 'Recruiting' ➔ Matches 'Employee Relations'")
                
            with res_col3:
                st.markdown("**🎯 AI Match Score**")
                # Calculate a mock score based on text length for simulation
                score = random.randint(88, 98)
                st.markdown(f"<div class='score-high'>{score}% Match</div>", unsafe_allow_html=True)
                st.caption("0% Algorithmic Bias")
                
                st.markdown("<br>", unsafe_allow_html=True)
                if score >= 90:
                    st.button("✅ Auto-Schedule Interview", use_container_width=True)
                else:
                    st.button("👀 Review Manually", use_container_width=True)

# ---------------------------------------------------------
# PAGE 3: GCC VISA & QUOTAS
# ---------------------------------------------------------
elif menu == "GCC Visa & Quotas":
    st.title("🏢 GCC Compliance & Visa Management")
    st.markdown("Native support for Multi-Entity Hierarchy and Saudization/Emiratization.")
    
    st.warning("⚠️ 3 Employee Visas expiring within the next 30 days. Action Required!")
    
    st.subheader("Emiratization Status")
    st.progress(0.65)
    st.caption("Current Quota Fulfillment: 65% (Target: 70%) - Group Company Level")
    
    st.markdown("---")
    st.subheader("Expiring Visas Tracking")
    
    visa_data = {
        "Employee Name": ["Mohammed Khan", "Arun Silva", "Jane Smith", "Ali Riaz"],
        "Entity / Dept": ["Pioneer Cement / HR", "Group A / Procurement", "BU 2 / Marketing", "Pioneer Cement / IT"],
        "Visa Expiry Date": ["2026-05-15", "2026-05-20", "2026-06-02", "2026-11-10"],
        "Status": ["🔴 Critical", "🔴 Pending Renewal", "🟢 Valid", "🟢 Valid"]
    }
    st.table(pd.DataFrame(visa_data))
