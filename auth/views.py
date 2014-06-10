from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from forms import RegisterForm, EditAccountForm, ChangeEmailForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        nextPage = request.POST.get("next", "/")
        form = RegisterForm(request.POST)
        if form.is_valid():
            # new_user = form.save()
            try:
                form.save()
            except:
                print("Unable to save form...")
                return render_to_response("registration/registration.html", {'form': form, 'next': nextPage}, context_instance=RequestContext(request))
            # log the user in before sending them to their next destination
            user = authenticate(username=request.POST.get("username"), password=request.POST.get("password1"))
            login(request, user)
            ### TODO Create account here!
            # account = Account()
            # account.user = User.objects.get(pk=user.id)
            # account.created_by = user
            # account.save()
            #
            return redirect(nextPage)
        else:
            print("errors in registration")
            print(form.errors)

    else:
        form = RegisterForm()
        nextPage = request.GET.get("next", "/")
    return render_to_response("registration/login.html", {}, context_instance=RequestContext(request))


def login_func(request):
    nextPage = request.GET.get("next", "/")
    state = ""
    if request.method == 'POST':
        nextPage = request.POST.get("next", "/")  # in theory we could take the default from before, but in case a url gets weird lets set a real default
        try:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        state = "You're successfully logged in!"
                    else:
                        state = "Your account is not active, please contact the site admin."
                else:
                    state = "Your username and/or password were incorrect."
                login(request, user)
                return redirect(nextPage)
            else:
                state = "Your username and/or password were incorrect."
                return render_to_response("registration/login.html", {'a_form': form, 'next': nextPage, 'state': state}, context_instance=RequestContext(request))
        except Exception as e:
            print("Error authenticating form")
            print(e)

    else:
        form = AuthenticationForm()

    return render_to_response("registration/login.html", {'a_form': form, 'next': nextPage, 'state': state}, context_instance=RequestContext(request))

@login_required
def account_settings(request):
    pass

@login_required
def change_password(request):
    if request.method == "POST":
        try:
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('dashboard.views.home')
                except Exception as e:
                    print("Error saving form")
            else:
                return render_to_response("registration/change_password.html", {'form': form}, context_instance=RequestContext(request))
        except Exception as e:
            print("Error validating password")
            print(e)
    else:
        form = EditAccountForm(SetPasswordForm)
    return render_to_response("registration/change_password.html", {'form': form}, context_instance=RequestContext(request))

@login_required
def change_email(request):
    if request.method == "POST":
        try:
            form = ChangeEmailForm(data=request.POST)
            if form.is_valid():
                try:
                    user = request.user
                    user.email = request.POST['email']
                    user.save()
                    return redirect('dashboard.views.home')
                except Exception as e:
                    print(e)

            else:
                print "form not valid"
        except Exception as e:
            print("Error getting email from database")
            print(e)
    else:
        form = ChangeEmailForm()
    return render_to_response("registration/change_email.html", {'form': form}, context_instance=RequestContext(request))
