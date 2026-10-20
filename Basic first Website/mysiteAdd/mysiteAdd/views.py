# Thet are New File
from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path


def index(request):
    return render(request, "index.html")
    # return HttpResponse("Hello, world. You're the first time!")


def analize(request):
    # Get the Text
    djtext = request.POST.get('test', 'default')

    # Check box Value
    removepunc = request.POST.get('removepunc', 'off')
    ConvertUpperCase = request.POST.get('ConvertUpperCase', 'off')
    remove_Space = request.POST.get('remove_Space', 'off')
    newLineRemover = request.POST.get('newLineRemover', 'off')
    charCount = request.POST.get('charCount', 'off')

    # Check Which CheckBox Is On
    if removepunc == "on":
        punctuations = '''!".,?!:;'—–-()[]{}.../@&#*_^+=>`~|§¶"'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'porpose': 'Removed Punctution', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, "analize.html", params)

    if ConvertUpperCase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'porpose': 'Convert UpperCase', 'analyzed_text': analyzed}

        djtext = analyzed
        # return render(request, "analize.html", params)


    if remove_Space == "on":
        analyzed = "".join(djtext.split())
        # for index, char in enumerate(djtext):
        #     if not (djtext[index] == " " and djtext[index + 1] == " "):
        #         analyzed = analyzed + char
        params = {'porpose': 'Convert remove Space', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, "analize.html", params)


    if newLineRemover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'porpose': 'Convert Remove New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, "analize.html", params)


    if charCount == "on":
        analyzed = (" Count of Charecter :- " + str(len(djtext)))
        params = {'porpose': 'Characters Counted', 'analyzed_text': analyzed}
        # djtext = analyzed
        # return render(request, "analize.html", params)

    if (removepunc != "on" and ConvertUpperCase != "on" and remove_Space != "on" and newLineRemover != "on" and charCount != "on"):
        return HttpResponse("Please the One Switch ")

    return render(request, "analize.html", params)


    # return render(request, "index.html")


def ex1(request):
    return render(request, "ex1.html")


def contact(request):
    # This return back to index page
    # return HttpResponse('Remove <a href="/"> Back</a>')
    return render(request, "contact.html")


def loginrw(request):
    with open("rw.txt", 'r') as f:
        return HttpResponse(f.read())


def loginmt(request):
    file_path = Path(__file__).resolve().parent / "mt.txt"
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()

    return HttpResponse(data)


def logout(request):
    file_open = Path(__file__).resolve().parent / "kkr.txt"
    with open(file_open, "r", encoding="utf-8") as f:
        result = f.read()
        return HttpResponse(result)
