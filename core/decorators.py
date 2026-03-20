from django.shortcuts import redirect

def role_required(role):
    def wrapper(view_func):
        def inner(request, *args, **kwargs):
            if request.user.profile.role != role:
                return redirect('error')
            return view_func(request, *args, **kwargs)
        return inner
    return wrapper
