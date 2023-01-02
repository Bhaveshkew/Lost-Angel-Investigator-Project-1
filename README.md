# Lost-Angel-Investigator

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
command - git clone https://github.com/DakshKothari18/HackathonWCE

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





 

