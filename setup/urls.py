from django.contrib import admin
from django.urls import path ,include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudantesViewSet, ListaMatriculaCursosViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('estudante', EstudanteViewSet, basename="Estudante")
router.register("curso", CursoViewSet, basename="Curso")
router.register("matricula", MatriculaViewSet, basename="Matricula")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("estudantes/<int:pk>/matriculas", ListaMatriculaEstudantesViewSet.as_view()),
    path("cursos/<int:pk>/matriculas", ListaMatriculaCursosViewSet.as_view())
]

