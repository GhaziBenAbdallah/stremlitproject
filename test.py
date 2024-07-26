import streamlit as st 


#title
st.title("Aaslema chabeb !")
st.write('this is our first app streamlit')

#### Markdown and text  

#markdown
st.markdown("# This is a markdown")
st.markdown("## This is a  second markdown")
st.markdown('### This is a markdown 3')


#text
st.text('this a text')


### headers and titles ####

st.title("Title")
st.header("header")
st.subheader('subheader')


##### layout and spacing


st.write("this is a text by me ")
st.write("")
st.write('text with spacing below')

### user input

user_input=st.text_input('Enter some text')
st.write(user_input)

#number input

number_input= st.number_input("Enter a number ",min_value=-100,max_value=100,value=50)
st.write(number_input)

#sliders
slider=st.slider("select a number ",min_value=-100,max_value=100,value=0)
st.write(slider)


#bouton
if st.button("hello!"):
    st.write('Enzel aal boutton yahbet citron')
    
    
#checkbox

if st.checkbox('this is a checkbox'):
    st.write("checkbow is checked")    
    
    
    
    
options= st.radio("check an option",["option1","option2","option3"]) 

st.write(f"your choice is {options}")   


select= st.selectbox("check an option",["option1","option2","option3"]) 

st.write(f"your choice is {select}")   



#multiselect box


hobbies= st.multiselect("what are your hobbies",['Sport',"Music","painting"])

st.write("you select ",len(hobbies),"hobbies")
st.write(hobbies)



## handle multi-user inputs    
def handle_input():
      name = st.text_input("Enter your name")
      age = st.number_input("Enter your age", min_value=0)
      if st.button("Submit"):
          st.write(f"Hello, {name}. You are {age} years old.")

handle_input()   



    
    
st.success("success!")    
st.info("information")
st.warning("warning")
st.error("Error")
exp=ZeroDivisionError("Trying to divide by zero")
st.exception(exp)    


from PIL import Image
img= Image.open("streamlit.png")
st.image(img,width=400)

#Input Values in App Logic
def app_logic(name, age):
      if age >= 18:
          st.success(f"Welcome, {name}. You are an adult.")
      else:
          st.error(f"Hello, {name}. You are a minor.")

name= st.text_input("Enter your name!")
age = st.number_input("Enter your age!", min_value=0)
if st.button("Submit!"):
    app_logic(name, age)