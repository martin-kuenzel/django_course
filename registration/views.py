from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from .forms import UserSignupForm

def user_signup(req):
    if req.method == 'POST':
        form = UserSignupForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(req)
            email_subject = 'Activate your account'
            message = render_to_string('registration/activate_account.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject,message,to=[to_email])
            email.send()
            return HttpResponse('An email has been sent to you. Please confirm your account.')
    else:
        form = UserSignupForm()
    return render(req, 'registration/signup.html', {'form':form} )

def activate_account(req,uidb64,token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        return HttpResponse('Your account has been activated successfully')
    else:
        return HttpResponse('Invalid Activation link')
