from apphos.viewsets import pacienteViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('paciente',pacienteViewset)

#url/paciente