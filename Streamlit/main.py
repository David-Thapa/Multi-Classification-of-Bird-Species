import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="SimiLo",
    layout="wide",
    initial_sidebar_state="expanded")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
st.markdown("""
<style>
  [data-testid=stSidebar] {
    background-color: ##28a745; /* Change the hex code for your desired green */
    color: white; /* Adjust text color if needed */
  }
  [data-testid=stImage]{
        display: flex;
        justify-content: center; /* Horizontally centers the items */
        align-items: center;
  }
</style>

""", unsafe_allow_html=True)

#Option Menu
with st.sidebar:
    st.image("Bird 1.png")
    selected = option_menu('Avian Species', ["Intro", 'Upload','Result','About'], 
        icons=['play-btn','upload','check-circle','info-circle'],menu_icon='intersect', default_index=0)
   
#Intro
if selected=="Intro":
    #Header
    st.title('Welcome to AvianVision')
    st.subheader('*Your go-to destination for seamless bird identification and exploration*')

    st.divider()

    #Use Cases
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.header('Snap, Upload, Discover')
            st.markdown(
                """
                Your go-to web app for effortless 
                bird identification and detailed 
                bird information at your fingertips! 
                """
                )
            st.divider()

            with st.container():
                col3,col4=st.columns(2)
                with col3:
                    st.header('Snap')
                    st.image('Snap.png', width=150)
                    
                with col4:
                    st.markdown(
                        """
                        <p style= "text-align: justify;">Capture the wonder of winged creatures with AvianVision! Take a quick snap of any bird you spot during your outdoor escapades. No need to be an expert photographer—just capture the moment. Our user-friendly app makes it easy for anyone to become an amateur ornithologist.</p>
                        
                        """,unsafe_allow_html=True
                    )
                st.divider()

                with st.container():
                    col5,col6 = st.columns(2)
                    with col5:
                        st.header('Upload')
                        st.image('Upload.png', width=150)
                
                with col6:
                    st.markdown(
                        """
                        <p style= "text-align: justify;">Simplify birdwatching with AvianVision's straightforward upload process. Just submit your bird photo, and let our intelligent system, powered by advanced CNN technology, swiftly analyze distinctive features, unveiling the identity of the bird in your snapshot.</p>
                        
                        """, unsafe_allow_html=True
                    )
                st.divider()
                
                with st.container():
                    col7,col8 = st.columns(2)
                    with col7:
                        st.header('Discover')
                        st.image('Discover.png', width=150)
                
                with col8:
                    st.markdown(
                        """
                        <p style= "text-align: justify;">Once your photo is uploaded, AvianVision doesn't just stop at identification. Discover fascinating facts about the bird species you've encountered. From habitat details to intriguing behaviors, AvianVision transforms your snapshots into a personalized birdwatching adventure.</p>
                        
                        """,unsafe_allow_html=True
                    )
        
        with col2:
            st.image("Parrot.png", width=400) 

#Upload
if selected=="Upload":
    #Header
    st.title('Upload')
    st.subheader('*Your go-to destination for seamless bird identification and exploration*')

    st.divider()    
    #uploading files
    images = st.file_uploader("pls upload your image",type=['png','jpg','jpeg'],accept_multiple_files=True)
    if images:
        for image in images:
            st.image(image)

#Result
import wikipediaapi

def get_bird_info(bird_name):
    wiki_wiki = wikipediaapi.Wikipedia(user_agent='BirdSpeciesClassification (daybeat06@gmail.com.com)',extract_format=wikipediaapi.ExtractFormat.WIKI)  # Initialize Wikipedia API

    # Retrieve page object for the specified bird name
    page = wiki_wiki.page(bird_name, unquote=True)

    if page.exists():
        # Extract summary and full text content
        summary = page.summary
        # full_text = page.text

        return summary
bird_name = "Rock Dove"
summary = get_bird_info(bird_name)
if selected=='Result':
    st.title('Predicted Result')
    st.subheader('This is result')
    st.write(summary)
               

#About
if selected=='About':
    st.title('Data')
    #st.subheader('All data for this project was publicly sourced from:')
    col1,col2,col3=st.columns(3)
    col1.subheader('Source')
    col2.subheader('Description')
    col3.subheader('Link')
    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('census_graphic.png',width=150)
        col1.write(':blue[U.S. Census Bureau]')
        col2.write('Demographic, housing, industry at zip level')
        #col2.write('American Community Survey, 5-Year Profiles, 2021, datasets DP02 - DP05')
        col3.write('https://data.census.gov/')
    
    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('cdc.png',width=150)
        col1.write(':blue[Centers for Disease Control and Prevention]')
        col2.write('Environmental factors at county level')
        col3.write('https://data.cdc.gov/')
    
    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('hud.png',width=150)\
        col1.write(':blue[U.S. Dept Housing and Urban Development]')
        col2.write('Mapping zip to county')
        col3.write('https://www.huduser.gov/portal/datasets/')

    with st.container():
        col1,col2,col3=st.columns(3)
        #col1.image('ods.png',width=150)
        col1.write(':blue[OpenDataSoft]')
        col2.write('Mapping zip to USPS city')
        col3.write('https://data.opendatasoft.com/pages/home/')
    
    st.divider()
    
    st.title('Creator')
    with st.container():
        col1,col2=st.columns(2)
        col1.write('')
        col1.write('')
        col1.write('')
        col1.write('**Name:**    Kevin Soderholm')
        col1.write('**Education:**    M.S. Applied Statistics')
        col1.write('**Experience:**    8 YOE in Data Science across Banking, Fintech, and Retail')
        col1.write('**Contact:**    kevin.soderholm@gmail.com or [linkedin](https://www.linkedin.com/in/kevin-soderholm-67788829/)')
        col1.write('**Thanks for stopping by!**')
        col2.image('Parrot.png')       