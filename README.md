# MeowsApps
Red social para publicar pequeños maullidos de los usuarios felinos 

Esta es una aplicacion la cual permite crear pequeños post de usuarios (maullidos). Permite crear un perfil de usuario , Hacer un login y desde su perfil crear un maullido el cual sera posible ver por los diferentes usuarios. Tambien permite crear relaciones de seguidores o dejarlos de seguir. 

Pasos para instalar la aplicacion 

- iniciamos un entorno virtual ( python -m venv venv )
- ejecutamos el entorno virtual ( .\venv\Scripts\activate )
- instalamos django y pillow ( pip install django pillow )

  ya en las carpetas viene creado el proyecto asi como la aplicacion y la db en sqlite
- ejecutamos el servidor para dar inicio a la app ( python manage.py runserver )
- se visualiza en el localhost:8000 
las librerias utilizadas son django para todo el proceso del backend y pillow que nos permite poder trabajar y cargar imagenes

Aspectos a mejorar con el tiempo con respeto a lo visual , y poder dar un like/unlike en las publicaciones. Esto mejora mas la experiencia con el usuario. Otro aspecto a mejorar es que el usuario le permita cargar la imagen desde registro de su perfil, ya que cuando el crea su perfil , este crea una imagen por defecto y solo un superadmin la puede modificar. 
