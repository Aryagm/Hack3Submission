import numpy as np
import streamlit as st
import joblib

st.set_page_config(layout="wide")

anx_model = joblib.load('./Models/anxiety_model.pkl')
dep_model = joblib.load('./Models/depression_model.pkl')
comp_model = joblib.load('./Models/compulsive_behavior_model.pkl')

st.image("https://cdn.discordapp.com/attachments/939536871262912546/939616419140755496/unknown.png")

st.subheader("Please fill out this survey to help us understand your health and suggest wellness solutions.")

st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown("<br/>", unsafe_allow_html=True)


q1 = st.radio("Are you currently employed at least part-time?", ('Yes', 'No'))

st.markdown("<br/>", unsafe_allow_html=True)

q2 = st.selectbox("What is your education level?", ('Some High School', 'Completed High School or GED', 'Some Undergraduate', 'Completed Undergraduate', 'Some Masters', "Completed Masters", "Some Phd", "Completed Phd"))

st.markdown("<br/>", unsafe_allow_html=True)

q3 = st.radio("Do you have your own computer separate from a smart phone?", ('Yes', 'No'))

st.markdown("<br/>", unsafe_allow_html=True)

q4 = st.radio("Are you legally disabled?", ('Yes', 'No'))

st.markdown("<br/>", unsafe_allow_html=True)

q5 = st.radio("Do you have regular access to the internet?", ('Yes', 'No'))

st.markdown("<br/>", unsafe_allow_html=True)

q6 = st.radio("Do you live with your parents?", ('Yes', 'No'))

st.markdown("<br/>", unsafe_allow_html=True)

q7 = st.radio("Do you have a gap in your resume?", ('Yes', 'No'))

st.markdown("<br/>", unsafe_allow_html=True)

q8 = st.number_input("What is your annual income (including any social welfare programs) in USD?", min_value=0)

st.markdown("<br/>", unsafe_allow_html=True)

q9 = st.radio("Do you read outside of work and school?", ('Yes', 'No'))

st.markdown("<br/>", unsafe_allow_html=True)

q10 = st.number_input("Annual income from social welfare programs (in USD)?", min_value=0, max_value=100000)

st.markdown("<br/>", unsafe_allow_html=True)

q11 = st.radio("Do you receive food stamps?", ('Yes', 'No'))

st.markdown("<br/>", unsafe_allow_html=True)

q12 = st.radio("Are you on section 8 housing?", ('Yes', 'No'))

st.markdown("<br/>", unsafe_allow_html=True)

q13 = st.radio("What is your age?", ('18-29', '30-44', '45-60', '60+'))

st.markdown("<br/>", unsafe_allow_html=True)

q14 = st.radio("What is your Gender?", ('Male', 'Female'))

st.markdown("<br/>", unsafe_allow_html=True)

q15 = st.selectbox("What is your Household Income (in USD)?", ('$0-$9,999', '$10,000-$24,999', '$25,000-$49,999', '$50,000-$74,999', '75,000-$99,999', "$100,000-$124,999", "125,000-$149,999", "150,000-$174,999", "$175,000-$199,999", "$200,000+"))

st.markdown("<br/>", unsafe_allow_html=True)

q16 = st.selectbox("Which region do you come from?", ('South Atlantic', 'Middle Atlantic', 'East North Central', 'Pacific', 'Mountain', "West South Central", "East South Central", "West North Central"))

st.markdown("<br/>", unsafe_allow_html=True)

q17 = st.selectbox("Which type of device are you using?", ('Windows Desktop / Laptop', 'Android Phone / Tablet', 'iOS Phone / Tablet', 'MacOS Desktop / Laptop'))

st.markdown("<br/>", unsafe_allow_html=True)

q18 = st.radio("Do feel a lack of concentration?", ('True', 'False'))

st.markdown("<br/>", unsafe_allow_html=True)

q19 = st.radio("Do feel tired without physical effort?", ('True', 'False'))

st.markdown("<br/>", unsafe_allow_html=True)

q20 = st.radio("Do you suffer from rapid Mood Swings?", ('True', 'False'))

st.markdown("<br/>", unsafe_allow_html=True)

q21 = st.radio("Do you tend to overthink things of low significance?", ('True', 'False'))

submit_button = st.button("Submit")

if submit_button:
    with st.spinner('Wait for it...'):
        ans_array = []

        if q1 == 'yes':
            ans_array.append(1)
        else:
            ans_array.append(0)

        if q2 == 'Some High School':
            ans_array.append("Some highschool")
        elif q2 == 'Completed High School or GED':
            ans_array.append("High School or GED")
        elif q2 == 'Some Undergraduate':
            ans_array.append("Some Undergraduate")
        elif q2 == 'Completed Undergraduate':
            ans_array.append("Completed Undergraduate")
        elif q2 == 'Some Masters':
            ans_array.append("Some Masters")
        elif q2 == "Completed Masters":
            ans_array.append("Completed Masters")
        elif q2 == "Some Phd":
            ans_array.append("Some Phd")
        elif q2 == "Completed Phd":
            ans_array.append("Completed Phd")
        
        if q3 == 'yes':
            ans_array.append(1)
        else:
            ans_array.append(0)

        if q4 == 'yes':
            ans_array.append(1)
        else:
            ans_array.append(0)

        if q5 == 'yes':
            ans_array.append(1)
        else:
            ans_array.append(0)
        
        if q6 == 'yes':
            ans_array.append(1)
        else:
            ans_array.append(0)
        
        if q7 == 'yes':
            ans_array.append(1)
        else:
            ans_array.append(0)
        
        ans_array.append(q8/1000)

        # Unemployed:
        if q1 == 'yes':
            ans_array.append(0)
        else:
            ans_array.append(1)
        
        if q9 == 'yes':
            ans_array.append(1)
        else:
            ans_array.append(0)
        
        ans_array.append(q10/1000)

        if q11 == 'yes':
            ans_array.append(1)
        else:
            ans_array.append(0)

        if q12 == 'yes':
            ans_array.append(1)
        else:
            ans_array.append(0)

        if q13 == '18-29':
            ans_array.append('18-29')
        elif q13 == '30-44':
            ans_array.append('30-44')
        elif q13 == '45-60':
            ans_array.append('45-60')
        elif q13 == '60+':
            ans_array.append('60+')

        if q14 == 'yes':
            ans_array.append(1)
        else:
            ans_array.append(0)

        if q15 == '$0-$9,999':
            ans_array.append('$0-$9,999')
        elif q15 == '$10,000-$24,999':
            ans_array.append('$10,000-$24,999')
        elif q15 == '$25,000-$49,999':
            ans_array.append('$25,000-$49,999')
        elif q15 == '$50,000-$74,999':
            ans_array.append('$50,000-$74,999')
        elif q15 == '75,000-$99,999':
            ans_array.append('75,000-$99,999')
        elif q15 == "$100,000-$124,999":
            ans_array.append("$100,000-$124,999")
        elif q15 == "125,000-$149,999":
            ans_array.append("125,000-$149,999")
        elif q15 == "150,000-$174,999":
            ans_array.append("150,000-$174,999")
        elif q15 == "$175,000-$199,999":
            ans_array.append("$175,000-$199,999")
        elif q15 == "$200,000+":
            ans_array.append("$200,000+")

        if q16 == 'South Atlantic':
            ans_array.append('South Atlantic')
        elif q16 == 'Middle Atlantic':
            ans_array.append('Middle Atlantic')
        elif q16 == 'East North Central':
            ans_array.append('East North Central')
        elif q16 == 'Pacific':
            ans_array.append('Pacific')
        elif q16 == 'Mountain':
            ans_array.append('Mountain')
        elif q16 == "West South Central":
            ans_array.append("West South Central")
        elif q16 == "East South Central":
            ans_array.append("East South Central")
        elif q16 == "West North Central":
            ans_array.append("West North Central")
        
        if q17 == 'Windows Desktop / Laptop':
            ans_array.append('Windows Desktop / Laptop')
        elif q17 == 'Android Phone / Tablet':
            ans_array.append('Android Phone / Tablet')
        elif q17 == 'iOS Phone / Tablet':
            ans_array.append('iOS Phone / Tablet')
        elif q17 == 'MacOS Desktop / Laptop':
            ans_array.append('MacOS Desktop / Laptop')
        
        if q18 == 'True':
            ans_array.append(1)
        else:
            ans_array.append(0)
        
        if q19 == 'True':
            ans_array.append(1)
        else:
            ans_array.append(0)
        
        if q20 == 'True':
            ans_array.append(1)
        else:
            ans_array.append(0)
        
        if q21 == 'True':
            ans_array.append(1)
        else:
            ans_array.append(0)


        anxiety_pred = anx_model.predict(np.array(ans_array).reshape(1, -1))
        depression_pred = dep_model.predict(np.array(ans_array).reshape(1, -1))
        compulsive_pred = comp_model.predict(np.array(ans_array).reshape(1, -1))

        if anxiety_pred[0] == 1:
            anxiety_pred = False
        else:
            anxiety_pred = True
        
        if depression_pred[0] == 1:
            depression_pred = False
        else:
            depression_pred = True
        
        if compulsive_pred[0] == 1:
            compulsive_pred = True
        else:
            compulsive_pred = False
               
        st.markdown("<hr/>", unsafe_allow_html=True)
        st.markdown("<br/>", unsafe_allow_html=True)

        st.header("Your Results:")
        st.markdown("<br/>", unsafe_allow_html=True)

        if anxiety_pred == True and depression_pred == True and compulsive_pred == True:
            st.subheader("We feel that you are feeling a bit anxious and under the weather. You also may be overthinking small things. Please take a look at the resources below, they can help you feel better :)")
        elif anxiety_pred == True and depression_pred == True and compulsive_pred == False:
            st.subheader("We feel that you are feeling a bit anxious and under the weather. Please take a look at the resources below, they can help you feel better :)")
        elif anxiety_pred == True and depression_pred == False and compulsive_pred == True:
            st.subheader("We feel that you are feeling a bit anxious and may be overthinking small things. Please take a look at the resources below, they can help you feel better :)")
        elif anxiety_pred == True and depression_pred == False and compulsive_pred == False:
            st.subheader("We feel that you are feeling a bit anxious. Please take a look at the resources below, they can help you feel better :)")
        elif anxiety_pred == False and depression_pred == True and compulsive_pred == True:
            st.subheader("We feel that you are feeling under the weather and may be overthinking small things. Please take a look at the resources below, they can help you feel better :)")
        elif anxiety_pred == False and depression_pred == True and compulsive_pred == False:
            st.subheader("We feel that you are feeling under the weather. Please take a look at the resources below, they can help you feel better :)")
        elif anxiety_pred == False and depression_pred == False and compulsive_pred == True:
            st.subheader("We feel that you may be overthinking small things. Please take a look at the resources below, they can help you feel better :)")
        else:
            st.subheader("We feel that you have an excellent State of Mind! :)")

        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("<hr/>", unsafe_allow_html=True)

        # Embed this video: https://www.youtube.com/watch?v=inpok4MKVLM in size 100 by 200
        st.markdown("""
        <iframe width="560" height="315" src="https://www.youtube.com/embed/inpok4MKVLM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)

        st.markdown("""
        <iframe width="560" height="315" src="https://www.youtube.com/embed/tEmt1Znux58" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)

        st.markdown("""
        <iframe width="560" height="315" src="https://www.youtube.com/embed/VUjiXcfKBn8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """, unsafe_allow_html=True)