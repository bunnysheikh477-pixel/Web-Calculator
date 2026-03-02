from django.shortcuts import render

def home(request):
    request.session['expression'] = ""
    return render(request, 'index.html', {'display': ""})

def calculator(request):
    expression = request.session.get('expression', "")

    if request.method == "POST":

        if 'num' in request.POST:
            expression += request.POST['num']

        elif 'operator' in request.POST:
            expression += request.POST['operator']

        elif request.POST.get('action') == '=':
            try:
                expression = str(eval(expression))
            except Exception:
                expression = "Error"

        elif request.POST.get('action') == 'C':
            expression = ""

        request.session['expression'] = expression

    return render(request, 'index.html', {'display': expression})
