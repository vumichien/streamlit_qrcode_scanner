from src.streamlit_qrcode_scanner import qrcode_scanner
import streamlit as st
import validators


def nav_to(url):
    # nav_script = """
    #     <meta http-equiv="refresh" content="0; url='%s'">
    # """ % url
    # st.write(nav_script, unsafe_allow_html=True)
    nav_script = f"""
            <script>
                window.location.href = '{url}';
            </script>
        """
    st.markdown(nav_script, unsafe_allow_html=True)


def main():
    st.write("## QR Code Scanner")

    qr_code = qrcode_scanner(key='qrcode_scanner')

    if qr_code:
        # st.info(f"QR Code detected: {qr_code}")
        # st.write(qr_code)

        if validators.url(str(qr_code)):
            # link = f"[Click here to go to the URL]({qr_code})"
            # st.markdown(link, unsafe_allow_html=True)
            st.link_button("URL link", qr_code, type="secondary")
        else:
            st.error(f"Invalid URL : {qr_code}")


if __name__ == "__main__":
    main()
