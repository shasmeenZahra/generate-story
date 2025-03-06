import streamlit as st

def mad_libs():
    st.title("Mad Libs Game")
    st.write("Fill in the blanks to create a funny story!")
    
    noun = st.text_input("Enter a noun:")
    verb = st.text_input("Enter a verb:")
    adjective = st.text_input("Enter an adjective:")
    place = st.text_input("Enter a place:")
    
    if st.button("Generate Story"):
        if noun and verb and adjective and place:
            story = f"One day, a {adjective} {noun} decided to {verb} at {place}. It was the most hilarious thing ever!"
            st.subheader("Here is your Mad Libs story:")
            st.write(story)
        else:
            st.warning("Please fill in all the fields to generate the story.")

if __name__ == "__main__":
    mad_libs()
