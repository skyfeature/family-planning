from django.shortcuts import render, redirect
from django.http import HttpResponse
# from matplotlib import pylab
# from pylab import *
# import PIL, PIL.Image
# from io import StringIO
from personal.forms import YearForm
from personal.forms import ContraceptiveMethod
from personal.forms import Y_variable
# from personal.forms import DemoVariable

def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me', 'bipuljnv@gmail.com']})

def getimageurl(y, x):
	cols_count = 3
	rows_count = 9
	imgmatrix = [['' for x in range(cols_count+1)] for x in range(rows_count+1)] 
	imgmatrix[1][1] = 'condom_vs_education.png'
	imgmatrix[1][2] = 'condom_vs_religion.png'
	imgmatrix[1][3] = 'condom_vs_district.png'
	imgmatrix[2][1] = 'insurance_vs_education.png'
	imgmatrix[2][2] = 'insurance_vs_religion.png'
	imgmatrix[2][3] = 'insurance_vs_district.png'
	imgmatrix[3][1] = 'tfr_vs_education.png'
	imgmatrix[3][2] = 'tfr_vs_religion.png'
	imgmatrix[3][3] = 'tfr_vs_district.png'
	imgmatrix[4][1] = 'pills_daily_vs_education.png'
	imgmatrix[4][2] = 'pills_daily_vs_religion.png'
	imgmatrix[4][3] = 'pills_daily_vs_district.png'
	imgmatrix[5][1] = 'tubectomy_vs_education.png'
	imgmatrix[5][2] = 'tubectomy_vs_religion.png'
	imgmatrix[5][3] = 'tubectomy_vs_district.png'
	imgmatrix[6][1] = 'copperT_vs_education.png'
	imgmatrix[6][2] = 'copperT_vs_religion.png'
	imgmatrix[6][3] = 'copperT_vs_district.png'
	imgmatrix[7][1] = 'aware_of_haf_vs_education.png'
	imgmatrix[7][2] = 'aware_of_haf_vs_religion.png'
	imgmatrix[7][3] = 'aware_of_haf_vs_district.png'
	imgmatrix[8][1] = 'aware_of_ort_ors_vs_education.png'
	imgmatrix[8][2] = 'aware_of_ort_ors_vs_religion.png'
	imgmatrix[8][3] = 'aware_of_ort_ors_vs_district.png'
	imgmatrix[9][1] = 'aware_of_ort_ors_zinc_vs_education.png'
	imgmatrix[9][2] = 'aware_of_ort_ors_zinc_vs_religion.png'
	imgmatrix[9][3] = 'aware_of_ort_ors_zinc_vs_district.png'
	
	return imgmatrix[y][x]

def getimage(request):
	
	contentDict = {}
	if request.method == 'POST':
		yearForm = YearForm(request.POST)
		if yearForm.is_valid():
			yearText = yearForm.cleaned_data['y2011']
			contentDict['yearText'] = yearText
		contentDict['yearForm'] = yearForm

		contraceptiveMethod = ContraceptiveMethod(request.POST)
		contentDict['contraceptiveMethod'] = contraceptiveMethod

		y_variable = Y_variable(request.POST)
		contentDict['y_variable'] = y_variable

		if y_variable.is_valid():
			y_chosen = y_variable.cleaned_data['y_axis']
			x_chosen = y_variable.cleaned_data['x_axis']
			print(y_chosen, x_chosen)
			print(getimageurl(int(y_chosen), int(x_chosen)))

		contentDict['img_name'] = getimageurl(int(y_chosen), int(x_chosen))
		# return redirect('/blog')
	else:
		yearForm = YearForm()
		contentDict['yearForm'] = yearForm
		contraceptiveMethod = ContraceptiveMethod()
		contentDict['contraceptiveMethod'] = contraceptiveMethod
		y_variable = Y_variable()
		contentDict['y_variable'] = y_variable
	return render(request, 'personal/blog.html', contentDict)


def showimage(request):
    # Construct the graph
    t = arange(0.0, 2.0, 0.01)
    s = sin(2*pi*t)
    plot(t, s, linewidth=1.0)

    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)

    # Store image in a string buffer
    buffer = StringIO.StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type ="image/png")

