from django.db import models

class Voter(models.Model):
    voter_id = models.IntegerField("Voter ID")
    voter_name = models.CharField("Voter Name", max_length=200)
    password = models.CharField("Password", max_length=200)
    email = models.EmailField("Email")
    is_voted = models.BooleanField(default=False)
    def __str__(self):
        return str(self.voter_id)

class Candidate(models.Model):
    cid = models.IntegerField('Candidate ID')
    cname = models.CharField('Candidate Name', max_length=200)
    partyname = models.CharField('Party Name', max_length=200)
    symbol = models.ImageField("Symbol", upload_to='candidate/')
    voted = models.IntegerField(default=0)
    def vote_count(self):
        return Vote.objects.filter(candidate=self).count()
    

    def __str__(self):
        return self.cname
    
class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.voter.voter_name} voted for {self.candidate.cname}"

