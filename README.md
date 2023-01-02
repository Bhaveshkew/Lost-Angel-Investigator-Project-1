# Lost-Angel-Investigator

Team Members -
<ul>
<li>Harsh Shrirame</li>
<li>Bhavesh Kewalramani</li>
<li>Daksh Kothari</li>
<li>Darshan Jawandhiya</li>
</ul>

In India many children are reported missing every year. Among them large number of cases are never found therefore one of the project's key goals is to create a missing children (people) locate application that may assist ordinary people whose loved ones have been abducted, missed, or rescued by the people. The public can upload photos of missing children, along with landmarks and to our webpage. The photo will be immediately matched to the missing child's registered photos in the database. The supplied child photograph is classified, and the photo with the best match is displayed from the database of missing children. Using the facial image uploaded by the public, a deep learning model is trained to accurately identify the missing child from the missing child image database.

Previously, MTCNN, a very successful deep learning method for image-based applications, wad employed for face detection. Now, Mediapipe's Face Mesh Module is employed for face detection. Then, EfficientNet is used to recognise faces in photographs. Unlike other deep learning algorithms, our method focuses solely on comparing photographs to those already recorded in the database and producing the most accurate results possible. Using the MTCNN model for face identification with EfficientNet, and correctly training it, yields a deep learning model that is noise, lighting, contrast, and picture position insensitive. The model's training accuracy was 96.66 percent and its testing accuracy was 76.81 percent, implying that there is a approximately 77 percent possibility of finding a match for the missing kid and it was evaluated using 25 Child classes. Now, when the model was trained on Darthmouth Dataset, it gave a training accuracy of 98.50 percent and testing accuracy of 96.30 percent, implying that there is a approximately 96 percent possibility of finding a match for the missing kid.

***
This model has got 76.81% accuracy on this validation dataset.
***

***
CroppedDataset.zip is zipped file for dataset.

Database of approximately 400 child images collected from internet.
The children in these images ARE NOT ACTUALLY LOST ONES.
Images are used just to train the model on dummy data because we could not get real data of lost children due to security and privacy issues.
***

***
Installation Process
 
1. First clone git repository.<br>
Write command in cmd <br>
command - git clone https://github.com/Bhaveshkew/Lost-Angel-Investigator-Project-1.git

2. Change directory to this folder <br>
command - cd HackathonWCE  <br>

3. Create a Virtual Environment <br>
	- pip install virtualenvwrapper-win <br>
	- mkvirtualenv project

4. Activate the Virtual Environment <br>
command - workon project <br>

5. Install Dependencies/Packages <br>
command - pip install -r requirements.txt <br>

6. Change directory to folder Frontend (Django) <br>
command - cd "Frontend (Django)" <br>

7. Make Migrations and Migrate <br>
command - python manage.py makemigrations <br>
command - python manage.py migrate <br>

8. Run the project <br>
command - python manage.py runserver <br>
***

***
Demonstration
Extract the zip file CroppedDataset.zip <br>

After running the project. <br> 
Go to localhost:8000/print <br>
<br>
Upload the image of child from Dataset <br>

Click Upload <br>
<img src="RESULTS/2.png"></img>
See the results. <br>
<img src="RESULTS/3.png"></img>
***





 

