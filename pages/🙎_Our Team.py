import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
st.write("""<h1 style="">Our Team.</h1>""",unsafe_allow_html=True)
selected = option_menu(
    menu_title=None,  # required
    options=["Kartik", "Tanish","Nikhil","Pratham","Mentor"],  # required
    icons=["person","person", "person", "person","person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal"
)
st.markdown('''
            <style>
            .st-emotion-cache-17mvwx7.eczjsme5{
             color:black;
             font-weight:bold;
            }
            </style>
            ''',unsafe_allow_html=True)
if selected == "Kartik":
    st.markdown("""
            <style>
            .st-emotion-cache-1v0mbdj.e115fcil1 img{
                border-radius:20%;
                height:190px;
                object-fit: cover;
            } 
            </style> 
                """,unsafe_allow_html=True)
    col1, col2, col3= st.columns(3)
    with col1:
        img = Image.open("kartik.jpg")
        st.image(img,
             width=200 ,
             channels="RGB",
             )
    with col2:
        img = Image.open("tm.jpg")
        st.image(img,
             width=200 ,
             channels="RGB",
             )
    with col3:
        st.markdown("""
            <style>
                .st-emotion-cache-zt5igj{
                position: relative;
                left: calc(-3rem);
                width: calc(100% + 3rem);
                display: flex;
                -webkit-box-align: center;
                align-items: center;
                overflow: visible;
                margin-right: 45px;
                font-size:28px;
            }
            </style> 
                """,unsafe_allow_html=True)
        st.title("""Kartik Rathod (Leader)
                 The Leader Of The Team""")
    st.title("""EnrollMent:
             210841102050""")
    st.title("""Email: 
                kartikrathod.sd21@gmail.com""")
    st.title("""Contact No: 
                9624280748""")
    st.title("""Github:
             https://github.com/Aku-Davis""")
    
    
if selected == "Pratham":
    st.markdown("""
            <style>
            .st-emotion-cache-1v0mbdj.e115fcil1 img{
                border-radius:20%;
                height:190px;
                object-fit: cover;
            } 
            </style> 
                """,unsafe_allow_html=True)
    col1, col2, col3= st.columns(3)
    with col1:
        img = Image.open("pn1.jpg")
        st.image(img,
             width=200 ,
             channels="RGB",
             )
    with col2:
        img = Image.open("tm.jpg")
        st.image(img,
             width=200 ,
             channels="RGB",
             )
    with col3:
        st.markdown("""
            <style>
                .st-emotion-cache-zt5igj{
                position: relative;
                left: calc(-3rem);
                width: calc(100% + 3rem);
                display: flex;
                -webkit-box-align: center;
                align-items: center;
                overflow: visible;
                margin-right: 45px;
                font-size:28px;
            }
            </style> 
                """,unsafe_allow_html=True)
        st.title("""Pratham Rathod (Team Member)
                 The Member Of Team""")
    st.title("""EnrollMent:
             210841102051""")
    st.title("""Email: 
                prathamrathod.sd21@gmail.com""")
    st.title("""Contact No: 
                 7862805842""")
if selected == "Tanish":
    st.markdown("""
            <style>
            .st-emotion-cache-1v0mbdj.e115fcil1 img{
                border-radius:20%;
                height:190px;
                object-fit: cover;
            } 
            </style> 
                """,unsafe_allow_html=True)
    col1, col2, col3= st.columns(3)
    with col1:
        img = Image.open("tn1.jpg")
        st.image(img,
             width=200 ,
             channels="RGB",
             )
    with col2:
        img = Image.open("tm.jpg")
        st.image(img,
             width=200 ,
             channels="RGB",
             )
    with col3:
        st.markdown("""
            <style>
                .st-emotion-cache-zt5igj{
                position: relative;
                left: calc(-3rem);
                width: calc(100% + 3rem);
                display: flex;
                -webkit-box-align: center;
                align-items: center;
                overflow: visible;
                margin-right: 45px;
                font-size:28px;
            }
            </style> 
                """,unsafe_allow_html=True)
        st.title("""Tanish Kokani (Team Member)
                 The Member Of Team""")
    st.title("""EnrollMent:
             210841102018""")
    st.title("""Email: 
                tanishkonkani.sd21@gmail.com""")
    st.title("""Contact No: 
                8780867785""")
    
if selected == "Nikhil":
    st.markdown("""
            <style>
            .st-emotion-cache-1v0mbdj.e115fcil1 img{
                border-radius:20%;
                height:190px;
                object-fit: cover;
            } 
            </style> 
                """,unsafe_allow_html=True)
    col1, col2, col3= st.columns(3)
    with col1:
        img = Image.open("nik2.jpg")
        st.image(img,
             width=200 ,
             channels="RGB",
             )
    with col2:
        img = Image.open("tm.jpg")
        st.image(img,
             width=200 ,
             channels="RGB",
             )
    with col3:
        st.markdown("""
            <style>
                .st-emotion-cache-zt5igj{
                position: relative;
                left: calc(-3rem);
                width: calc(100% + 3rem);
                display: flex;
                -webkit-box-align: center;
                align-items: center;
                overflow: visible;
                margin-right: 45px;
                font-size:28px;
            }
            </style> 
                """,unsafe_allow_html=True)
        st.title("""Nikhil Nayka (Team Member)
                 The Member Of Team""")
    st.title("""EnrollMent:
             210841102026""")
    st.title("""Email: 
                nikhilnayka.sd21@gmail.com""")
    st.title("""Contact No: 
                8733847211""")   
if selected=="Mentor":
    st.markdown("""
            <style>
            .st-emotion-cache-1v0mbdj.e115fcil1 img{
                border-radius:20%;
                height:190px;
                object-fit: cover;
                margin-left: 230px;
            } 
            </style> 
                """,unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        img = Image.open("sir.jpg")
        st.image(img,
             width=200 ,
             channels="RGB",
             )
    with col2:
        st.markdown("""
            <style>
                .st-emotion-cache-zt5igj{
                position: relative;
                left: calc(-3rem);
                width: calc(100% + 3rem);
                display: flex;
                -webkit-box-align: center;
                align-items: center;
                overflow: visible;
                margin-right: 45px;
                font-size:28px;
            }
            </style> 
                """,unsafe_allow_html=True)
    st.title("""Abdul Aziz Sir(Our Mentor)
                 """)
    st.title("""Linked In Profile:
             https://www.linkedin.com/in/abdul-aziz-md/""")
    st.title("""Contact No: 
                +91 96036 23824""")
footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p style='display: block; color:white; text-align: center; padding-top:10px;  font-weight: bold;' >Made With ❤️ By Kartik (leader) and Team.</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
