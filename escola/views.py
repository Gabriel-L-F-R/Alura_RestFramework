from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudantesSerializer, ListarMatriculasCursoSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    
class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    
class ListaMatriculaEstudantesViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs["pk"])
        return queryset
    serializer_class = ListaMatriculasEstudantesSerializer
    
class ListaMatriculaCursosViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs["pk"])
        return queryset
    serializer_class = ListarMatriculasCursoSerializer