"# family-planning"   

Hi there,   
	Welcome to the project 'Analysis of family planning data'.   
	You can download data from:   
		https://nrhm-mis.nic.in/hmisreports/AHSReports.aspx   
		We are working on the 'WOMAN' data and 'WPS' data. So make sure you download both the folders.   
	The tools you will require are:   
		python3.5 :- any of the python3.x version will work   
		numpy :- for manipulating numerical aspect of data   
		pandas :- for storing and handling of data. The data structure used for storing it is Dataframe   
		matplotlib :- for plotting and coloring   
		sklearn :- for inbuilt machine learning libraries   
		pickle :- reading of text file takes a lot of time. So we will read the text file once    
		using pandas into dataframe and then freeze it and save it into a .pkl file.    
		Reading the file takes few seconds max.    
		jupyter :- This will be our working environment.    
		django :- The website is built upon django.    
  
		We will code into jupyter and execute them then and there.   
	  
		I would suggest you to get familiar with basic jupyter commands.   
		Basic 4-5min of video will do it. The best thing about jupyter is it saves the state of the running program.  
		So suppose your program read 1gb of data in 5mins in one block then you can keep doing   
		calculation again and again on the data in other block without spending time in reading the data again.     
	  
		Why django: Because it forces us to adapt mvc(model-view-controller) architecture,   
		which leads to easy to understand and manageable code. Watch some videos related to it.   
		I would suggest sentex on youtube. Django's documentation is top notch.   
		Once you will get hang of it, you will find intuitive.     

	File explanation:  
		contraception.ipynb:  
			This file is about exploring and getting familiar with the data in 'WPS' folder.   
			This file contains lots of graph plotting techniques which one may use as reference or simply copy paste.   
			I have tried to tell using comments about what I was doing and what was outcome of experiment.    
		analysis_of_women_data.ipynb:     
			This file deals in data in 'WOMAN' folder. Data contained in 'WOMAN' folder is our main data.     
			Since the data contained in this folder has hugh size and your laptop cannot handle it,      
			you can start with working on 2-3 smaller states first.    
		Data_structure_AHS.xlsx:   
			This file contains description of the data files downloaded from above mentioned site.   
		An Introduction To Statistical Learning with Applications in R (ISLR Sixth Printing):   
			Book prescribed by Prof to read for modelling.   
		AHS_report_part1.pdf:   
			Official report of the survey by Govt. For any further explanation of data contact this file.    

	Instructions for getting started with data visualization on webpage:   
		Open terminal and clone the repository:   
			$git clone https://github.com/skyfeature/family-planning.git   
		Enter into the folder family-planning.   
		Here you will see bunch of files alongside with a folder named mysite.   
		mysite contains code for django website. To test it open terminal inside the folder and type:   
			$python manage.py runserver   
		Then you can view website by going to http://127.0.0.1:8000   
		Our project website is http://127.0.0.1:8000/blog   
		Here choose x and y variables and click submit. It fetches corresponding graph and displays them.   
		The related code is stored in mysite/personal   
		The personal folder contains:   
			/static/personal :- It contains all css, javascript, image files for our website.   
			/template/personal :- It contains all webpages. Blog.html is our focus.   
			/forms.py :- It contains all the form classes used in webpage.   
			/url.py :- It maps url to webpage.   
			/views.py :- Here we import the form classes and receive get and post requests.    
			Collect user input and fetch image urls according to user input.   
			Image urls has been stored in a dictionary. Though what we wanted to do was to plot and fetch them directly into webpage.   
		Todo has been mentioned in final presentation.   
 
	Instructions for getting started with data analysis:   
		Open terminal in family-panning folder and type:   
			$jupyter notebook   
		Click on 'contraception.ipynb' or 'analysis_of_women_data.ipynb'.   
		View the file as it is.   
		Start execution from first block by ctrl+enter.   