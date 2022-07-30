import streamlit as st
import phonenumbers
from phonenumbers import timezone,geocoder,carrier


st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )

st.title("Mobile Info")


number = st.text_input("Enter Mobile Number with +91:")

try:
    mobile = phonenumbers.parse(number)
    time = timezone.time_zones_for_number(mobile)
    cr = carrier.name_for_number(mobile,"en")
    reg = geocoder.description_for_number(mobile,"en")
except Exception as e:
    st.error("Enter the number:")
    

try:
    if st.button("Get Info"):
        st.text(f"{mobile}")
        st.text(f"Time Zone: {time}")
        st.text(f"Carrier: {cr}")
        st.text(f"Region: {reg}")
except Exception as e:
    st.error("First Enter your number \U0001F601 ")


