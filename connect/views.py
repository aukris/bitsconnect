from django.shortcuts import render,redirect, get_object_or_404
from extra_func import get_weekly_calendar,get_fav_status
from .models import *
from django.http import HttpResponse,Http404,HttpResponseRedirect
from datetime import datetime
from django.contrib.auth import authenticate, login , logout
import time,string,random
from django.contrib.auth.decorators import login_required
from scripts import gmail
from django.contrib.auth.decorators import login_required
import re
import textwrap
from django.utils import timezone
from django.db.models import Q
import urllib3, json


def auth_logout(request):
    logout(request)
    return redirect('home')


def auth_register(request):
    if request.method == "POST":
        method = request.POST['signup_method']
        if method == 'email':
            try:
                username = request.POST['username']
                first_name = request.POST['nickname']
                if not re.match(r'[fh]201[0-9]{4}',username):
                    raise Http404("Not Allowed!")
            except:
                raise Http404("Please provide all necessary details to register.")
            else:
                if username and first_name:
                    try:
                        user = User.objects.get(username=username)
                        return render(request, 'connect/info.html', { 'msg' : """Your account is
                                already registered. Please login using the link below"""})
                    except Exception as e:
                        email = username+'@pilani.bits-pilani.ac.in'
                        password = "".join(random.choice(string.letters+string.digits) for i in range(8))
                        user = User(username=username, first_name=first_name, email=email)
                        user.set_password(password)
                        user.save()
                        email_subject = "Bits Connect Password"
                        email_body = ("Dear %s,\nThank you for registering with BITS Connect.Your password is\n%s\n\n"+
                                      "If you are a SU representative please contact the administrators for permission to "+
                                      "solve problems on P.R.S. Also if you represent a Department, Club or Regional Association "+
                                      "that is yet to receive login credentials please request for one at the earliest. "+
                                      "\n\n-regards\nSidhartha Namburi")%(first_name, password)
                        gmail.send(email, email_subject, email_body)
                        return render(request, 'connect/email_sent.html')

                else:
                    raise Http404("Please provide the necessary details to register.")
        elif method == 'facebook':
            access_token = request.POST['access_token']
            http = urllib3.PoolManager()
            file_ = http.request('GET',
                "https://graph.facebook.com/me?access_token=" + access_token + '&fields=email,first_name,last_name')
            ret = json.loads(file_.data)
            uid_ = ret['id']
            try:
                email = ret['email']
            except KeyError:
                raise Http404("Unknown Facebook error")
            try:
                user = UserFacebookData.objects.get(uid=uid_).user_profile
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return HttpResponse(1,status=200)
            except UserFacebookData.DoesNotExist:
                email = ret['email'].encode('utf-8')
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    first_name = ret['first_name'].encode('utf-8')
                    last_name = ret['last_name'].encode('utf-8')
                    # HANDLE PHONE HERE
                    username = first_name.lower().replace(" ", "") + str(random.randint(1, 999999))
                    user = User(username=username, first_name=first_name, email=email)
                    user.save()
                except:
                    return HttpResponse(0, status=400)
                UserFacebookData.objects.create(token=access_token, extra_data=json.dumps(ret),
                                                       user_profile=user, uid=uid_)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return HttpResponse(1, status=200)
    else:
        return HttpResponse(-1, status=400)



def auth_forgot(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
        except:
            raise Http404("500.Empty Username not allowed!!")

        else:
            try:
                user = User.objects.get(username=username)
                password = "".join(random.choice(string.letters+string.digits) for i in range(8))
                user.set_password(password)
                user.save()
                email_subject = "BITS Connect Password RESET"
                email_body = "Dear %s, \nYour password is   %s \n\n -regards\n Sidhartha Namburi"%(user.first_name, password)
                gmail.send(user.email, email_subject, email_body)
                return render(request, 'connect/email_sent.html')
            except User.DoesNotExist:
                return render(request, 'connect/info.html', { 'msg' : """You don't have an account.
					Please register"""})
            except Exception as e:
                #print e
                raise Http404('Error Occured')
    else:
        return redirect('home')




def home(request):
    if not request.user.is_authenticated():

        return render(request,'connect/index.html')
    else:
        context = {'events':GlobalEvent.objects.all()}
        return render(request,'connect/dashboard.html',context)

def about(request):
    return render(request, 'connect/about.html')



def auth_login(request):
    error = 0
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse(1, status=200)


                else:
                    error = 3
            else:

                user = User.objects.get(username=username)
                error=1

        except User.DoesNotExist:
            error=2
        except Exception as e:
            redirect('home')
        return HttpResponse(error, status=400)
    else:
        return redirect('home')





@login_required
def get_user_name(request):
    if request.method == 'POST':
        username = request.POST['username']
        try:
            user = User.objects.get(username=username)
            return HttpResponse(user.first_name)
        except:
            return HttpResponse('')
    else:
        return redirect('home')


@login_required
def auth_reset_pass(request):
    if request.method == 'POST':
        try:
            password = request.POST['newpassword']
            oldpassword = request.POST['oldpassword']
            user = authenticate(username=request.user, password=oldpassword)
        except:
            return redirect('home')
        try:
            if user:
                user.set_password(password)
                user.save()
                return redirect('logout')
            else:
                return redirect('home')
        except:
            raise Http404('Error occured.')
    else:
        redirect('home')


@login_required
def missed_call(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
            MissedCall.objects.create(user=user,actor=request.user)
            return HttpResponse(1)
        except:
            return HttpResponse(1)
    else:
        return redirect('home')
@login_required
def bits_line(request):
    partner_id = request.GET.get('partner_id',"")
    call_obj = MissedCall.objects.filter(user=request.user).select_related('actor__username').order_by('-pk')
    calls = [x.actor.username for x in call_obj]
    call_obj.delete()


    return  render(request,'connect/bits_line.html',{'my_id':request.user, 'partner_id':partner_id, 'calls':calls})

@login_required
def services(request):
    context={'services':Service.objects.all().order_by("-created")}
    return render(request, 'connect/services.html',context,)

@login_required
def del_service(request,service_id):
    try:
        service = get_object_or_404(Service,pk=service_id, user=request.user)
        service.delete()
    except:
        raise Http404("Cannot delete post.")
    return redirect('myservices')



@login_required
def del_classified(request,ad_id):
    try:
        classified = get_object_or_404(Classified,pk=ad_id, user=request.user)
        classified.delete()
    except:
        raise Http404("Cannot delete post.")
    return redirect('myads')


@login_required
def del_travel(request,t_id):
    try:
        classified = get_object_or_404(Travel,pk=t_id, user=request.user)
        classified.delete()
    except:
        raise Http404("Cannot delete post.")
    return redirect('mytravel')


@login_required
def my_travel(request):
    context={'travel' : Travel.objects.filter(user=request.user).order_by("-pk")}
    return render(request, 'connect/my_travel.html',context)




@login_required
def del_problem(request,p_id):
    try:
        problem = get_object_or_404(Problem,pk=p_id, user=request.user)
        bhavan = problem.bhavan.name
        problem.delete()
    except:
        raise Http404("Cannot delete post.")

    return redirect('myproblems',bhavan=bhavan )


@login_required
def my_services(request):
    context={'post':False,'error':False}
    if request.method == 'POST':
        context['post'] = True
        try:
            title = request.POST['title']
            content = request.POST['content']
            if title.isspace() or content.isspace():
                raise ValueError('Only spaces')
            if not Service.objects.filter(title=title, content=content, user=request.user):
                Service.objects.create(title=title, content=content, user=request.user)
        except ValueError as e:
            context['error'] = True

    context['services'] = Service.objects.filter(user=request.user).order_by("-created")
    return render(request, 'connect/my_services.html',context)



@login_required
def classifieds(request):
    context={'ads':Classified.objects.all().order_by("-created")}
    return render(request, 'connect/classifieds.html',context,)



@login_required
def my_classifieds(request):
    context={'post':False,'error':False}
    if request.method == 'POST':
        context['post'] = True
        try:
            title = request.POST['title']
            content = request.POST['content']
            if title.isspace() or content.isspace():
                raise ValueError('Only spaces')
            if not Classified.objects.filter(title=title, content=content, user=request.user):
                Classified.objects.create(title=title, content=content, user=request.user)
        except ValueError as e:
            context['error'] = True

    context['ads']=Classified.objects.filter(user=request.user).order_by("-created")
    return render(request, 'connect/my_classifieds.html',context)



@login_required
def travel(request):
    context={'travel':None, 'post':False, 'error':False, 'date':'', 'places':Place.objects.all()}
    if request.POST:

        try:
            if request.POST["type"] == 'search':
                context['post'] = True
                context['date'] = request.POST['date']
                from_place = Place.objects.get(pk=request.POST['my-location'])
                to_place = Place.objects.get(pk=request.POST['destination'])
                start_date = datetime.strptime(request.POST['date'], "%d/%m/%Y")
                date_range = (
                    timezone.make_aware(datetime.combine(start_date, datetime.min.time()), timezone.get_current_timezone()),
                    timezone.make_aware(datetime.combine(start_date, datetime.max.time()), timezone.get_current_timezone())
                )
                context['travel'] = Travel.objects.filter(date__range=date_range,from_place=from_place, to_place=to_place)
            elif request.POST["type"] == "create":
                content = request.POST['description']
                if content.isspace():
                    raise ValueError("only Spaces")
                from_place = Place.objects.get(pk=request.POST['my-location'])
                to_place = Place.objects.get(pk=request.POST['destination'])
                start_date = timezone.make_aware(datetime.strptime(request.POST['date'], "%d/%m/%Y %I:%M %p"), timezone.get_current_timezone())
                Travel.objects.create(date=start_date, from_place=from_place, to_place=to_place, content=content, user=request.user)
                return redirect('mytravel')

            else:
                return Http404("Your form is not authorised to make a request.")

        except ValueError as e:
            #print e
            context['error'] = True
        except:
            redirect("travel")


    return render(request, 'connect/travel.html',context)




@login_required
def calendar(request):
    context={}
    context['post']=False
    context['error']=False
    if request.method == 'POST':
        if not request.user.has_perm("connect.event_add"):
            raise Http404('You do not have permission')

        context['post'] = True
        try:
            title = request.POST['title']
            date_time = request.POST['date_time']
            if title.isspace():
                raise ValueError('Only spaces')
            date_time = timezone.make_aware(datetime.strptime(date_time, "%d/%m/%Y %I:%M %p"), timezone.get_current_timezone())
            date_time = date_time
            if not Event.objects.filter(user=request.user, title=title, time=date_time):
                Event.objects.create(user=request.user, title=title, time=date_time)
            else:
                pass
        except ValueError as e:
            context['error'] = True
        except:
            Http404("Some error occured")

    week = request.GET.get('week',0)
    week = int(week)
    context.update(get_weekly_calendar(week))
    return render(request, 'connect/calendar.html',context)




@login_required
def vote_problem(request):
    if request.method == 'POST':
        p_id = request.POST['p_id']
        problem = get_object_or_404(Problem, pk=p_id)
        try:
            vote = ProblemVote.objects.get(problem=problem, user=request.user)
            vote.delete()
        except ProblemVote.DoesNotExist:
            ProblemVote.objects.create(problem=problem, user=request.user)
        return HttpResponse(1)
    else:
        raise 	Http404("Cannot Vote")




@login_required
def problems(request, bhavan):
    bhavan = get_object_or_404(Bhavan,name=bhavan)
    problems = Problem.objects.all().filter(bhavan=bhavan).order_by('-votes')
    status = get_fav_status(problems,request.user)
    context = {'problems': problems, 'status_dict':status, 'bhavan':bhavan}
    return  render(request,'connect/problems_unsolved.html',context)




@login_required
def problems_solved(request, bhavan):
    bhavan = get_object_or_404(Bhavan,name=bhavan)
    problems = ProblemSolved.objects.all().filter(bhavan=bhavan).order_by('-pk')[0:30]
    context = {'problems': problems, 'bhavan':bhavan}
    return  render(request,'connect/problems_solved.html',context)



@login_required
def my_problems(request, bhavan):
    bhavan = get_object_or_404(Bhavan,name=bhavan)
    context={'post':False,'error':False}
    if request.method == 'POST':
        context['post'] = True
        try:
            title = request.POST['title']
            content = request.POST['content']
            if title.isspace() or content.isspace():
                raise ValueError('Only spaces')
            if not Problem.objects.filter(title=title, content=content, user=request.user, bhavan=bhavan):
                Problem.objects.create(title=title, content=content, user=request.user, bhavan=bhavan)
        except ValueError as e:
            context['error'] = True
    problems = Problem.objects.all().filter(bhavan=bhavan, user=request.user).order_by('-pk')
    context.update({'problems': problems, 'bhavan':bhavan})
    return  render(request,'connect/my_problems.html',context)




@login_required
def solve_problem(request, p_id):
    if not request.user.has_perm("connect.problem_solve"):
        raise Http404('You don\'t have permission to solve this')
    context={}
    context['post']=False
    context['error']=False
    context['problem'] = get_object_or_404(Problem,pk=p_id)
    problem = context['problem']
    if request.method == 'POST':

        context['post'] = True
        try:
            reply = request.POST['reply']
            if reply.isspace():
                raise ValueError('Only spaces')
            ProblemSolved.objects.create(user=problem.user, title=problem.title, reply=reply,
                                         solved_by=request.user, bhavan = problem.bhavan, posted_on = problem.created )
            if request.user != problem.user:
                gmail.send(problem.user.email, 'Your Problem has been solved by %s!'%request.user.first_name,
                           'Dear %s,\nRejoice! Your problem has been addressed.\n %s \n\n %s \n\n\n-regards\nSidhartha Namburi'%(problem.user.first_name,problem.title,reply))


            problem.delete()
            return redirect("problems_solved", bhavan=problem.bhavan.name)

        except ValueError as e:
            context['error'] = True


    else:
        return render(request, 'connect/solve_problem.html',context)


@login_required
def phone_db(request):
    if request.method == 'POST':
        nos = PhoneNumberDB.objects.filter(Q(name__istartswith=request.POST['q'])| Q(designation__icontains=request.POST['q']))
    else:
        nos = PhoneNumberDB.objects.all()


    return render(request, 'connect/misc_no.html', {'nos':nos})


@login_required
def book_search(request):
    if request.method == 'POST':
        books = Book.objects.filter(title__icontains=request.POST['q'])
    else:
        books = Book.objects.all()
    return render(request, 'connect/books.html', {'books':books})

@login_required
def my_book_orders(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']
        book = Book.objects.get(id=request.POST['book_id'])
        nos =  request.POST['nos']
        BookOrder.objects.create(user=request.user, nos=nos, phone=phone, address=address, book=book)
        return redirect('my_book_orders')
    else:
        return render(request, 'connect/books_order.html', {'orders':BookOrder.objects.filter(user=request.user)})

def del_book_orders(request, bo_id):
    order = BookOrder.objects.get(pk=bo_id)
    if order.user == request.user:
        order.delete()
    return redirect('my_book_orders')


@login_required
def view_store(request):
    return render(request, 'connect/store_in_town.html')

@login_required
def book_request_view(request):
    title =  request.POST['title']
    title = str(title)
    title.replace("'",'"')
    BookRequest.objects.create(user=request.user, title=title)
    return HttpResponse(1, status=200)