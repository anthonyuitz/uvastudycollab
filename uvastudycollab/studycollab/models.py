from django.db import models

class group(models.Model):
    users = models.CharField(max_length=500, blank=True)
    groupName = models.CharField(max_length=100, blank=True)

    def setGroup(self, x):
        self.users = json.dumps(x)

    def getGroup(self, x):
        return json.loads(self.users)
