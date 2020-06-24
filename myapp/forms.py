from django import forms
from myapp.models import UserData, Activity


class UserForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["id"].label = "Unique Id"
        self.fields["real_name"].label = "Name"
        self.fields["tz"].label = "TimeZone"


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].label = "User"
        self.fields["start_time"].label = "Start Time"
        self.fields["end_time"].label = "End Time"
