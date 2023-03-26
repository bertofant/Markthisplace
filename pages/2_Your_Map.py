import streamlit as st
import myauthenticator as stauth
import sqlfunctions
from Home import formRegistrazione, authenticator

# initialize session state
if 'config' not in st.session_state:
    config = sqlfunctions.getconfigfromsql()
    st.session_state['config'] = config
else:
    config = st.session_state['config']

if 'register_expanded' not in st.session_state:
    st.session_state['register_expanded'] = False

if 'show_register_success' not in st.session_state:
    st.session_state['show_register_success'] = False


# with open('./users.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)


if st.session_state['authentication_status']:
    st.header('This is the map page for a registered user')
    authenticator.logout('Logout','sidebar')
else:
    if st.session_state['show_register_success']:
        st.success('Utente registrato con successo. Effettua il login')
        st.session_state['show_register_success'] = False
        st.session_state['authentication_status'] = None
    name, authentication_status, username = authenticator.login('Login','main')
    if authentication_status==False:
        st.error('Email o password non corretti')
        formRegistrazione()
    elif authentication_status==None:
        formRegistrazione()

st.write(st.session_state)
