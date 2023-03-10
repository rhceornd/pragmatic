'''
update에서 아이디 비활성화를 위하여 views.py의
AccountUpdateView의 form_class 상속받아 수정
'''

from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True