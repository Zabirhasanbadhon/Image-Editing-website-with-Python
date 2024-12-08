import streamlit as st #Build WeApp
import cv2 #image Processiong
from PIL import Image, ImageEnhance
import numpy as np
import os


face_cascade = cv2.CascadeClassifier('D:\Image_editing_Project_Python\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:\Image_editing_Project_Python\haarcascade_eye.xml')


def detect_faces(our_image):
     new_img = np.array(our_image.convert("RGB"))
     faces = face_cascade.detectMultiScale(new_img, 1.1, 20)
     for (x,y,w,h) in faces:
         cv2.rectangle(new_img,(x,y), (x+w ,y+h), (255,0,0), 2)
     return new_img,faces

def detect_eyes(our_image):
     new_img = np.array(our_image.convert("RGB"))
     eyes = eye_cascade.detectMultiScale(new_img, 1.3, 20)
     for (x,y,w,h) in eyes:
         cv2.rectangle(new_img,(x,y), (x+w ,y+h), (0,255,0), 2)
     return new_img

def cartoonize_image(our_image):
     new_img = np.array(our_image.convert("RGB"))
     gray = cv2.cvtColor(new_img,cv2.COLOR_BGR2GRAY)
     gray = cv2.medianBlur(gray, 5)
     edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 9)
     color = cv2.bilateralFilter(new_img, 9, 300, 300)
     cartoon = cv2.bitwise_and(color, color, mask = edges)
     return cartoon
 
def cannize_image(our_image):
    new_img = np.array(our_image.convert("RGB"))
    img = cv2.GaussianBlur(new_img,(13,13),0)
    canny = cv2.Canny(img, 100, 150)
    return canny
    
      

def main():
    
   st.title('Image_Editing With Fun')
   st.text('Edit Your Image in fast and Simple Way')
   
   
   activities = ['Detection','About']
   choice = st.sidebar.selectbox('Select Activity', activities)
   
   if choice == 'Detection':
       
       st.subheader('Face Detection')
       image_file = st.file_uploader('Upload Image',type = ['jpg','png','jpeg'])
       st.text('Please Upload Your Image and Edit Your Image')
       
       if image_file is not None:
           
           our_image = Image.open(image_file)
           st.text('Original Image')
           st.image(our_image)
           
           enhance_type = st.sidebar.radio("Enhance type", ['Original','Gray-Scale','Contrast','Brightness','Blurring', 'Sharpness'])
           
           if enhance_type == 'Gray-Scale':
               
               st.text('Gray-Scaled Image')
               img = np.array(our_image.convert('RGB'))
               gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
               st.image(gray)
               
           
           elif enhance_type == 'Contrast':
               
               st.text('Tune Contrast.............')
               rate = st.sidebar.slider("Contrast", 0.0, 8.0)
               enhancer = ImageEnhance.Contrast(our_image)
               enhanced_img = enhancer.enhance(rate)
               st.image(enhanced_img)
               
               
               
           
           elif enhance_type == 'Brightness':
               
               st.text('Tune Brightness..........')
               rate = st.sidebar.slider("Brightness", 0.0, 8.0)
               enhancer = ImageEnhance.Brightness(our_image)
               enhanced_img = enhancer.enhance(rate)
               st.image(enhanced_img)
               
           
           
           elif enhance_type == 'Blurring':
               
               st.text('Tune Blur.............')
               rate = st.sidebar.slider("Blurring Image", 0.0, 7.0)
               blurred_img = cv2.GaussianBlur(np.array(our_image), (15,15), rate)
               st.image(blurred_img)
               
               
           elif enhance_type == 'Sharpness':
               
               rate = st.sidebar.slider("Sharpness", 0.0 , 10.0)
               enhancer = ImageEnhance.Sharpness(our_image)
               enhanced_img = enhancer.enhance(rate)
               st.image(enhanced_img)
               
           elif enhance_type == 'Original':
               st.image(our_image)
          
           else :
                st.image(our_image)
                
                
       tasks = ["Faces", "Eyes", "Cartoonize", "Cannize"]
       feature_choice = st.sidebar.selectbox("Fine Features", tasks)
       
       if st.button("Process"):
           if feature_choice == "Faces":
                result_img, result_faces = detect_faces(our_image)
                st.image(result_img)
                st.success("Found {} faces".format(len(result_faces)))
                
           elif feature_choice  == "Eyes":
                result_img = detect_eyes(our_image)
                st.image(result_img)
               
                
           elif feature_choice == "Cartoonize":
               result_img = cartoonize_image(our_image)
               st.image(result_img)
               
           elif feature_choice == "Cannize":
               result_img = cannize_image(our_image)
               st.image(result_img)
        

               
   elif choice == 'About':
        
       st.subheader('About the Developer')
       st.markdown('Build with streamlit by  [ZaBir HaSan](https://github.com/Zabirhasanbadhon)')
       st.text('I am Zabir Hasan From Bangladesh. I am Computer science Student')
        
           


if __name__ == '__main__':
    main()