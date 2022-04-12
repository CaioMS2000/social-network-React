from fastapi.security import OAuth2PasswordRequestForm

class Custom_OAuth2PasswordRequestForm(OAuth2PasswordRequestForm):
    email: str

#aparentemente custumizar o formulario não é possivel
#porem essa tentativa não atrapalha o funcionamento, pois a classe original foi herdada