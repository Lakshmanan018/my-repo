import streamlit as st
import pandas as pd

st.title("💹 BondX – AI Powered Bond Platform")

menu = st.sidebar.radio("Navigate", ["Login", "Marketplace", "Bond Explainer", "Portfolio"])

if menu == "Login":
    st.header("Welcome to BondX")
    st.button("Login with DigiLocker (KYC)")
    st.button("Continue with UPI")
    st.button("Demo Mode")

elif menu == "Marketplace":
    st.header("Bond Marketplace")
    data = {
        "Bond Name": ["Bond A", "Bond B"],
        "Issuer": ["SBI", "Reliance"],
        "Coupon Rate": ["7%", "8%"],
        "Maturity": [2028, 2030],
        "Price (₹)": [1000, 950]
    }
    df = pd.DataFrame(data)
    st.table(df)

elif menu == "Bond Explainer":
    st.header("Ask BondX AI 🤖")
    q = st.text_input("Ask about bonds:")
    if q:
        st.write("AI Answer: Coupon rate is the annual interest a bond pays.")

elif menu == "Portfolio":
    st.header("My Portfolio")
    st.metric("Total Value (₹)", "50,000")
    st.metric("Upcoming Interest (₹)", "1,200")
    st.metric("Number of Bonds", "5")
