# COLLABSTUDIO

## DESCRIPTION
This is a web application that allows users collaborate on various projects involving content creation e.g music,art,movies e.t.c they can upload and share their content and even be able to play it through the application.

## AUTHOR
Neville Oronni

## USER STORIES
A **user** should be albe to:
1. Sign in to the application to start using.

2. Upload content(images,music) to the site.

3. See my profile with all my projects.

4. Follow other users and see their projects on my timeline.

5. Like a projects and leave  comments on it.

6. Download projects content like media files and save it to my machine.

7. Create their own custom projects and have others follow it.

## SPECIFICATIONS
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
|Sign into application |click sigin button | logged into the index page|
|Upload media | Click post button & add image url | see posted media display in profile page |
|See all user projects | Click profile | see profile page with profile details and projects |
|Follow other users | Navigate the users posted image & click follow button | list of followed users should be dispayed in users index page |
|Like another user project | Click like button on post | should see no. of likes increment by 1 every time you like |
|Download media files | Click download button on image | should see downloaded image on local machine after completion |  

## SETUP/INSTALLATION
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

* Clone the repo
  * git clone **repo_url** e.g git clone https://github.com/nevooronni/Capstone
* Create and start a virtual environment inside project directory
  * virtual venv virtual
  * source virtual/bin/activate

* Install all the dependencies in the file > requirements.txt
  * pip install -r requirements.txt
* Start the development server
  * python3.7 manage.py runserver

## PREREQUISITIES
* Python3.6
* Django

## TECHNOLOGIES USED
* Python3.6
* Django
* Postgresql
* Bootstrap3

## BUGS
No known bugs

## CONTACT
[nevooronni@gmail.com](nevooronni@gmail.com)

## LICENCE
Licenced under a MIT licence
