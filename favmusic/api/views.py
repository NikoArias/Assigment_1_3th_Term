from django.shortcuts import render
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world")


# http POST 127.0.0.1:8000/api/register username=lalalala password=lalalal.

def register_api_endpoint(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"msg":"something went wrong"}, status= 400)

        username = data.get("username")
        password = data.get("password")

        if username == None:
            return JsonResponse({"msg":"you forgot the username."})
        elif password == None:
            return JsonResponse({"msg":"you forgot the password."})
        else:
            return JsonResponse({"Message":"account created"})
    else:
        return JsonResponse({"Console":"Try again."}, status=405)

# http POST 127.0.0.1:8000/api/login username=lalalala password=lalalal.

def login_api_endpoint(request):
    if request.method == "POST":
          try:
              data = json.loads(request.body)
          except:
              return JsonResponse({"msg":"something went wrong"}, status= 400)

          username = data.get("username")
          password = data.get("password")

          if username == None:
              return JsonResponse({"msg":"you forgot the username."})
          elif password == None:
              return JsonResponse({"msg":"you forgot the password."})
          else:
              return JsonResponse({"Token":"123456"})
    else:
              return JsonResponse({"Console":"Try again."}, status=405)

# http GET 127.0.0.1:8000/api/music.
# http POST 127.0.0.1:8000/api/login artist=lalalala song=lalalal.

def list_create_music_api_endpoint(request):
    if request.method == "GET":
        # return JsonResponse({"msg":"working"})
        return  JsonResponse({"results":[{"id": 1, "artist": "Some artist name", "song_title":"lalala"}]})
    elif request.method == "POST":
         try:
             data = json.loads(request.body)
         except:
             return JsonResponse({"msg":"something went wrong"}, status= 400)

         artist = data.get("artist")
         song_title = data.get("song")


         if artist == None:
             return JsonResponse({"msg":"you forgot the artist."})
         elif song_title == None:
             return JsonResponse({"msg":"you forgot the song."})
         else:
             return JsonResponse({"Message":"record created"})
    else:
        return JsonResponse({"msg":"try again"}, status=405)

# http GET 127.0.0.1:8000/api/rud/("id").
# http PUT 127.0.0.1:8000/api/rud/("id") artist=lalalala song=lalalal.
# http DELETE 127.0.0.1:8000/api/rud/("id").

def comments_rud_api_endpoint(request, id):
    if request.method == "GET":
        return JsonResponse({"results": [{"id": id, "artist": "Some random artist", "SongTitle": "some random song"}]})

    elif request.method == "PUT":

        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"msg":"something went wrong"}, status= 400)

        artist_name = data.get("artist")
        song_name = data.get("song")

        return JsonResponse({"id": id, "Artist": artist_name, "SongName": song_name})
        return JsonResponse({"Console": "Successfully updated"})

    elif request.method == "DELETE":
        return JsonResponse({"msg":"Record Successfully deleted"})
    else:
        return JsonResponse({"message" : "something went wrong, try again"}, status=405)
