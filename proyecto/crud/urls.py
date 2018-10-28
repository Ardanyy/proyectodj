from django.urls import path,include
from  .views import Usuarioslogin,HomePageView,PageListSlider,PageListjuego,PageListplataformas,PageListControles,PageListGeneros,PageListDistribuidora,Detailjuego,Createjuego,Createplataformas,CreateControles,CreateGenero,CreateDistribuidora,CreateSlider,Updatecontroles,Updatejuego,Updateplataformas,UpdateGenero,UpdateDistribuidora,UpdateSlider,Deletejuego,DeletePlataformas,DeleteControl,DeleteGenero,DeleteDistribuidora,DeleteSlider
pages_patters = ([
   path('', HomePageView.as_view(), name='home'),
   path('<int:pk>/', Detailjuego.as_view(), name='detalle'),

   path('juegos/', PageListjuego.as_view(), name='inicio'),
   path('plataformas/', PageListplataformas.as_view(), name='plataformas'),
   path('controles/', PageListControles.as_view(), name='controles'),
   path('generos/', PageListGeneros.as_view(), name='generos'),
   path('distribuidora/', PageListDistribuidora.as_view(), name='distribuidora'),
   path('slider/', PageListSlider.as_view(), name='slider'),

   path('create/', Createjuego.as_view(), name='crear'),
   path('plataformas/create/', Createplataformas.as_view(), name='nuevop'),
   path('controles/create/', CreateControles.as_view(), name='nuevoc'),
   path('generos/create/', CreateGenero.as_view(), name='nuevog'),
   path('   /create/', CreateDistribuidora.as_view(), name='nuevod'),
   path('slider/create/', CreateSlider.as_view(), name='nuevos'),

   path('actualizar/<int:pk>/', Updatejuego.as_view(), name='actualizar'),
   path('plataformas/actualizar/<int:pk>/', Updateplataformas.as_view(), name='actualizarp'),
   path('controles/actualizar/<int:pk>/', Updatecontroles.as_view(), name='actualizarc'),
   path('generos/actualizar/<int:pk>/', UpdateGenero.as_view(), name='actualizarg'),
   path('distribuidora/actualizar/<int:pk>/', UpdateDistribuidora.as_view(), name='actualizard'),
   path('slider/actualizar/<int:pk>/', UpdateSlider.as_view(), name='actualizars'),

   path('eliminar/<int:pk>/', Deletejuego.as_view(), name='eliminar'),
   path('plataformas/eliminar/<int:pk>/', DeletePlataformas.as_view(), name='eliminarp'),
   path('controles/eliminar/<int:pk>/', DeleteControl.as_view(), name='eliminarc'),
   path('generos/eliminar/<int:pk>/', DeleteGenero.as_view(), name='eliminarg'),
   path('distribuidora/eliminar/<int:pk>/', DeleteDistribuidora.as_view(), name='eliminard'),
   path('slider/eliminar/<int:pk>/', DeleteSlider.as_view(), name='eliminars'),
   path('accounts/',include('django.contrib.auth.urls')),
    
], 'app')   