import streamlit as st
from datetime import date

st.set_page_config(page_title="Loan Details", layout="wide")

st.title("Loan Details")
st.write("Tell us about the loan you are applying for.")

# Sidebar like chatbot placeholder
with st.sidebar:
    st.header("Your Loan Companion 🤖")
    st.write(
        "Hi there! I'm here to help you with your loan application. Feel free to ask any questions!"
    )
    st.info("This is a placeholder for a live chatbot interface.")

# Form state initialization
if "formData" not in st.session_state:
    st.session_state.formData = {
        "loanType": "",
        "requiredLoanAmount": "",
        "loanDuration": "",
        "hasExistingLoan": "no",
        "preferredEmiDate": "",
        "attachments": {
            "saleAgreement": None,
            "ec": None,
            "dealerInvoice": None,
            "quotation": None,
            "admissionLetter": None,
            "feeStructure": None,
        },
    }

formData = st.session_state.formData

# Tabs
loan_tab, attach_tab = st.tabs(["Loan Details", "Attachments"])

# Loan Details Tab
with loan_tab:
    st.subheader("Your Loan Request")
    col1, col2 = st.columns(2)

    with col1:
        formData["loanType"] = st.selectbox(
            "Loan Type",
            ["", "Home Loan", "Vehicle Loan", "Education Loan", "Personal Loan"],
            index=["", "Home Loan", "Vehicle Loan", "Education Loan", "Personal Loan"].index(formData["loanType"])
        )

    with col2:
        formData["requiredLoanAmount"] = st.number_input(
            "Required Loan Amount ($)", min_value=0, value=int(formData["requiredLoanAmount"] or 0)
        )

    col3, col4 = st.columns(2)

    with col3:
        formData["loanDuration"] = st.number_input(
            "Loan Duration (Years)", min_value=0, value=int(formData["loanDuration"] or 0)
        )

    with col4:
        formData["preferredEmiDate"] = st.selectbox(
            "Preferred EMI Date", [""] + [str(i) for i in range(1, 29)], index=(formData["preferredEmiDate"] and int(formData["preferredEmiDate"])) or 0
        )

    st.write("### Do you have any existing loans?")
    formData["hasExistingLoan"] = st.radio(
        "", ["yes", "no"], index=["yes", "no"].index(formData["hasExistingLoan"]) 
    )

# Attachments Tab
with attach_tab:
    st.subheader("Required Attachments")
    st.write("Please upload the documents specific to your loan type.")

    loanType = formData["loanType"]
    requiredAttachments = []

    if loanType == "Home Loan":
        requiredAttachments = [
            ("saleAgreement", "Sale Agreement"),
            ("ec", "Encumbrance Certificate (EC)")
        ]
    elif loanType == "Vehicle Loan":
        requiredAttachments = [
            ("dealerInvoice", "Dealer Invoice"),
            ("quotation", "Quotation")
        ]
    elif loanType == "Education Loan":
        requiredAttachments = [
            ("admissionLetter", "Admission Letter"),
            ("feeStructure", "Fee Structure")
        ]

    if not requiredAttachments:
        st.info("Please select a Loan Type to see required documents.")
    else:
        for key, label in requiredAttachments:
            uploaded = st.file_uploader(label, key=key)
            if uploaded:
                formData["attachments"][key] = uploaded

# Submit Button
if st.button("Submit Loan Details"):
    st.success("Loan Details Submitted Successfully!")
    st.json(formData)
