from finqueue import views 
from users.models import User
user = User.objects.first()
recommendations = views.user_ranking(user)
print(recommendations)
