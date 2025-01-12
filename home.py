import streamlit as st
from page_init import page_init
from meeting_form import insert_meeting_form
from send_email import test
from calendar_source import OutlookCalendar
from datetime import datetime


def main():
    calendar = OutlookCalendar()

    c1, c2 = page_init()

    with st.container():
        with c1:  
            st.markdown("# Hi, I'm Kyan Nelson")
            st.markdown("##### *BS  Dual Emphasis in Finance and Information Management with Computer Science Integration*")
            st.markdown('''
                        - Phone Number:303-802-9736
                        - Email: kyan.nelson@colorado.edu
                        - LinkedIn: https://www.linkedin.com/in/kyan-nelson/                        
                        ''')

        with c2:
            st.image("static/headshot.png", width=400)

    st.header("Schedule a Coffee Chat:")
    # insert_meeting_form()
    if st.button("Send"):
        st.write(calendar.get_available_slots(datetime.now().date()))
        print(calendar.get_available_slots(datetime.now().date()))
        # test()

if __name__ == "__main__":
    main()