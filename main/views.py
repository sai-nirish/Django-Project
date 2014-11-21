from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from signin.models import UserProfile
import csv, os

@login_required
# Create your views here.
def checkcourse(request):
	submitted = False
	if request.method == 'POST':
		submitted = True
		rank = request.POST['rank']
		category = request.POST['cat']
		
		try:
			rank = int(rank)
		except ValueError:
			print("Enter integer rank")
		
		if category == "":
			print("Choose a category")
		
		else:
			ocranks = {}
			ccourses = {}
			f1 = open("./closingRankData-2012.csv")
			f2 = open("./data_u-2012.csv")
			reader1 = csv.reader(f1)
			reader2 = csv.reader(f2)
			for row in reader2:
				cid = row[2]
				ccampus = row[0]
				cname = row[1]
				ccourses[cid] = (ccampus+" "+cname)
			for row in reader1:
				cid = row[0]
				if cid!= 'Code':
					vals = {}
					vals['gen'] = (int(row[1]),int(row[2]))
					vals['obc'] = (int(row[3]),int(row[4]))
					vals['sc'] = (int(row[5]),int(row[6]))
					vals['st'] = (int(row[7]),int(row[8]))
					vals['genpd'] = (int(row[9]),int(row[10]))
					vals['obcpd'] = (int(row[11]),int(row[12]))
					vals['scpd'] = (int(row[13]),int(row[14]))
					vals['stpd'] = (int(row[15]),int(row[16]))
					ocranks[cid] = vals
			pcourses = []
			for key in ocranks.keys():
				if ocranks[key][category][0] <= rank and ocranks[key][category][1] >= rank:
					pcourses.append(key+" "+ccourses[key])
				pcourses.sort()
				
			return render(request, 'main/coursecheck.html', {'submitted':submitted, 'courselist':pcourses, 'user':request.user})
	else:
		return render(request, 'main/coursecheck.html', {'submitted':submitted, 'user':request.user})

@login_required		
def index(request):
	if request.method == 'POST':
		num = 1
		data = ""
		while True:
			tag = 'option'+str(num)
			option = request.POST.get(tag,False);
			if not(option):
				data = data[:len(data)-1]
				break
			else:
				data+=option[:5]+"_"
				num+=1
		userprofile = UserProfile.objects.get(user=request.user)
		userprofile.choices = data
		userprofile.save()
		username = request.user
		emailid = request.user.email
		userprofile = UserProfile.objects.get(user=request.user)
		roll = userprofile.uniqueid
		saved = True
		return render(request, 'main/index.html', {'saved':saved, 'user_name':username, 'user_email':emailid, 'roll_number':roll, 'choices':data})
	else:
		username = request.user
		emailid = request.user.email
		userprofile = UserProfile.objects.get(user=request.user)
		roll = userprofile.uniqueid
		return render(request, 'main/index.html', {'user_name':username, 'user_email':emailid, 'roll_number':roll})

@login_required
def fill(request):
	userprofile = UserProfile.objects.get(user=request.user)
	if userprofile.locked == "N":
		username = request.user
		emailid = request.user.email
		userprofile = UserProfile.objects.get(user=request.user)
		choices = userprofile.choices
		chlist = []
		while choices != "":
			chlist.append(choices[:5])
			choices = choices[6:]
		f2 = open("./data_u-2012.csv")
		ccourses = []
		reader2 = csv.reader(f2)
	
		choicelist = []
		for row in reader2:
			cid = row[2]
			ccampus = row[0]
			cname = row[1]
			if cid in chlist:
				choicelist.append(cid+" "+ccampus+" "+cname)
			else:
				ccourses.append((cid, ccampus+" "+cname))
				ccourses.sort()
		return render(request, 'main/filloptions.html', {'user_name':username, 'user_email':emailid, 'course_list':ccourses, 'choice_list':choicelist})
	else:
		username = request.user
		emailid = request.user.email
		roll = userprofile.uniqueid
		return render(request, 'main/index.html', {'user_name':username, 'user_email':emailid, 'roll_number':roll, 'locked':True})
	
@login_required
def verify(request):
	userprofile = UserProfile.objects.get(user=request.user)
	ccourses = {}
	f2 = open("./data_u-2012.csv")
	reader2 = csv.reader(f2)
	data = userprofile.choices
	datalist = []
	while data!="":
		datalist.append(data[:5])
		data=data[6:]
	choicelist =[]
	for row in reader2:
		cid = row[2]
		ccampus = row[0]
		cname = row[1]
		for word in datalist:
			if(word == cid):
				choicelist.append(cid+" "+ccampus+" "+cname)
	unlock = False
	if userprofile.locked == 'N':
		unlock = True
	return 	render(request,'main/verify.html',{'choice_list':choicelist,'unlocked':unlock})
	
def lock(request):
	userprofile = UserProfile.objects.get(user=request.user)
	unlock = False
	if userprofile.locked == 'N':
		unlock = True
	if unlock:
		os.system("touch choices.csv")
		f = open('choices.csv')
		r = csv.reader(f)
		counter = 0
		lwrite = False
		for row in r:
			counter+=1
			if counter>=1:
				break
		if counter == 0:
			lwrite = True
		with open('choices.csv', 'a') as fp:
			a = csv.writer(fp, delimiter=',')
			data = [[userprofile.uniqueid,userprofile.category,userprofile.pdstatus,userprofile.choices]]
			if lwrite:
				line = [["unique ID", "Category", "PD status", "Choices"]]
				a.writerows(line)
			a.writerows(data)
		userprofile.locked = "Y"
		userprofile.save()
		username = request.user
		emailid = request.user.email
		roll = userprofile.uniqueid
		return render(request, 'main/index.html', {'user_name':username, 'user_email':emailid, 'roll_number':roll, 'vlocked':True})
