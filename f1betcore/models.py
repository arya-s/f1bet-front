from django.db import models

import json


class RedditUser(models.Model):
    name = models.TextField()
    flair = models.TextField(null=True)
    points = models.TextField(default="[]")

    def get_points_list(self):
        return json.loads(self.points)

    def get_points(self):
        points = json.loads(self.points)

        return sum(points)

    def add_points(self, points):
        cur_points = json.loads(self.points)
        cur_points.append(points)

    def __unicode__(self):
        return u"{0} {1}".format(self.name, self.get_points())


class Team(models.Model):
    name = models.TextField()
    points = models.TextField(default="[]")

    def get_points_list(self):
        return json.loads(self.points)

    def get_points(self):
        points = json.loads(self.points)

        return sum(points)

    def add_points(self, points):
        cur_points = json.loads(self.points)
        cur_points.append(points)

    def __unicode__(self):
        return u"{0} - {1}".format(self.name, self.get_points())


class Driver(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    team = models.ForeignKey(Team)
    number = models.IntegerField(null=True)
    points = models.TextField(default="[]")

    def full_name(self):
        return u"{0} {1}".format(self.first_name, self.last_name)

    def get_points_list(self):
        return json.loads(self.points)

    def get_points(self):
        points = json.loads(self.points)

        return sum(points)

    def add_points(self, points):
        cur_points = json.loads(self.points)
        cur_points.append(points)

    def __unicode__(self):
        return u"{0} - {1} - {2}".format(self.full_name(), self.team.name, self.get_points())


class DriverShort(models.Model):
    tlid = models.TextField(null=True)
    driver = models.ForeignKey(Driver)

    def get_driver(self):
        return driver.full_name()

    def __unicode__(self):
        return u"{0} - {1}".format(self.tlid, self.driver.full_name())


class Race(models.Model):
    round = models.IntegerField(default=0)
    grand_prix = models.TextField()
    circuit = models.TextField()
    deadline = models.DateTimeField()
    finished = models.BooleanField(default=False)
    driver_list = models.ManyToManyField(Driver)

    def __unicode__(self):
        return u"{0} - {1}".format(self.round, self.grand_prix)


class Bet(models.Model):
    user = models.ForeignKey(RedditUser)
    race = models.ForeignKey(Race)
    timestamp = models.TextField()
    drivers = models.ManyToManyField(Driver)

    def __unicode__(self):
        return u"{0} - {1}".format(self.user.name, self.race.grand_prix)

