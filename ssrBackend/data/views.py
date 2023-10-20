from django.shortcuts import render
from django.http import JsonResponse
from .models import Project,teamDetails
from .serializers import projectSerializer,teamDetailsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


imgLink = 'https://ssramritapuri.blob.core.windows.net/data/img/'
@api_view(['GET'])
def projects(request):
    try:
        # Retrieve all projects from the database
        projects = Project.objects.all()
        # Serialize the data using projectSerializer
        serializer = projectSerializer(projects, many=True)
        for i in serializer.data:
            im = []
            t = i['img'].split()
            for a,b in enumerate(t):
                if b=='Y':
                    im.append(imgLink+i['projectId']+'-img'+str(a+1)+'.jpg')
            i['img'] = im
        # Return the serialized data as a JSON response
        pages = [serializer.data[i:i + 20] for i in range(0, len(serializer.data), 20)]
        return JsonResponse(pages, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse(
            {"detail": "An error occurred: " + str(e)},
            status=500
        )


def projectDetails(request, teamId):
    try:
        project = Project.objects.filter(projectId=teamId).first()
        team = teamDetails.objects.filter(projectId=teamId)
        
        if project is not None and team is not None:
            # Serialize the data from both models
            project_data = projectSerializer(project).data
            team_data = teamDetailsSerializer(team, many=True).data
            project_data['category'] = project_data['category'].split(',')
            im = []
            t = project_data['img'].split()
            for a,b in enumerate(t):
                if b=='Y':
                    im.append(imgLink+project_data['projectId']+'-img'+str(a+1)+'.jpg')
            project_data['img'] = im
            # Create a dictionary to combine the data
            combined_data = {
                "project": project_data,
                "team": team_data,
            }
            
            return JsonResponse(combined_data, safe=False)
        else:
            return JsonResponse({"detail": "Team or project not found"}, status=404)
    except Exception as e:
        print(e)
        return JsonResponse({"detail": "An error occurred"}, status=500)